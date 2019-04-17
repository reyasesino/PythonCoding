import boto3
import re
from datetime import datetime

s3 = boto3.client('s3')

def main():
    # Getting the list of the buckets
    response = s3.list_objects(
        Bucket='sqlbackupdb'
    )
    datetobesearched = ""
    #converttoobhectdatetime = datetime.strptime(datetobesearched, '<provided format>')

    count = 0
    regexp = re.compile("^myfile_(.*)\d{0,9}.ext")

    for ele in response['Contents']:
        print(ele['Key'])

    for ele in response['Contents']:
        print(ele['Key'])
        m = regexp.search(ele['Key']).group(1)
        print(m)
    #     datetime_from_key = datetime.strptime(m, '%d%b%y')
    #     if(converttoobhectdatetime == datetime_from_key):
    #         print("The database backup exists")
    #         count = count + 1
    #     else:
    #         pass
    #
    # if(count > 0 ):
    #     print("The db backup exits")
    # else:
    #     print("Sending information to sns topic that db bacup does not exists for the date :: " , converttoobhectdatetime)


if __name__ == '__main__':
    main()