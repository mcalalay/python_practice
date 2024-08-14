import openpyxl

filename = 'C:/Users/matthew.a.calalay/Downloads/Agent_List_V2.xlsx'


## opening the xlsx file
wb = openpyxl.load_workbook(filename)

## masterAgentList
##masterAgentList = wb.get_sheet_names()[1] deprecated code
masterAgentList = wb.sheetnames()[1]
###worksheet = wb.get_sheet_by_name(masterAgentList) deprecated  code
worksheet = wb[masterAgentList]


## getting the data from the sheet
data = worksheet.rows

## creating a csv file
csv = open("data.csv", "w+")

for row in data:
    l = list(row)
    for i in range(len(l)):
        if i == len(l) - 1:
            csv.write(str(l[i].value))
        else:
            csv.write(str(l[i].value) + ',')
        csv.write('\n')

## close the csv file
csv.close()

if source_key.endswith(".xlsx"):
    file_obj = s3_client.get_object(Bucket=source_config_bucket, Key=file_config_name)
    file_content = file_obj["Body"].read()
    read_excel_data = io.BytesIO(file_content)
    df = pd.read_excel(read_excel_data)
    df.to_csv('/tmp/updated.csv')

    s3_resource = boto3.resource('s3')
    s3_resource.Bucket(config['rawLocation']).upload_file('/tmp/updated.csv')