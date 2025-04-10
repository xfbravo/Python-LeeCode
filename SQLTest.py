import mysql.connector
# Connect to the database
db= mysql.connector.connect(host='localhost',port=3306,user="root",password="Dengni0425@xf",database="db")
cursor=db.cursor()
if cursor:
    print("Connection successful")
# cursor.execute("INSERT INTO sc (sno,cno,grade) VALUES ('95006','6','100')")
# cursor.execute("select * from sc where grade>='90' ")
# Fetch all rows from the result set
# rows = cursor.fetchall()
# Print each row
# for row in rows:
#     print(row)
cursor.execute("INSERT INTO student(sno, sname, sage, ssex, sdept) VALUES ('95006', '老六', 20, '男', '考古')")
db.commit()
# Close the cursor and connection
cursor.close()
db.close()