import insert
import read
import update
import delete


class Programa:

    def __init__(self):
        self.dato = 1

    def menu(self):
        
        while self.dato:

            selection = input(
                "seleccione 1 para insertar,2 para actualizar,3 para leer, y 4 para borrar: ")

            if selection == "1":
             insert.insert()
            elif selection == "2":
             update.update()
            elif selection == "3":
             read.read()
            elif selection == "4":
             delete.delete()
            else:
             print("seleccion invalida")
             

persona1=Programa()
persona1.menu()
