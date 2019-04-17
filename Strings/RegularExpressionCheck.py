import re
from datetime import datetime

def main(test):
    regexp = re.compile("^CEPC_db_backup(.*)-\d{0,9}.sql.gz")
    m = regexp.search(test).group(1)
    print(m)
    datetime_object = datetime.strptime(m, '%d%b%y')
    print(datetime_object)




if __name__ == '__main__':
    text = 'CEPC_db_backup05Apr19-042138.sql.gz'
    main(text)