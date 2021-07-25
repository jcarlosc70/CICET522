students = ["Pedro", "Luís", "Milagros", "Marta", "Macarena", "Marcelo", "Epifanio"]

# 1.Hacer un backup de la lista students en una variable students_copy (Utilizar el método apropiado) y trabajar solo con esta lista

students_backup = students.copy()
# print(students_backup)

# # 2.Cuántos estudiantes hay en total?
# print(len(students))

# 3.La estudiante Milagros ha abandonado el curso, eliminarla de la lista backup

# students_backup.remove("Macarena")
# print(students_backup)

# 4.Ahora que lista ha cambiado su longitud, qué posición ocupa Macarena?

# print(students_backup.index("Macarena"))

# # 5.Agregar un nuevo estudiante, Germán, a la mitad de la lista

# students_backup.insert((len(students_backup)//2), "German")
# print(students_backup)

# 6.Unir los nuevos estudiantes al final de la lista backup
new_students = ["Felipe", "Tomas", "Facundo"]

students_backup.extend(new_students)
# print(students_backup)

# 7.Reescribir students con students_backup con todos los cambios efectuados

students = students_backup.copy()
# print(students)

# WHILE

# 1.Con la ayuda de una iteracción, mostrar todos los nombres en mayúscula

# lo = "lo"
# count = 0
# while count < len(students):
#     print(students[count].upper())
#     count += 1

# 2. Mostrar por panatalla todos los nombres agregando el sufijo "lo"
# lo = "lo"
# count = 0
# while count < len(students):
#     print(students[count] + lo)
#     count += 1

# 3.Cuántos nombres empiezan con la letra "M"?

# count = 0
# resultado = 0
# while count < len(students):
#     if students[count].startswith("M"):
#         resultado +=1
#     count += 1
# print(resultado)

# 4.Pantalla por cada estudiante: El estudiante {estudiante} ocupa el lugar {}
# count = 0
# while count < len(students):
#     print(f"el estudiante {students[count]} ocupa la posicion {count} ")
#     count += 1

# 5.Considerando el punto anterior y con la ayuda del operador in mostrar por pantalla:

approved_students = ["Pedro", "Felipe", "Macarena", "Epifanio"]

# count = 0
# while count < len(students):
#     if students[count] in approved_students:
#         # print(f"El estudiante {students[count]} ha aprobado")
#     else:
#         # print(f"El estudiante {students[count]} NO ha aprobado")
#     count += 1

# 6.Permitir al user buscar la posición de un estudiante (Sin list methods)

# user = input("students search: ")
# count = 0
# while count < len(students):
#     if user in students:
#         print(f"el estudiante {user} se encuentra en la posicion {count}")
#         count = len(students) + 1
#     else:
#         print("Estudiante no encontrado")
#     count += 1
# print(students)

# 7.Permitir al user buscar un estudiante y de encontrarlo, preguntar por qué nombre quiere cambiarlo -->

# user = input("students search: ")
# count = 0
# while count < len(students):
#     if user == students[count]:
#         students[count] = input("New Name: ") 
#     count = len(students) + 1
# print(students)# 4.Pantalla por cada estudiante: El estudiante {estudiante} ocupa el lugar {}

# 8.Permitir al user indicar un nombre de la lista students y así poder unirlo a la lista vacía new_course

# count = 0
# new_course = []
# user = input("Estudiante a agregar: ")
# while count < len(students):
#     if user == students[count]:
#         new_course.append(user)
#     count += 1
# print(new_course)

print("---Bienvenido a Students App---")
print("1. Buscar estudiante")
print("2. Buscar y actualizar estudiante")
print("3. Para Salir")
user = input("Elija una opcion: ")

while user != "3":
    if user == "1":
        user = input("Estudiante a buscar: ")
        count = 0
        while count < len(students):
            if user == students[students]:
                print(f"El estudiante {user} se encuentra en la oposicion {count}")
            count = len(students)
            count += 1
    user = input("Y ahora que?: ")