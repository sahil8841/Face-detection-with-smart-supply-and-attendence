import mysql.connector

mydb = mysql.connector.connect(
       host= "192.168.1.105",
       user="project",
       password="madangle7788",
     database="source"

)
a = mydb.cursor()
#a.execute("CREATE DATABASE source")
#a.execute("CREATE TABLE Attendance (Date VARCHAR(30),Student_NAME VARCHAR(255),DateTime VARCHAR(255),Roll_No VARCHAR(255), PRIMARY KEY (Date,Student_NAME))")
#sql = "DROP DATABASE source"
#a.execute(sql)
mydb.commit()
mydb.close()
