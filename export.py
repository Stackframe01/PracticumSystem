import mysql.connector

def delete_database():
    mydb = mysql.connector.connect(host='localhost', user='root', passwd='mysqlrootuser')
    mycursor = mydb.cursor()
    mycursor.execute('DROP DATABASE standarts')

def create_database():
    mydb = mysql.connector.connect(host='localhost', user='root', passwd='mysqlrootuser')
    mycursor = mydb.cursor()
    mycursor.execute('CREATE DATABASE standarts')
    mydb = mysql.connector.connect(host='localhost', user='root', passwd='mysqlrootuser', database='standarts')
    mycursor = mydb.cursor()
    mycursor.execute('CREATE TABLE labor_market_skills (skill VARCHAR(255))')
    mycursor.execute('CREATE TABLE professional_standarts (skill VARCHAR(255))')

def labor_market_skills_to_mysql(dataset):
    mydb = mysql.connector.connect(host='localhost', user='root', passwd='mysqlrootuser', database='standarts')
    mycursor = mydb.cursor()
    for el in dataset:
        print(el)
        mycursor.execute("INSERT INTO labor_market_skills (skill) VALUES ({})".format('"' + el + '"'))
        mydb.commit()

def professional_standarts_to_mysql(dataset):
    mydb = mysql.connector.connect(host='localhost', user='root', passwd='mysqlrootuser', database='standarts')
    mycursor = mydb.cursor()
    for el in dataset:
        mycursor.execute("INSERT INTO professional_standarts (skill) VALUES ({})".format('"' + el + '"'))
        mydb.commit()

if __name__ == "__main__":
    pass