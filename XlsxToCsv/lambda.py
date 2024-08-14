if source_key.endswith(".xlsx"):
    ## opening the xlsx file
    wbFromS3 = s3.Object(config['stagingLocation'], source_key)
    wb = load_workbook(wbFromS3)
    # wb = openpyxl.load_workbook(source_key)

    ## masterAgentList
    masterAgentList = wb.get_sheet_names()[1]
    worksheet = wb.get_sheet_by_name(masterAgentList)

    ## getting the data from the sheet
    data = worksheet.rows

    ## creating a csv file
    csv = open(file_config_name, "w+")

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
        s3_client.download_file(source_config_bucket, file_config_name, '/tmp/wb.xlsx')
        ## opening the xlsx file

        # data = s3.Object(config['stagingLocation'], source_key)
        # binary_data = obj['Body'].read()
        # wb = openpyxl.load_workbook(BytesIO(binary_data)

        wb = openpyxl.load_workbook('/tmp/wb.xlsx')

        # wbFromS3 = s3.Object(config['stagingLocation'], source_key)
        # wb = load_workbook(wbFromS3)
        # wb = openpyxl.load_workbook(source_key)

        ## masterAgentList

        masterAgentList = wb.get_sheet_names()[1]
        worksheet = wb.get_sheet_by_name(masterAgentList)

        # masterAgentList = wb.sheetnames
        # worksheet = wb[masterAgentList[1]]

        ## getting the data from the sheet
        data = worksheet.rows

        ## creating a csv file
        csv = open(file_config_name, "w+")

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
            print("Processing Excel Files")
            file_obj = s3_client.get_object(Bucket = source_config_bucket, Key=record['s3']['object']['key')
            content = file_obj["Body"].read()
            read_excel_data = io.BytesIO(content)
            df = pd.read_excel(read_excel_data, sheet_name = config['columnToExtract'])
            print(df)

arn:aws:lambda:us-east-1:005484526251:layer:oiepartnerpilot-openpyxl:4

if source_key.endswith(".xlsx"):
            print ("Processing Excel Files")
            s3_client.download_file(source_config_bucket, record['s3']['object']['key'], '/tmp/wb.xlsx')
            wb = openpyxl.load_workbook('/tmp/wb.xlsx')
            print("Sheet Names are", wb.sheetnames)
            masterAgentList = wb.get_sheet_names()[1]
            worksheet = wb.get_sheet_by_name(masterAgentList)
            print(worksheet)

            openpyxl to open/read
            pd to save csv upload