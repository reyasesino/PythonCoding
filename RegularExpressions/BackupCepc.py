import boto3
import time
import re
from datetime import datetime

client = boto3.client('s3')
sns = boto3.client('sns')
import json


def main():

    # print(response)
    # searcheddate = '2019-04-15'
    # searchddateformat = datetime.strptime(searcheddate, "%Y-%M-%d")
    strfind = 'CEPC_db_backup01Apr19-235501.sql'
    # CEPC_db_backup_2019-04-15.sql.gz
    expression = re.search('^CEPC_db_backup_(.*?).sql.gz', strfind)
    print(expression)



    # return "Competed"
if __name__ == "__main__":
    main()