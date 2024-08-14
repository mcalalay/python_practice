import time,boto3,os
import pandas as pd
from datetime import datetime
from datetime import datetime, timedelta
from dateutil import tz
from io import StringIO
total_run_time = time.time()

notebook_instance_name = os.environ['NOTEBOOK_INSTANCE_NAME']

# athena constant
DATABASE = ####
TABLE = ####
JOB_LEVEL_TABLE = ####
WORKGROUP = ####

# S3 constant
S3_OUTPUT = ####
S3_BUCKET = ####
SSE_KMS_KEY = '84547fa1-852e-4ca9-a5fc-7c6416bd0f5b'
ENVIRONMENT = ####
BUCKET=#### # Or whatever you called your bucket
DATASET = ####

# Query Retries
RETRY_COUNT = 100

## added for oie dash status message
def csv_logger(today, component, status, message, order, file):
    logger_df = pd.DataFrame(columns=['date', 'component', 'status', 'message', 'order'])
    logger_df = logger_df.append({'date': today, 'component': component, 'status': status, 'message': message, 'order':order}, ignore_index=True)
    bucket = 'opsnav-client110'
    filename = 'fbaisquad/prod/datasets/sagemaker_redshift_logs/{}'.format(file)
    logger_buffer = StringIO()
    logger_df.to_csv(logger_buffer, index=False)
    s3_resource = boto3.resource('s3')
    s3_resource.Object(bucket, filename).put(Body=logger_buffer.getvalue())

## parse results into a dictionary
def parse_response(response):
    results_dictionary = {}
    num_of_cols=0
    columns_index_dictionary = {}
    # generate keys from columns
    for column_name in response['ResultSet']['Rows'][0]['Data']:
        column_name = column_name['VarCharValue']
        results_dictionary[column_name] = []
        columns_index_dictionary[column_name] = num_of_cols
        num_of_cols+=1
    # remove columns from resultset
    response['ResultSet']['Rows'].pop(0)
    # add rows to column
    for row in response['ResultSet']['Rows']:
        for column, index in columns_index_dictionary.items():
            try:
                results_dictionary[column].append(row['Data'][index]['VarCharValue'])
            except Exception:
                results_dictionary[column].append(None)
    return results_dictionary

def await_notebook_stopped(sagemaker, notebook_instance_name):
    try:
        describe_notebook_response = sagemaker.describe_notebook_instance(
            NotebookInstanceName=notebook_instance_name
        )
        while(describe_notebook_response['NotebookInstanceStatus'] != 'Stopped'):
            print("Waiting For Notebook Instance To Be Stopped")
            describe_notebook_response = sagemaker.describe_notebook_instance(
            NotebookInstanceName=notebook_instance_name
            )
            time.sleep(5)
    except Exception as e:
        print(str(e))
        return False
    return True

def await_query_execution(query_execution_id, retry_count, client):
    for i in range(1, 1 + retry_count):
        query_status = client.get_query_execution(QueryExecutionId=query_execution_id)
        query_execution_status = query_status['QueryExecution']['Status']['State']
        if query_execution_status == 'SUCCEEDED':
            print("STATUS:" + query_execution_status)
            return query_execution_status
        if query_execution_status == 'FAILED':
            return query_execution_status
        else:
            print("STATUS:" + query_execution_status)
            time.sleep(i)
    else:
        client.stop_query_execution(QueryExecutionId=query_execution_id)
        return 'TIMEOUT'

def start_sagemaker(latest_date,notebook_instance_name,lifecycle_config):
    sagemaker = boto3.client(service_name='sagemaker', region_name='us-east-1')
    describe_notebook_response = sagemaker.describe_notebook_instance(
        NotebookInstanceName=notebook_instance_name
    )
    ## add lifecycle config
    if await_notebook_stopped(sagemaker,notebook_instance_name):
        update_notebook_response = sagemaker.update_notebook_instance(
            NotebookInstanceName=notebook_instance_name,
            LifecycleConfigName=lifecycle_config,
        )
    
    ## start sagemaker
    if await_notebook_stopped(sagemaker,notebook_instance_name):
        sagemaker_response = sagemaker.start_notebook_instance(
                NotebookInstanceName=notebook_instance_name
        )
    message = "{} instance started running with latest Job level as of {}".format(notebook_instance_name, latest_date)
    subject = "[{}] Started Running".format(notebook_instance_name)
    client = boto3.client('sns')
    response = client.publish(
        TargetArn='arn:aws:sns:us-east-1:005484526251:opsnav-client110-fbaisquad-sagemaker-state',
        Message=message,
        Subject=subject,
        MessageStructure='string'
    )
    
def check_files_present(s3_client, bucket, to_check, ENVIRONMENT):
    empty_folders = []
    files_present = []
    for s3_key in to_check:
        response = s3_client.list_objects(Bucket=bucket,Prefix=ENVIRONMENT+s3_key)
        if 'Contents' in response and len(response['Contents']) > 1:
            files_present.append(s3_key)
        else:
            empty_folders.append(s3_key)
    return (files_present, empty_folders)

