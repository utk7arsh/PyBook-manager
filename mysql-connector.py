import MySQLdb #import the module, case sensitive
db=MySQLdb.connect(host=’localhost’, user=’Root’, password=”sql“, port=3306) #login to your database
cursor=db.cursor() #creates a command prompt variable ‘cursor’
try:
   cursor.execute(‘CREATE DATABASE LIBRARY’)
   print(‘Created library successfully’)
except:
   print(‘The database exists’)

cursor.execute(‘USE LIBRARY’)

try: 
  cursor.execute(‘CREATE TABLE STUDENT(SCODE INT NOT NULL, SNAME\
  VARCHAR(25) NOT NULL, BCODE INT(3) NOT NULL’))
  print(‘created table, add items now’)

except:
  print(‘table exists’)

try:
  cursor.execute(‘CREATE TABLE BOOKS(BCODE INT NOT NULL, BNAME\
  VARCHAR(25) NOT NULL, BAUTH VARCHAR(25), SCODE INT NOT NULL,STATUS\
  VARCHAR(25) DATEOFISSUE DATE,\
  DATEDUE DATE’))
  print(‘created table, add items now’)

except:
  print(‘table exists’)


print("Book Management System 1.0")
while True:
 CH=input("A:Add Item V:View S:Search I:Issue R:Return Q:Quit")
 if CH=='A':
  AddBook()
 elif CH=="S":
  SearchBook()
 elif CH=="V":
  View()
 elif CH=="I":
  IssueBook()
 elif CH=='R':
  returned()
 else:
  break
studentnumbers()
db.close()

