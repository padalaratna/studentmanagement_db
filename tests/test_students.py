from config_tests import TestConfig

# Unit test cases for studentmanagement.
class TestStudentsView(TestConfig):
    # Unit test for fetching all students.
    def test_students_route(self):
        response = self.app.get("/list")      
        self.assertEqual(response.status_code, 200)
        self.assertIn("<td>RATNA</td>",response.data.decode("utf-8"))

    # Unit test for add student with get method.
    def test_add_student_get_route(self):
        response = self.app.get("/add")
        self.assertEqual(response.status_code, 200)
        self.assertIn('<input type="text" name="age" />',response.data.decode("utf-8"))

    # Unit test for add student with post method.    
    def test_add_student_post_route(self):
        response = self.app.post("/add", data={
            "name": "Göran",
            "age": 12,
            "grade": 1,
            "subjects":"english"
        })
        self.assertEqual(response.status_code, 200)    
        self.assertIn('<i style="color: brown;">Student is successfully created with NAME :Göran</i>',response.data.decode("utf-8"))

    # Unit test for edit student with get method.
    def test_edit_student_get_route(self):
        response = self.app.get("/edit/1")
        self.assertEqual(response.status_code, 200)
        #print(response.data.decode("utf-8"))
        self.assertIn('<input type="text" name="name"  value="RATNA"/>',response.data.decode("utf-8"))

    # Unit test for edit student with post method.
    def test_update_student_post_route(self):
       response = self.app.post("/update", data={
            "id" : 1,
            "name": "Göran",
            "age": 12,
            "grade": 1,
            "subjects":"english"
        })
       self.assertEqual(response.status_code, 200)       
       self.assertIn('<h3><i style="color: brown;">Student with name Göran successfully updated</i></h3>',response.data.decode("utf-8"))

    # Unit test for delete student.
    def test_delete_student_get_route(self):
        response = self.app.get("/delete/1")
        self.assertEqual(response.status_code, 200)       
        self.assertIn('<h3><i style="color: brown;">Student with id 1 successfully deleted </i></h3>',response.data.decode("utf-8"))
 
   
   