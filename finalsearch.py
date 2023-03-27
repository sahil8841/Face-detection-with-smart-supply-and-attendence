import mysql.connector





def mysqlsearch(name):
       mydb = mysql.connector.connect(
       host= "192.168.1.105",
       user="project",
       password="madangle7788",
       database="source"

)

       a = mydb.cursor()
       sql1=a.execute("SELECT * from Attendance WHERE Student_NAME = %(name)s", {'name': name})

       a.execute(sql1)
       checkUsername = a.fetchall()
       print(*checkUsername, sep = "\n")

       mydb.commit()
       mydb.close()

name=input("Enter Student_Name:-")
mysqlsearch(name)
        
         
         
         
         
        
