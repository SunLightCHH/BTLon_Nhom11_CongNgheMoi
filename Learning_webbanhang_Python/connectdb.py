import mysql.connector
db=mysql.connector.connect(user='root', password = '', host='localhost', database='test1')
#Query
code = "CREATE DATABASE `TEST1`"
#Create table
code1="CREATE TABLE `test1`.`info` (`ID` INT NOT NULL, `Name` VARCHAR(45) NOT NULL, `Year` INT NULL, PRIMARY KEY (`ID`))"
#Add content
code2 = "INSERT INTO `info` (`ID`, `Name`, `Year`) VALUES ('01', 'Anh', '2002');"
code4 = "INSERT INTO `info` (`ID`, `Name`, `Year`) VALUES (%s, %s, %s);"
val=[
    ('2', 'Tuan', '1999'),
    ('3', 'Nam', '2000')
]
#Remove content
code3 = "DELETE FROM `info` WHERE id = '01'"
#RUN
mycursor = db.cursor()
mycursor.execute(code2)
for items in val:
    mycursor.execute(code4, items)
#update db
db.commit()