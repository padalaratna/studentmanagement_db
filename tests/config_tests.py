import sqlite3
import unittest
from unittest.mock import patch

from studentmanagement import app

class TestConfig(unittest.TestCase):
    def setUp(self):
        self.connection = sqlite3.connect(":memory:")
        cursor = self.connection.cursor()
        create_table = 'CREATE TABLE STUDENT_TAB ( ID INT ,NAME VARCHAR(255),AGE INT,GRADE INT,SUBJECTS VARCHAR(255),PRIMARY KEY(ID))'
        insert_student_query = 'INSERT INTO STUDENT_TAB (ID,NAME,AGE,GRADE,SUBJECTS) VALUES (1,"RATNA",34,12,"MATHS")' 
        cursor.execute(create_table)      
        cursor.execute(insert_student_query)
        self.connection.commit()        
        self.db_connection_patch = patch("studentmanagement.db_connection", return_value=self.connection)
        self.db_connection_patch.start()
        
        self.app = app.test_client()

    def tearDown(self):
        self.connection.close()