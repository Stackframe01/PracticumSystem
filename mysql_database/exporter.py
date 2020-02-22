import mysql.connector


def add_key_skills(work_function, data):
    database = mysql.connector.connect(host='localhost', user='root', passwd='mysqlrootuser', database='standards')
    cursor = database.cursor()
    for i in data:
        cursor.execute(
            'INSERT INTO key_skills (work_function, key_skill) VALUES ("{}", "{}")'.format(work_function, ', '.join(i)))
    database.commit()


def add_requirements(work_function, data):
    database = mysql.connector.connect(host='localhost', user='root', passwd='mysqlrootuser', database='standards')
    cursor = database.cursor()
    for i in data:
        cursor.execute(
            'INSERT INTO requirements (work_function, requirement) VALUES ("{}", "{}")'.format(work_function,
                                                                                               ', '.join(i)))
    database.commit()


def add_professional_standards(work_function, data):
    database = mysql.connector.connect(host='localhost', user='root', passwd='mysqlrootuser', database='standards')
    cursor = database.cursor()
    for i in data:
        cursor.execute(
            'INSERT INTO professional_standards (work_function, professional_standard) VALUES ("{}", "{}")'.format(
                work_function, i))
    database.commit()


if __name__ == '__main__':
    pass
