import boto3
client = boto3.client('athena')

def main():
    queryStart = client.start_query_execution(
        QueryString = 'select count(*) as Count from data where temperature is not null and pressure is not null',
        #QueryString = 'select *  from data where temperature >=20 and temperature <=50',
        #QueryString = 'select  COUNT(*) as ValidTemp  from data where temperature >=20 and temperature <=25',
        #QueryString = 'select count(*) as Count from data where temperature is not null and pressure is not null',
        QueryExecutionContext = {
            'Database': 'sampledb'
        },
        ResultConfiguration={
        'OutputLocation': 's3://sachin-iot-creator/test-tester-rblwh/results',
        'EncryptionConfiguration': {
            'EncryptionOption': 'SSE_S3'
        }
      }
    )

    print(queryStart['QueryExecutionId'])
    queryExecution = client.get_query_results(QueryExecutionId=queryStart['QueryExecutionId'])

    #queryExecution = client.get_query_results(QueryExecutionId=queryStart['QueryExecutionId'])
    #print(queryExecution)


if __name__ == '__main__':
    main()
