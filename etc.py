class Student:
  student_id = 0
  name = str 
  year = 0
  gpa = 0.0
  enrolled = False

wednesday = Student()
wednesday.student_id = 14323
wednesday.name = 'Wednesday'
wednesday.year = 1923
wednesday.gpa = 3.2
wednesday.enrolled = True
print(vars(wednesday))