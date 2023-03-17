from random import choice, randrange
from datetime import datetime

# Operadores posibles
operators = ["+", "-", "/", "*"]

# Cantidad de cuentas a resolver
times = 5

# Contador inicial de tiempo.
# Esto toma la fecha y hora actual.
init_time = datetime.now()

print(f"¡Veremos cuanto tardas en responder estas {times} operaciones!")

correctas = 0
incorrectas = 0
for i in range(times):
    # Se eligen números y operador al azar
    number_1 = randrange(10)
    number_2 = randrange(10)
    operator = choice(operators)
    # Se imprime la cuenta.
    print(f"{i+1}- ¿Cuánto es {number_1} {operator} {number_2}?")
    # Le pedimos al usuario el resultado
    result = input("resultado: ")
    # Verificamos si la respuesta es correcta o no
    resultado = eval(f"{number_1} {operator} {number_2}") 
    if resultado == int(result):
        print("Respuesta correcta!")
        correctas =correctas + 1
        
    else:
        print("Respuesta incorrecta.")
        incorrectas = incorrectas+ 1      
# Al terminar toda la cantidad de cuentas por resolver.
# Se vuelve a tomar la fecha y la hora.
end_time = datetime.now()
# Restando las fechas obtenemos el tiempo transcurrido.
total_time = end_time - init_time
# Mostramos ese tiempo en segundos.
print(f"\n Tardaste {total_time.seconds} segundos.")
print(f"TOTAL DE RESPUESTAS CORRECTAS {correctas} TOTAL DE RESPUESTAS INCORRECTAS {incorrectas}")