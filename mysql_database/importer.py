import mysql.connector


def get_description_regex_start():
    database = mysql.connector.connect(host='localhost', user='root', passwd='mysqlrootuser', database='standards')
    cursor = database.cursor()
    cursor.execute('SELECT value FROM vocabularies WHERE vocabulary = "description_regex_start"')
    return [i[0].replace('\n', '') for i in cursor.fetchall()]


def get_description_regex_end():
    database = mysql.connector.connect(host='localhost', user='root', passwd='mysqlrootuser', database='standards')
    cursor = database.cursor()
    cursor.execute('SELECT value FROM vocabularies WHERE vocabulary = "description_regex_end"')
    return [i[0].replace('\n', '') for i in cursor.fetchall()]


def get_stopwords_english():
    database = mysql.connector.connect(host='localhost', user='root', passwd='mysqlrootuser', database='standards')
    cursor = database.cursor()
    cursor.execute('SELECT value FROM vocabularies WHERE vocabulary = "stopwords_english"')
    return [i[0].replace('\n', '') for i in cursor.fetchall()]


def get_stopwords_russian():
    database = mysql.connector.connect(host='localhost', user='root', passwd='mysqlrootuser', database='standards')
    cursor = database.cursor()
    cursor.execute('SELECT value FROM vocabularies WHERE vocabulary = "stopwords_russian"')
    return [i[0].replace('\n', '') for i in cursor.fetchall()]


if __name__ == '__main__':
    pass
