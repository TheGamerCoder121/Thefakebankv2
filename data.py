import pymysql
import pymysql.cursors
import pickle
from sys import exit
import time
import warnings

hmmmm = pickle.load( open( "randomtextdoc.txt", "rb" ) )
connection = pymysql.connect('thefakebank.cvauivbqyvrn.us-east-1.rds.amazonaws.com','admin',hmmmm,'Fakebank',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
print("Hello, you are connected to the databace " + str(connection))
print("""
NOTE: Please EXIT or S_OUT before you go
""")
while True: 
    login = False
    pickle.dump( login, open( "login.txt", "wb"))
    print("login is " + str(login))
    print(" Welcome to the fake bank(ALPHA)")
    print(" 'Help' for help")
    start = input("What would you like to do? ")
    if(start == "Help"):
        import helpcmd.py
    if (start=="CMD"):
        import cmds.py
    if (start == "EXIT" or "S_OUT"):
        login = False
        pickle.dump( login, open( "login.txt", "wb" ) )
        exit(0)
        #fix this:
    if (start == "S-IN"):
      print("")
  
    if (start == "S_NEW"): 
        print("One moment please..")
        time.sleep(3)
        newusername = input("Username:" )
        newuserpass = input("Password: ")
        connection = pymysql.connect('thefakebank.cvauivbqyvrn.us-east-1.rds.amazonaws.com','admin',hmmmm,'Fakebank',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
        print("Hello, you are connected to the databace " + str(connection))
        try:
          with connection.cursor() as cursor:
                # Create a new record
              sql = "INSERT INTO `Users` (`username`, `password`) VALUES (%s, %s)"
              cursor.execute(sql, (newusername, newuserpass))

            # connection is not autocommit by default. So you must commit to save your changes.
          connection.commit()

          with connection.cursor() as cursor:
              #Read a single record
              sql = "SELECT `id`, `password` FROM `users` WHERE `username`=%s"
              cursor.execute(sql, (newusername,))
              result = cursor.fetchone()
              print(result)
              time.sleep(4)
        finally:
          connection.close()