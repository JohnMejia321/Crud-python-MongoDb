from pymongo import MongoClient

client = MongoClient("localhost:27017")
db=client.EmployeeData

def insert():
    try:
        employeeid=input("ingrese ID de empleado: ")
        employeename=input("ingrese nombre de empleado: ")
        employeeage=input("ingrese edad de empleado: ")
        employeecountry=input("ingrese pais de empleado: ")
        db.Employees.insert_one(
            {
                "id": employeeid,
                "name": employeename,
                "age": employeeage,
                "country": employeecountry
                
            }
        )
        print ("se inserto el dato")
    except ImportError:
        platform_specific_module=None
