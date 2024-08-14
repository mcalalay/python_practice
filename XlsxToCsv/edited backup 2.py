import openpyxl
import csv
import io


if source_key.endswith(".xlsx"):
    print("Processing Excel Files")
    print("this is the key", record['s3']['object']['key'])
    print("this is the source config keyt", source_config_bucket)
    print("the source key:", source_key)
    print("this is the sourceLocation: ", config['sourceLocation'])

    file_obj = s3_client.get_object(Bucket=source_config_bucket, Key=record['s3']['object']['key'])
    file_content = file_obj["Body"].read()
    read_excel_data = io.BytesIO(file_content)
    df = pd.read_excel(read_excel_data, config['columnToExtract'])
    df.to_csv('/tmp/extracted.csv')

    response, destination_key, filename = move_s3_object(
        's3://oiepartnerpilot-datasets-raw-dev/testing-resolution/agent_list/extracted.csv', config['rawLocation'])
    print("destination_key " + destination_key)

    s3_client.upload_file('/tmp/extracted.csv', source_config_bucket, destination_key)