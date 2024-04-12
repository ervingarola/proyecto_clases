import os
import sys
sys.path.append(r"C:\Users\DELL 5400\Desktop\proyecto-en-clases")
from dao import daoConnection
from models import clases as c


os.system('cls')
conex = daoConnection.Connection("localhost", "root", "", "dbregisters")
conex.connect()


def insertarCiudad():
    nombreCiudad = input("Nombre ciudad\n")
    ciudad = c.City(nombreCiudad, 1, any)
    daoCity = daoConnection.DaoCity(conex)
    daoCity.insert(ciudad)

def mostrarCiudad(): 
    daoCity=daoConnection.DaoCity(conex)
    cities = daoCity.get_all()
    for city in cities:
        print(city)

def updateCiudad():
    id=input("codigo ciudad")
    nombre = input("Nombre ciudad\n")
    ciudad = c.City(id, nombre, 1)
    daoCity = daoConnection.DaoCity(conex)
    daoCity.update(ciudad)


def deleteCiudad():
    id=input("codigo ciudad")
    daoCity = daoConnection.DaoCity(conex)
    daoCity.delete(id)

def buscarCiudad():
    nombre = input("Nombre ciudad\n")
    ciudad = c.City(0, nombre, 1)
    print(ciudad)
    daoCity = daoConnection.DaoCity(conex)
    reg = daoCity.buscar(nombre)
    print(reg)

def buscarCiudadId():
    id = int(input("Id: "))
    daoCity = daoConnection.DaoCity(conex)
    reg = daoCity.get_by_id(id)
    print(reg)

def insertarjob():
    nombreTrabajo = input("Nombre  del job \n")
    job = c.Job(nombreTrabajo, 1, any)
    daojob = daoConnection.Daojob(conex)
    daojob.insert(job)

def mostrarjob(): 
    daojob=daoConnection.Daojob(conex)
    job = daojob.get_all()
    for job in job:
        print(job)

def updatejob():
    nombre = input("Nombre del job\n")
    job = c.job( nombre, 1, any)
    daojob = daoConnection.Daojob(conex)
    daojob.update(job)


def deletejob():
    id=input("codigo job")
    daojob = daoConnection.Daojob(conex)
    daojob.delete(id)

def buscarjob():
    nombre = input("Nombre del trabajo\n")
    job = c.job(0, nombre, 1)
    print(job)
    daojob = daoConnection.Daojob(conex)
    reg = daojob.buscar(nombre)
    print(reg)

def buscarjobId():
    id = int(input("Id: "))
    daojob = daoConnection.Daojob(conex)
    reg = daojob.get_by_id(id)
    print(reg)

def insertarEmployee():
    name = input("Nombre del Trabajador\n")
    ciudad_id = mostrarCiudad()
    ciudad_id =int(input("elija el id de la ciudad del trabajador\n"))
    job_id = mostrarjob() 
    job_id =int(input("elija el id del trabajo\n"))
    salary = int(input("Salario del Trabajador\n"))
    Employee = c.Employee(name, ciudad_id, job_id, salary, status=1)
    daoEmployee = daoConnection.DaoEmployee(conex)
    daoEmployee.insert(Employee)

def mostrarEmployee(): 
    daoEmployee=daoConnection.DaoEmployee(conex)
    Employee = daoEmployee.get_all()
    for Employee in Employee:
        print(Employee)

def updateEmployee():
    id=input("codigo Employee")
    nombre = input("Nombre del Trabajador\n")
    Employee = c.Employee(nombre, 1, id)
    daoEmployee = daoConnection.DaoEmployee(conex)
    daoEmployee.update(Employee)


def deleteEmployee():
    id=input("codigo del Trabajador")
    daoEmployee = daoConnection.DaoEmployee(conex)
    daoEmployee.delete(id)

def buscarEmployee():
    nombre = input("Nombre del Trabajador\n")
    Employee = c.Employee(0, nombre, 1)
    print(Employee)
    daoEmployee = daoConnection.DaoEmployee(conex)
    reg = daoEmployee.buscar(nombre)
    print(reg)

def buscarEmployeeId():
    id = int(input("Id: "))
    daoEmployee = daoConnection.DaoEmployee(conex)
    reg = daoEmployee.get_by_id(id)
    print(reg)


def Menu():
    print("1. ingresar datos")
    print("2. Editar datos")
    print("3. Mostrar datos")
    print("4. Eliminar datos")
    print("5. buscar datos")
    print("6. salir")


def mainCuidad():
    opcion = 0
    while(opcion != 6):
        Menu()
        opcion = int(input("dime tu opcion\n" ))
        if (opcion == 1 ):
            insertarCiudad()
            os.system("pause")
        elif(opcion == 2):
            updateCiudad()
            os.system("pause")
        elif(opcion == 3):
            mostrarCiudad()
            os.system("pause")
        elif(opcion == 4):
            deleteCiudad()
            os.system("pause")
        elif(opcion == 5):
            buscarCiudad()
            os.system("pause")
        if(opcion == 6):
            print("saliendo del menu")
            break

def mainjob():
    opcion = 0
    while(opcion != 6):
        Menu()
        opcion = int(input("dime tu opcion\n" ))
        if (opcion == 1 ):
            insertarjob()
            os.system("pause")
        elif(opcion == 2):
            updatejob()
            os.system("pause")
        elif(opcion == 3):
            mostrarjob()
            os.system("pause")
        elif(opcion == 4):
            deletejob()
            os.system("pause")
        elif(opcion == 5):
            buscarjob()
            os.system("pause")
        if(opcion == 6):
            print("saliendo del menu")
            break

def mainEmployee():
    opcion = 0
    while(opcion != 6):
        Menu()
        opcion = int(input("dime tu opcion\n" ))
        if (opcion == 1 ):
            insertarEmployee()
            os.system("pause")
        elif(opcion == 2):
            updateEmployee()
            os.system("pause")
        elif(opcion == 3):
            mostrarEmployee()
            os.system("pause")
        elif(opcion == 4):
            deleteEmployee()
            os.system("pause")
        elif(opcion == 5):
            buscarEmployee()
            os.system("pause")
        if(opcion == 6):
            print("saliendo del menu")
            break

def main():
    opcionprincipal = 0
    while(opcionprincipal != 3):
        print("BIENVENIDOS AL REGISTRO")
        print("1. menu ciudad")
        print("2. menu trabajo")
        print("3. empleados")
        opcionprincipal = int(input("selecciona una opcion\n"))
        if(opcionprincipal == 1):
            mainCuidad()
            os.system("pause")
        if(opcionprincipal == 2):
            mainjob()
            os.system("pause")
        if(opcionprincipal == 3):
            mainEmployee()
            os.system("pause")
       
main()
