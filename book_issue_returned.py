def IssueBook():
 BCODE=input("BCODE:")
 SQL="SELECT * FROM BOOKS WHERE BCODE="+BCODE+""
 N=MyCur.execute(SQL)
 if N>0:
   SCODE=input("CODE OF ISSUE STUDENT:")
   STATUS="ISSUED"
    DATEOFISSUE=input("DATE OF ISSUE[YYYY-MM-DD]:")
   DATEDUE=input("DUE DATE [YYYY-MM-DD]")
   SQL="UPDATE BOOKS SET Qty=Qty+"+Qty\
   +",STATUS='"+STATUS\
   +"',DATEOFISSUE=”+DATEOFISSUE+”,DATEDUE=”+DATEDUE+”\
    WHERE BCODE="+BCODE+""
   MyCur.execute(SQL)
   db.commit()

def studentnumbers():
  print(“number of students”)
  x=cursor.rowcount()
  print(x)

def returned():
 BCODE=input("BCODE:")
 SCODE=input(“SCODE:”)
 SQL="SELECT * FROM BOOKS WHERE BCODE="+BCODE+"" AND SCODE=”+SCODE””
 N=MyCur.execute(SQL)
 if N>0:
   SCODE=0
   STATUS="Available"
    DATEOFISSUE=None
   DATEDUE=None
   SQL="UPDATE BOOKS SET Qty=Qty+"+Qty\
   +",STATUS='"+STATUS\
   +"',DATEOFISSUE=”+DATEOFISSUE+”,DATEDUE=”+DATEDUE+”\
    WHERE BCODE="+BCODE+""
   MyCur.execute(SQL)
   db.commit()
