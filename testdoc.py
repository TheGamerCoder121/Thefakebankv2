#imports
import pymysql
import pymysql.cursors
import pickle
import time

# Fail to create table #1
# try:
#    # Create a cursor object
#    cursorObject = connectionObject.cursor()                                  
#    # SQL query string
#    sqlQuery            = "CREATE TABLE Employee(id int, LastName varchar(32), FirstName varchar(32), DepartmentCode int)"   
#    # Execute the sqlQuery
#    cursorObject.execute(sqlQuery)
#    # SQL query string
#    sqlQuery            = "show tables"   
#    # Execute the sqlQuery
#    cursorObject.execute(sqlQuery)
#    #Fetch all the rows
#    rows                = cursorObject.fetchall()
#    for row in rows:
#        print(row)
# except Exception as e:
#    print("Exeception occured:{}".format(e))
# finally:
#    connectionObject.close() 

# #final code for databace:
hmmmm = pickle.load( open( "randomtextdoc.txt", "rb" ) )
connection = pymysql.connect('thefakebank.cvauivbqyvrn.us-east-1.rds.amazonaws.com','admin',hmmmm,'Fakebank',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
print("Hello, you are connected to the databace " + str(connection))
# create user and print username
try:
   Theusername = input("What is the admin username: ")
   Thepassword = input("What is the admin password: ")
   with connection.cursor() as cursor:
        # Create a new record
       sql = "INSERT INTO `Users` (`username`, `password`) VALUES (%s, %s)"
       cursor.execute(sql, (Theusername, Thepassword))

    # connection is not autocommit by default. So you must commit to save your changes.
   connection.commit()

   with connection.cursor() as cursor:
      #Read a single record
      sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
      cursor.execute(sql, (Theusername,))
      result = cursor.fetchone()
      print(result)
      time.sleep(4)
finally:
   connection.close()
