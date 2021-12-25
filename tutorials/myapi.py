from fastapi import FastAPI
from fastapi.param_functions import Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

students = {}


class Student(BaseModel):
    name: str
    age: int
    degree: str


class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    degree: Optional[str] = None


@app.get("/")
def index():
    return {"name": "First Data"}


@app.get("/student_id/{sid}")
def student_id(sid: int = Path(None, description="enter student id", gt=0)):
    if sid in students:
        return f"my name is { students[sid].name}"
    return f"student id {sid} not found"


@app.get("/student_id")
def student_id(*, name: Optional[str]):
    for student_id in students:
        if students[student_id]["name"] == name:
            return {"result": "name found in dict"}
    return {"result": "name not found in dict"}


@app.post("/new_student/{student_id}")
def new_student(student_id: int, student: Student):
    print(students)
    if student_id in students:
        print(students)
        return {"error": "student id already exist"}
    else:
        print(students)
        students[student_id] = student
        return {"result": "new student record created successfully"}


@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"error": "student not found"}

    if student.name != None:
        students[student_id]["name"] = student.name
    if student.age != None:
        students[student_id]["age"] = student.age
    if student.degree != None:
        students[student_id]["degree"] = student.degree
    return students[student_id]


@app.delete("/delete-student/{student_id}")
def delete_stud(student_id: int):
    if student_id not in students:
        return {"error": "student ID not found"}

    del students[student_id]
    return {"result": "successfully deleted student record"}
