from fastapi import FastAPI
import csv

app = FastAPI()

employees = {}

with open('employees.csv', mode='r') as infile:
    reader = csv.DictReader(infile)
    for row in reader:
        employees[int(row["employee_id"])] = row["employee_name"]

@app.get("/employee/{employee_id}")
def read_employee(employee_id: int):
    if employee_id in employees:
        return {"employee_id": employee_id, "employee_name": employees[employee_id]}
    else:
        return {"error": "Employee not found"}
