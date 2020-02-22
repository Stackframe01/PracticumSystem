import mysql.connector


def initialize_database():
    database = mysql.connector.connect(host='localhost', user='root', passwd='mysqlrootuser')
    cursor = database.cursor()

    try:
        cursor.execute('CREATE DATABASE standards')
    except mysql.connector.errors.DatabaseError:
        pass

    database = mysql.connector.connect(host='localhost', user='root', passwd='mysqlrootuser', database='standards')
    cursor = database.cursor()

    try:
        cursor.execute('CREATE TABLE key_skills (work_function TEXT, key_skill TEXT)')
    except mysql.connector.errors.ProgrammingError:
        cursor.execute('DELETE FROM key_skills')
    try:
        cursor.execute('CREATE TABLE requirements (work_function TEXT, requirement TEXT)')
    except mysql.connector.errors.ProgrammingError:
        cursor.execute('DELETE FROM requirements')
    try:
        cursor.execute('CREATE TABLE professional_standards (work_function TEXT, professional_standard TEXT)')
    except mysql.connector.errors.ProgrammingError:
        cursor.execute('DELETE FROM professional_standards')
    try:
        cursor.execute('CREATE TABLE vocabularies (vocabulary TEXT, value TEXT)')
    except mysql.connector.errors.ProgrammingError:
        cursor.execute('DELETE FROM professional_standards')

    with open('data/vocabularies/description_regex_start.csv') as f:
        for line in set(f.readlines()):
            cursor.execute(
                'INSERT INTO vocabularies (vocabulary, value) VALUES ("description_regex_start", "{}")'.format(line))
    with open('data/vocabularies/description_regex_end.csv') as f:
        for line in set(f.readlines()):
            cursor.execute(
                'INSERT INTO vocabularies (vocabulary, value) VALUES ("description_regex_end", "{}")'.format(line))
    with open('data/vocabularies/stopwords_english.csv') as f:
        for line in set(f.readlines()):
            cursor.execute(
                'INSERT INTO vocabularies (vocabulary, value) VALUES ("stopwords_english", "{}")'.format(line))
    with open('data/vocabularies/stopwords_russian.csv') as f:
        for line in set(f.readlines()):
            cursor.execute(
                'INSERT INTO vocabularies (vocabulary, value) VALUES ("stopwords_russian", "{}")'.format(line))

    database.commit()


if __name__ == '__main__':
    pass
