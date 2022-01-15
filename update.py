from pymongo import MongoClient

# creating connectioons for communicating with Mongo DB
client = MongoClient('localhost:27017')
db = client.EmployeeData


# Function to update record to mongo db
def update():
    try:
        criteria = input("ingrese ID de actualizacion: ")
        name = input("ingrese nombre a actualizar: ")
        age = input("ingrese edad a actualizar: ")
        country = input("ingrese pais a actualizar: ")

        db.Employees.update_one(
        {"id": criteria},
        {
            "$set": {
                "name": name,
                "age": age,
                "country": country
            }
        }
        )
        print ("actualizacion guardada")

    except ImportError:
        platform_specific_module = None
