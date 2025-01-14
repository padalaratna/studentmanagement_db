import sqlite3
# Setting up the sql database with name student.db, create a table STUDENT_TAB.
database = 'student.db'
max_student_query = 'SELECT MAX(ID) FROM STUDENT_TAB'
create_table = 'CREATE TABLE STUDENT_TAB ( ID INT ,NAME VARCHAR(255),AGE INT,GRADE INT,SUBJECTS VARCHAR(255),PRIMARY KEY(ID))'
insert_student_query = 'INSERT INTO STUDENT_TAB (ID,NAME,AGE,GRADE,SUBJECTS) VALUES (1,"RATNA",34,12,"MATHS")' 
select_student_query = 'SELECT * FROM STUDENT_TAB'
update_student_query = 'UPDATE STUDENT_TAB SET NAME = "lucky", AGE = 10 WHERE ID = 1'
delete_student_query = 'DELETE FROM STUDENT_TAB WHERE ID = 1'
try:
    with sqlite3.connect(database) as conn:
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS STUDENT_TAB")
        cursor.execute(create_table) 
        print("Table People is Ready!") 

except sqlite3.OperationalError as e:
    print(e)