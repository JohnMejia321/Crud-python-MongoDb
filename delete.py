from pymongo import MongoClient

# creating connectioons for communicating with Mongo DB
client = MongoClient('localhost:27017')
db = client.EmployeeData

def delete():
    try:
        criteria=input("ingrese ID de empleado a borrar: ")
        db.Employees.delete_many({"id":criteria})
        print ("empleado borrado")
    except ImportError:
        platform_specific_module=None