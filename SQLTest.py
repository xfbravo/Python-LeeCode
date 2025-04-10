import mysql.connector
# Connect to the database
try:
    db= mysql.connector.connect(
        host='localhost',
        port=3306,user="root",
        password="Dengni0425@xf",
        database="db"
    )
    cursor=db.cursor()
    print("Connection successful")
    # cursor.execute("CREATE VIEW Sage_22 AS SELECT sno,sname,sage FROM student WHERE sage<22 WITH CHECK OPTION")
    # cursor.execute("INSERT INTO Student(sno, sname, sage, ssex, sdept) VALUES ('95005', '老八', 29, '男', '临床医学')")
    # cursor.execute("INSERT INTO course(cno,cname,Ccredit) VALUES ('1', '数据结构', 3)")
    # cursor.execute("INSERT INTO course(cno,cname,Ccredit) VALUES ('2', '微积分', 6)")
    # cursor.execute("INSERT INTO course(cno,cname,Ccredit) VALUES ('3', '离散数学', 4)")
    # cursor.execute("INSERT INTO course(cno,cname,Ccredit) VALUES ('4', '大学物理', 4)")
    # cursor.execute("INSERT INTO course(cno,cname,Ccredit) VALUES ('5', '数值分析', 2)")
    # cursor.execute("UPDATE sc SET cno='5' WHERE sno='95006' AND cno='6'")
    # cursor.execute("INSERT INTO sc(sno,cno,grade) VALUES ('95003','4','88')")
    # cursor.execute("INSERT INTO sc(sno,cno,grade) VALUES ('95003','2','98')")
    # cursor.execute("INSERT INTO sc(sno,cno,grade) VALUES ('95004','3','48')")
    # cursor.execute("INSERT INTO sc(sno,cno,grade) VALUES ('95004','5','78')")
    # cursor.execute("INSERT INTO sc(sno,cno,grade) VALUES ('95005','1','89')")
    # cursor.execute("INSERT INTO sc(sno,cno,grade) VALUES ('95005','2','99')")
    # cursor.execute("INSERT INTO sc(sno,cno,grade) VALUES ('95005','3','93')")
    # cursor.execute("INSERT INTO sc(sno,cno,grade) VALUES ('95006','1','87')")
    # cursor.execute("SELECT sc.sno,Grade FROM sc,student \
    #                 WHERE sc.sno=student.sno AND sc.grade>='90' AND student.Sdept IN ('计算机科学与技术','自动化控制','网络安全')\
    #                 ORDER BY sc.sno"
    # )
    # result = cursor.fetchall()
    # for row in result:
    #     print(row)
    cursor.execute("SELECT student.sno,student.sname,student.sage,student.ssex,student.sdept,AVG(Grade)\
                    FROM student,sc\
                    WHERE student.sno=sc.sno \
                    GROUP BY student.sno\
                    HAVING AVG(sc.grade)>=90"
    )
    result = cursor.fetchall()
    for row in result:
        print(row)
    db.commit()
    cursor.close()
    db.close()
except mysql.connector.Error as error:
    print("Connection failed: {}".format(error))
# cursor.execute("INSERT INTO sc (sno,cno,grade) VALUES ('95006','6','100')")
# cursor.execute("select * from sc where grade>='90' ")
# Fetch all rows from the result set
# rows = cursor.fetchall()
# Print each row
# for row in rows:
#     print(row)
# cursor.execute("INSERT INTO student(sno, sname, sage, ssex, sdept) VALUES ('95006', '老六', 20, '男', '考古')")
# Close the cursor and connection
