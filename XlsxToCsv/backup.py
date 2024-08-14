import json
import pandas as pd
import boto3
import logging
import os
import io
import openpyxl
import csv
from data_preprocessing import preprocessing

s3 = boto3.resource('s3')
s3_client = boto3.client('s3')


def is_valid_schema(schema, expected_schema):
    logging.info("Expected Schema")
    logging.info(expected_schema)
    logging.info("Received Schema")
    logging.info(schema)
    return len(set(expected_schema) - set(schema)) == 0


def move_s3_object(source, destination):
    source_split = source.split("//")[1].split("/")
    source_bucket = source_split[0]
    source_split.pop(0)
    source_key = "/".join(source_split)
    filename = source_split[-1]
    destination_split = destination.split("//")[1].split("/")
    destination_bucket = destination_split[0]
    destination_split.pop(0)
    destination_key = "/".join(destination_split) + '/' + filename
    copy_source = {
        'Bucket': source_bucket,
        'Key': source_key
    }
    bucket = s3.Bucket(destination_bucket)
    obj = bucket.Object(destination_key)
    response = obj.copy(copy_source)
    logging.info(response)
    # response = s3.Bucket(source_bucket).delete_objects(Bucket=source_bucket, Delete={'Objects': [{'Key':source_key}]})
    logging.info(response)
    return response, destination_key, filename


def notify_sns(message):
    client = boto3.client('sns')
    arn = os.environ['SNS_ARN']
    response = client.publish(
        TargetArn=arn,
        Message=message,
        MessageStructure='json')
    logging.info(response)
    print("Response value is", response)
    return response


def validate_schema(config, schema):

    if schema = None:
        schema = pd.read_csv(config['sourceLocation'], header=0, nrows=0).columns.tolist()

    print("ACTUAL SCHEMA LOCATION", config['sourceLocation'])
    expected_schema = list(config['schema'])
    print("EXPECTED_SCHEMA", expected_schema)
    print("ACTUAL SCHEMA", schema)
    if is_valid_schema(schema, expected_schema):
        response, source_key, filename = move_s3_object(config['sourceLocation'], config['rawLocation'])
        print("source_key" + source_key)
        file_source = config['sourceLocation']
        print("File pass validation in raw folder")
        # Perform processing to staging by calling method
        preprocessing(file_source, config, filename)


    else:
        response = move_s3_object(config['sourceLocation'], config['quarantineLocation'])
        print("File move to quarantine")
        failure_message = {
            "subject": "[OIE PSO][ACTION REQUIRED] {SOURCE_LOCATION} FAILED SCHEMA CHECK".format(
                SOURCE_LOCATION=config['sourceLocation']),
            "message": """FAILED SCHEMA CHECK. Please correct and reupload file for {SOURCE_LOCATION}
                        Expected Schema is:
                        {EXPECTED_SCHEMA}
            """.format(SOURCE_LOCATION=config['sourceLocation'], EXPECTED_SCHEMA=config['schema']),
            "owner": config['dataOwnerEmail']
        }

        json_message = json.dumps({"default": json.dumps(failure_message)})
        print(json_message)
        response = notify_sns(json_message)
    return {
        'statusCode': 200,
        'body': response
    }


def lambda_handler(event, context):
    for record in event['Records']:
        ## TODO: cleanup below splitting, no need to do all of this splitting since the event object comes with bucket and key already split
        ## ENHANCEMENTS: if we want to be able to track validations configs by ci/cd, we should move all landing configs to a general folder, instead of inside a dataset specific folder
        ## then configs can be tracked in codecommit and deployed to s3 using codeploy. we would just need to follow a standard inside the general folder to allow automatic pickup based on dataset
        source_key = "s3://{BUCKET}/{KEY}".format(BUCKET=record['s3']['bucket']['name'],
                                                  KEY=record['s3']['object']['key'])
        final_source_key = source_key.replace("+", " ")
        print("FINAL SOURCE KEY" + " " + final_source_key)
        split_agent = final_source_key.split(".")
        print("SPLIT AGENT", split_agent)
        testing = split_agent[0]
        print("FINAL SPLIT", testing)

        split = source_key.split('//')
        print("FINAL SPLITTTT", split)
        split = "/".join(split).split('/')
        source_config_bucket = split[1]
        # source_config_key = split[2]
        # source_config_obj = split[3]
        # print("FINAL FOLDER", source_config_bucket + "/" source_config_key + source_config_obj)
        agent_filename = split[4]
        agent_split = agent_filename.split('.')
        final_agent = agent_split[0]

        split.pop(0)
        split.pop(0)
        dataset = split[1]

        source_config_key = "validation/{DATASET}.json".format(DATASET=dataset)

        s3_client.download_file(source_config_bucket, source_config_key, '/tmp/validation_config.json')

        config = None
        with open('/tmp/validation_config.json') as json_file:
            config = json.load(json_file)

            config['sourceLocation'] = final_source_key
            print("Source location is", config['sourceLocation'])
            print("LAST" + final_source_key)

        if source_key.endswith(".xlsx"):
            print("extrating to .csv")
            file_obj = s3_client.get_object(Bucket=source_config_bucket, Key=record['s3']['object']['key'])
            file_content = file_obj["Body"].read()
            read_excel_data = io.BytesIO(file_content)
            df = pd.read_excel(read_excel_data, config['sheetToExtract'])
            df.to_csv('/tmp/extracted.csv')
            df = pd.read_csv('/tmp/extracted.csv')
            first_column = df.columns[0]
            df = df.drop([first_column], axis=1)
            df.to_csv('/tmp/extracted.csv', index=False)
            print("file converted to .csv")

            s3_client.upload_file('/tmp/extracted.csv', config['extractedCsvBucket'],
                                  config['extractedCsvLocation'] + final_agent + config['fileExtension'])
            agent_path = "s3://" + config['extractedCsvBucket'] + "/" + config['extractedCsvLocation'] + final_agent + \
                         config['fileExtension']
            schema = pd.read_csv(agent_path, header=0, nrows=0).columns.tolist()
            print("FINAL SCHEMA FOR AGENT", schema)



        if config:
            response = validate_schema(config, schema)
        return {
            'statusCode': 200,
            'body': response
        }
