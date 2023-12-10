# Install Mysql on your computer
# https://dev.mysql.com/downloads/installer/
# pip install my sql
# pip install mysql-connector 
# pip install mysql-connector-python

import mysql.connector 

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root2',
	passwd = '12345678'
	)

#prepare a curosr object 
cursorObject = dataBase.cursor()

#Create a database 
cursorObject.execute('CREATE DATABASE elderco')

print("All Done!")