def AddBook():
  def NotNull(x):
    if type(x)==None:
        x=input(‘re-enter %g’)%x

  BCODE=input("bcode :")
  NotNull(BCODE)
  BNAME=input("BNAME :")
  NotNull(BNAME)
  BAUTH=input("AUTHOR :")
     NotNull(BAUTH)
  SCODE=input("SCODE:")
  STATUS=input("Status")
    DATEOFISSUE=input("DATE OF ISSUE[YYYY-MM-DD]:")
  DATEDUE=input("DUE DATE [YYYY-MM-DD]")
  SNAME=input("SNAME :")  
  SQL="INSERT INTO STUDENT VALUES ("\
  +SCODE+",'"+SNAME+"',"+\
  BCODE+")
  cursor.execute(SQL)
  db.commit()
  SQL="INSERT INTO BOOKS VALUES ("\
  +BCODE+",'"+BNAME+"',"+BAUTH+","+\
  SCODE+",'"+STATUS+"',”+DATEOFISSUE+”,”+DATEDUE+”)"
  cursor.execute(SQL)
  db.commit()
