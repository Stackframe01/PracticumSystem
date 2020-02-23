import mysql.connector


def add_key_skills(professional_standard, work_function, data):
    database = mysql.connector.connect(host='localhost', user='root', passwd='mysqlrootuser', database='standards')
    cursor = database.cursor()
    for i in data:
        cursor.execute(
            'INSERT INTO key_skills (professional_standard, work_function, key_skill) VALUES ("{}", "{}", "{}")'.format(
                professional_standard, work_function, ', '.join(i)))
    database.commit()


def add_requirements(professional_standard, work_function, data):
    database = mysql.connector.connect(host='localhost', user='root', passwd='mysqlrootuser', database='standards')
    cursor = database.cursor()
    for i in data:
        cursor.execute('INSERT INTO requirements (professional_standard, work_function, requirement) VALUES ("{}", '
                       '"{}", "{}")'.format(professional_standard, work_function,', '.join(i)))
    database.commit()


def add_professional_standards(professional_standard, work_function, data):
    database = mysql.connector.connect(host='localhost', user='root', passwd='mysqlrootuser', database='standards')
    cursor = database.cursor()
    for i in data:
        cursor.execute(
            'INSERT INTO professional_standards (professional_standard, work_function, required_skill) VALUES ("{}", '
            '"{}", "{}")'.format(
                professional_standard, work_function, i))
    database.commit()


if __name__ == '__main__':
    pass
