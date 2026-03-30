# Lista donde se almacenara la informacion de los estudiantes
registros = [

    {"id": 1143245632, "nombre": "Randy", "edad": 19, "programa": "sistemas", "estado": "activo"},
    {"id": 1234567890, "nombre": "Maria", "edad": 17, "programa": "sistemas", "estado": "activo"},
    {"id": 1223345567, "nombre": "Luis", "edad": 21, "programa": "sistemas", "estado": "inactivo"},
    {"id": 1112223334, "nombre": "Jhon", "edad": 22, "programa": "sistemas", "estado": "activo"},
    {"id": 1673452134, "nombre": "Luisa", "edad": 20, "programa": "sistemas", "estado": "inactivo"},
    {"id": 1395462312, "nombre": "Jose", "edad": 22, "programa": "sistemas", "estado": "activo"},
    {"id": 1432564325, "nombre": "Martha", "edad": 19, "programa": "sistemas", "estado": "activo"},
    {"id": 1236754356, "nombre": "Juan", "edad": 18, "programa": "sistemas", "estado": "activo"},
    {"id": 1222348764, "nombre": "Alberto", "edad": 18, "programa": "sistemas", "estado": "activo"},
    {"id": 1111467834, "nombre": "Manuel", "edad": 19, "programa": "sistemas", "estado": "activo"}
    
]

# Funcion para registrar estudiantes

def registrar_estudiantes(estudiantes):

    

    estudiantes = {
        "id": id,
        "nombre": nombre,
        "edad": edad,
        "programa": programa,
        "estado": estado
    }

    registros.append(estudiantes)

    print("Successful Student Registration")

# Funcion consultar lista de estudiantes

def consultar_lista_estudiantes(registros):
    
    if len(registros) == 0:
        print("The list is empty")
        return
    
    for e in registros:
        print(f"Id: {e['id']} | Nombre: {e['nombre']} | Edad: {e['edad']} | Programa: {e['programa']} | Estado: {e['estado']}")

# Funcion para buscar estudiantes por el nombre

def buscar_estudiantes(registros, nombre):

    for e in registros:
        if e["nombre"].lower() == nombre.lower():
            return e

    return None

#Funcion para actualizar informacion

def actualizar_informacion(registros, nombre, nueva_edad, nuevo_estado):

    estudiantes = buscar_estudiantes(registros, nombre)

    if estudiantes is None:
        print("Student not found")
        return

    if nueva_edad is not None:
        estudiantes["edad"] = nueva_edad

    if nuevo_estado is not None:
        estudiantes["estado"] = nuevo_estado

    print("Student updated successfully")

# Funcion para eliminar un estudiante

def eliminar_estudiante(registros, nombre):

    estudiantes = buscar_estudiantes(registros, nombre)

    if estudiantes:
        registros.remove(estudiantes)
        print("Student deelete")
    else:
        print("Student not found")


while True:

    print("\n--- STUDENT MANAGEMENT ---")
    print("1. Register new students")
    print("2. Check the student list")
    print("3. Find a student")
    print("4. Update student information")
    print("5. Delete students")

    opcion = input("Select an option: ")

    if opcion == "1":
        nombre = input("Name: ")
        id = int(input("Enter ID: "))
        edad = int(input("Enter Age: "))
        programa = input("Enter the Program: ")
        estado = input("Active/Inactive: ")

        registrar_estudiantes(nombre)

    elif opcion == "2":

        consultar_lista_estudiantes(registros)
    
    elif opcion == "3":

        nombre = input("Name of student to look for: ")

        estudiante = buscar_estudiantes(registros, nombre)

        if estudiante:
            print(estudiante)
        else:
            print("Student not found")

    elif opcion == "4":

        nombre = input("Student to update: ")

        try:
            edad = input("New age (enter to skip): ")
            estado = input("New status (enter to skip): ")

            edad = int(edad) if edad else None
            estado = int(estado) if estado else None

            actualizar_informacion(registros, nombre, edad, estado)

        except ValueError:
            print("Invalid data")

    elif opcion == "5":

        nombre = input("Student to be eliminated: ")
        eliminar_estudiante(registros, nombre)

























while True:

    print("\n--- GESTION DE ESTUDIANTES ---")
    print("1. Registrar nuevos estudiantes")
    print("2. Consultar la lista de estudiantes")
    print("3. Buscar un estudiante")
    print("4. Actualizar informacion de estudiante")
    print("5. Eliminar estudiantes")