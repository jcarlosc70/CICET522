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

count = 0
resultado = 0
while count < len(students):
    if students[count].startswith("M"):
        resultado +=1
    count += 1
print(resultado)

# 4.Pantalla por cada estudiante: El estudiante {estudiante} ocupa el lugar {}

