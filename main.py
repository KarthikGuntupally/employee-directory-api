from fastapi import FastAPI
import csv

app = FastAPI()

employees = []

with open("employees.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        employees.append(row)

@app.get("/employee/{employee_id}")
def get_employee(employee_id: int):
    for employee in employees:
        if int(employee["employee_id"]) == employee_id:
            return employee
    return {"error": "Employee not found"}

@app.get("/openapi.json")
def get_openapi():
    return app.openapi()