def lambda_handler(event, context):
    query = "SELECT max(wk_end_fri) as ds FROM {DATABASE}.{TABLE};".format(DATABASE=DATABASE, TABLE=TABLE)
    # athena client
    client = boto3.client('athena', region_name='us-east-1')

    # Execution
    response = client.start_query_execution(
        QueryString=query,
        QueryExecutionContext={
            'Database': DATABASE
        },
        ResultConfiguration={
            'OutputLocation': S3_OUTPUT,
            'EncryptionConfiguration': {
            'EncryptionOption': 'SSE_KMS',
            'KmsKey': SSE_KMS_KEY
        }
        },
        WorkGroup=WORKGROUP
    )
    query_execution_id = response['QueryExecutionId']
    
    job_level_query = "SELECT max(date_parse(ds,'%Y-%m-%d')) as ds FROM {DATABASE}.{TABLE};".format(DATABASE=DATABASE, TABLE=JOB_LEVEL_TABLE)
    job_level_response = client.start_query_execution(
        QueryString=job_level_query,
        QueryExecutionContext={
            'Database': DATABASE
        },
        ResultConfiguration={
            'OutputLocation': S3_OUTPUT,
            'EncryptionConfiguration': {
            'EncryptionOption': 'SSE_KMS',
            'KmsKey': SSE_KMS_KEY
        }
        },
        WorkGroup=WORKGROUP
    )
    job_level_query_execution_id = job_level_response['QueryExecutionId']
    
    can_run_sagemaker = False
    
    s3 = boto3.client('s3', region_name='us-east-1')
    bucket = 'opsnav-client110'
    to_check = ['weather_holiday/final/',
                'pm/final/',
                'shifts/final/',
                'bugs/final/',
                'co_app_roster/rolling/',
                'training/final/',
                'absenteeism/final/',
                'action_severity/final/',
                'activity_code/final/',
                'backlog/final/',
                'events/final/',
                'rep_occupancy_actors/final/',
                'review_type/final/',
                'job_level_workflow_status/rolling/',
                'dmr_summary/rolling/']
    
    ok_folders, empty_folders = check_files_present(s3, bucket, to_check, ENVIRONMENT)
    if await_query_execution(query_execution_id,RETRY_COUNT, client) == 'SUCCEEDED' and await_query_execution(job_level_query_execution_id,RETRY_COUNT, client) == 'SUCCEEDED':
        result = client.get_query_results(QueryExecutionId=query_execution_id)
        job_level_result = client.get_query_results(QueryExecutionId=job_level_query_execution_id)
        latest_modeling_date_key = 'fbaisquad/athena-query-results/{}.csv'.format(query_execution_id)
        client = boto3.client('s3',  region_name='us-east-1')
        obj = client.get_object(Bucket=BUCKET, Key=latest_modeling_date_key)
        latest_modeling_date_df = pd.read_csv(obj['Body'])
        latest_job_level_date_key = 'fbaisquad/athena-query-results/{}.csv'.format(job_level_query_execution_id)
        job_level_obj = client.get_object(Bucket=BUCKET, Key=latest_job_level_date_key)
        latest_job_level_export_df = pd.read_csv(job_level_obj['Body'])
        latest_job_level_export_ds = max(pd.to_datetime(latest_job_level_export_df['ds'], errors='coerce'))
        latest_modeling_ds = max(pd.to_datetime(latest_modeling_date_df['ds'], errors='coerce'))
        DAYS_TO_ADD = 7
        expected_export_date = (latest_modeling_ds + timedelta(days=DAYS_TO_ADD))
        print("latest job level export date {}".format(str(latest_job_level_export_ds)))
        print("latest srt modeling date {}".format(str(latest_modeling_ds)))
        print("latest expected_export_date date {}".format(str(expected_export_date)))
        print(empty_folders)
        if (latest_job_level_export_ds >= expected_export_date) and (latest_modeling_ds < expected_export_date)and not empty_folders:
            can_run_sagemaker=True
            start_sagemaker(str(latest_job_level_export_ds),notebook_instance_name,'opsnav-client110-co-ac-scoring-v2-on-start-prod')
        elif (datetime.now() >= (expected_export_date + timedelta(days=2))):
            #log error message on oie dash
            from_zone = tz.gettz('UTC')
            to_zone = tz.gettz('America/Los_Angeles')
            utc = datetime.utcnow()
            utc = utc.replace(tzinfo=from_zone)
            pst = utc.astimezone(to_zone)
            today = pst.date()
            csv_logger(today, 'Pipeline', 0, 'OIE AC AWS Automated Pipeline Stalled on {}'.format(today), 1, 'pipeline_log.csv')
            csv_logger(today, 'Status Details', 0, 'Experiencing Upstream SRT Data Delay', 2, 'status_details.csv')
    return {
        'statusCode': 200,
        'body': {'sagemaker_ran': can_run_sagemaker,
                 #'latest_date': str(latest_job_level_export_ds) if latest_job_level_export_ds > latest_modeling_ds else str(latest_modeling_ds),
                 'empty_folders': str(empty_folders)
        }
    }
