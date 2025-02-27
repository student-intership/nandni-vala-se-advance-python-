import pymysql

mydb = pymysql.connect(host='localhost',user='root',password='')
mycursor = mydb.cursor()

mycursor.execute("create database if not exists Table1")
mydb.commit()

mydb = pymysql.connect(host='localhost',user='root',password='',database='Table1')
mycursor = mydb.cursor()

mycursor.execute("create table if not exists table1(id int primary key auto_increment,name varchar(40),salary varchar(10) unique key)")
mydb.commit()