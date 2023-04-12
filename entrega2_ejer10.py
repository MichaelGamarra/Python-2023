nombres = ''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR',
'David','Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo',
'Francsica', 'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan',
'Joaquina', 'Jorge','JOSE', 'Javier', 'Joaquín' , 'Julian', 'Julieta', 'Luciana',
'LAUTARO', 'Leonel', 'Luisa', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias',
'Nicolás', 'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises',
'Yanina' '''

notas_1 = [81, 60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69,
12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44,
85, 73, 37, 42, 95, 18, 7, 74, 60, 9, 65, 93, 63, 74]
notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37,
64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73,
95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10]


# Separar los nombres en una lista
nombres_lista = nombres.replace("\n", "").split(",")

# Unir las dos listas de notas en una lista de tuplas
notas_tuplas = list(zip(notas_1, notas_2))

# Crear el diccionario con las notas de cada estudiante
notas_estudiantes = {}
for i in range(len(nombres_lista)):
    notas_estudiantes[nombres_lista[i]] = list(notas_tuplas[i])

print(notas_estudiantes)

#crear un diccionario con los promedios
promedios = {}

for estudiante, notas in notas_estudiantes.items():
    promedio = sum(notas) / len(notas)
    promedios[estudiante] = promedio

for nombre, promedio in promedios.items():
    print(f"{nombre}: {promedio}")

#promedio general
promedio_general = sum(promedios.values()) / len(promedios)
print("El promedio general del curso es:", promedio_general)



# maximo y minimo

mejor_estudiante = max(promedios, key=promedios.get)
peor_estudiante = min(notas_estudiantes, key=notas_estudiantes.get)
print("el estudiante por exelencia es: " + mejor_estudiante)
print("el estudiante mas boludo es: "+ peor_estudiante)


# Obtenemos la clave (nombre del alumno) y el valor (nota) del elemento con la nota más alta
mejor_alumno, mejor_nota = max(promedios.items(), key=lambda x: x[1])
peor_alumno, peor_nota = min(notas_estudiantes.items(), key=lambda x: x[1])[0]
# Imprimimos el resultado obtenido
print(f"El mejor estudiante es {mejor_alumno} con una nota de {mejor_nota}")
print(f"El peor estudiante es {peor_alumno} con la nota de {peor_nota}")