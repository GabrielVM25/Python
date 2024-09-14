name = str(input("Ingresa tu nombre:"))
age = int(input("Ingresa tu edad:"))
def notes() :
    average = float(input("Ingresa tu nota promedio:"))
    if average >= 70:
        return "Aprobado, su nota es:" + str(average)
    elif average <= 69:
        return "Reprobado, su nota es:" + str(average)
    else:
        return "Recuperatorio, su nota es:" + str(average)
print (f"Estudiante: {name} de {age} años de edad Su estado es {notes()}")

# Crear variable name(str) y age(int)
# Definir función "notes"
# Crear variable average(float)
# Si average es mayor o igual a 70, regresar Aprobado y "average"
# De lo contrario si average es menor o igual a 69, regresar Reprobado y "average"
# De otro modo, regresar Recuperatorio y "average"
# Imprimir el nombre del estudiante, su edad, su estado en la asignatura y su nota promedio