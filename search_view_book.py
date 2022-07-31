def View():
  ask=input(‘which table do you want to see?’).upper()
  while ask not in [‘STUDENT’,’BOOKS’]:
   print(‘no such table’)
   ask=input(‘which table do you want to see?’).upper()
  SQL="SELECT * FROM %s" %ask
  MyCur.execute(SQL)
  R=MyCur.fetchall()
  if ask==’STUDENT’:
    for SCODE, SNAME, BCODE in R:
       print("%4d | %20s | %5d | "%\
            (SCODE,SNAME.ljust(20,"_"),BCODE))
  else:
    for BCODE, BNAME, BAUTH, SCODE, STATUS,DATEOFISSUE, DATEDUE in R:
       print("%4d | %20s | %5d | %8.2f | %12s | %2s| %4s |"%\
            (BCODE, BNAME.ljust(20,"_"),BAUTH,SCODE,STATUS,
                           DATEOFISSUE,DATEDUE))
  

def SearchBook():
  Bookno=input("Book code")
  SQL="SELECT * FROM STUDENT WHERE BCODE="+BCODE+""
  N=MyCur.execute(SQL)
  if N>0:
  R=MyCur.fetchone()
  print("Found...")
  print("BCODE :",R[0])
  print("BNAME :",R[1])
  print("AUTHOR :",R[2])
  print("SCODE :",R[3])
  print(‘STATUS’ R[4])
  if R[4]=’Issued’:
     print(‘Book Issued’)
