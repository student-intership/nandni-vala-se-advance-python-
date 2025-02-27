import pymysql

mydb = pymysql.connect(host="localhost",user="root",password="")
mycursor = mydb.cursor()

mycursor.execute("create database if not exists student01")
mydb.commit()

mydb = pymysql.connect(host="localhost",user="root",password="",database="student01")
mycursor = mydb.cursor()

mycursor.execute("create table if not exists Student(id int primary key auto_increment,name varchar(60),subject varchar(50),mobile_no varchar(10) unique key)")
mydb.commit()

