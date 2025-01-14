from flask import Flask,render_template,request,redirect,url_for 
import sqlite3
from contextlib import contextmanager

app = Flask(__name__)
list_students = [];
cursor = None;
database = 'student.db';
select_student_query = 'SELECT * FROM STUDENT_TAB'

@contextmanager
def db_connection():
    connection = sqlite3.connect(database)
    try:
        yield connection
    finally:
        connection.close()

# Function to load all the students from STUDENT_TAB table.
def load_students_from_database():
  return fetch_all_students();

# Function to generate next ID of STUDENT_TAB table.
def generate_student_id():
   select_student_query = 'SELECT MAX(ID) FROM STUDENT_TAB'
   try:
    with  db_connection() as conn:
        cursor = conn.cursor()       
        cursor.execute(select_student_query)        
        max_id = cursor.fetchone()     
        if max_id[0] == None:
          next_id = 1
        else:      
          next_id = max_id[0] + 1;
        return  next_id
   except sqlite3.OperationalError as e:
    print(e)
    
# Function to fetch all the students from STUDENT_TAB table.    
def fetch_all_students():
   select_student_query = 'SELECT * FROM STUDENT_TAB'
   try:
    with  db_connection() as conn:
        cursor = conn.cursor()       
        cursor.execute(select_student_query)        
        return cursor.fetchall() 
   except sqlite3.OperationalError as e:
    print(e)

# Function to fetch a student by ID from STUDENT_TAB table.    
def fetch_student(id):
   select_student_query = f'SELECT * FROM STUDENT_TAB WHERE ID = {id}'
   try:
    with  db_connection() as conn:
        cursor = conn.cursor()       
        cursor.execute(select_student_query)        
        return cursor.fetchone() 
   except sqlite3.OperationalError as e:
    print(e)


# Function to add a new student in STUDENT_TAB table.  
def add_student(name,age,grade,subjects):   
    # Create a student in student database  
    id = generate_student_id()    
    try:
      with  db_connection() as conn:
        cursor = conn.cursor()
        insert_student_query = f'INSERT INTO STUDENT_TAB (ID,NAME,AGE,GRADE,SUBJECTS) VALUES ({id},"{name}",{age},{grade},"{subjects}")'     
        cursor.execute(insert_student_query)       
        conn.commit()        
    except sqlite3.OperationalError as e:
       print(e)
       
# Function to delete an existing student from STUDENT_TAB table.  
def delete_student(student_id):   
   try:
      with  db_connection() as conn:
        cursor = conn.cursor()
        delete_student_query = f'DELETE FROM STUDENT_TAB WHERE ID = {student_id}'       
        cursor.execute(delete_student_query)       
        conn.commit()        
   except sqlite3.OperationalError as e:
       print(e)

# Function to edit an existing student in STUDENT_TAB table.          
def edit_student(student_id,name,age,grade,subjects):   
    try:
      with  db_connection() as conn:
        cursor = conn.cursor()
        update_student_query = f'UPDATE STUDENT_TAB SET NAME = "{name}", AGE = {age} , GRADE = {grade} ,  SUBJECTS = "{subjects}"  WHERE ID = {student_id}'        
        cursor.execute(update_student_query)       
        conn.commit()         
    except sqlite3.OperationalError as e:
       print(e)



@app.route("/")
def home():
    list_students = fetch_all_students()
    return render_template("home.html",students=list_students)

@app.route("/list" )
def viewAll():
    list_students = fetch_all_students()
    return render_template("viewAllStudents.html",students=list_students)

@app.route("/add" , methods = ['POST', 'GET'])
def addStudent():
 if request.method == 'POST':        
            name = request.form['name']
            age = request.form['age']
            grade = request.form['grade']
            subjects = request.form['subjects']
            add_student(name,age,grade,subjects);
            msg = "Student is successfully created with NAME :" + name;
            return render_template("result.html",content=msg)   
 else:
    return render_template("addStudent.html")

@app.route("/edit/<id>")
def editStudent(id):
     student = fetch_student(id)     
     return render_template("editStudent.html",content = student)
    
          
@app.route("/update" , methods = ['POST'])
def updateStudent():   
    if request.method == 'POST':     
        id = request.form['id']
        name = request.form['name']
        age = request.form['age']
        grade = request.form['grade']
        subjects = request.form['subjects']
        edit_student( id, name, age, grade, subjects)
        msg = f"Student with name {name} successfully updated";
        return render_template("result.html",content=msg) 
    else:
        return redirect(url_for("home"))   

       
@app.route("/delete/<id>")
def deleteStudent(id):      
    delete_student(id);
    msg = "Student with id " + str(id) + " successfully deleted ";
    return render_template("result.html",content=msg) 

 
if __name__ == "__main__":   
    list_students = load_students_from_database()
    app.run()
