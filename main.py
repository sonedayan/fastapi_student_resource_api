from fastapi import FastAPI
from uuid import UUID

# Creating a FastAPI instance
app = FastAPI()

# dictionary for storing
students = {}

student_data = {
    "id": 0,
    "name": "",
    "age": "",
    "age": "",
    "sex": "", 
    "height": "",
}

# Get a list of students
@app.get("/")
def get_students():
    ''' Returns all the students  '''
    return students

# Add a new student
@app.post("/students")
def add_student(name: str, age: int, sex: str, height: float):
    new_student = student_data.copy()
    new_student["id"] = str(UUID(int=len(students) + 1))
    new_student["name"] = name
    new_student["age"] = age
    new_student["sex"] = sex
    new_student["height"] = height

    students[new_student["id"]] = new_student

    return {"message": "Student added successfully", "data": new_student}

# Get a specific student
@app.get("/students/{id}")  # GET method to get a resource
def get_student_by_id(id: int):
    student = students.get(id)
    if not student:
        return {"error": "Student not found"}

    return student