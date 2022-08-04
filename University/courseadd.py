

from pydoc import describe
from unicodedata import name
from django.forms import SelectDateWidget

from django.db import connections
class CourseAdd:
    def __init__(self,course_id='',name='',description='',student_id=''):
        self.course_id=course_id
        self.name=name
        self.description=description
        self.student_id = str(student_id)
    def addCourse(self):
        #print(f"Course Name: {self.name}, Course ID: {self.id}, Description: {self.description}")
        
        #database connection to the app
        db_cursor=connections['default'].cursor()
        
        #Sql Query for course add
        db_cursor.execute("INSERT INTO University_courseregistrations (course_ID,course_Name,course_Description,owner_id) VALUES('"+self.course_id+"','"+self.name+"','"+self.description+"','"+self.student_id+"')")
    
    def deleteCourse(self):
        #database connection to the app
        db_cursor=connections['default'].cursor()
        
        #Sql Query for course add
        db_cursor.execute("DELETE FROM University_courseregistrations WHERE (course_ID='"+self.course_id+"' AND WHERE owner_id='"+self.student_id+"')")
        
        
    

