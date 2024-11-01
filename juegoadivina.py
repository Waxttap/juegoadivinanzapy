import random

numero_secreto = random.randint(0,100)
adivinado = False
cant_intentos = 0
max_intentos = 5
adivinado = False

print("Bienvenido al juego de adivinar el número secreto")

while not adivinado and cant_intentos < max_intentos:
    entrada = input("Introduce un número del 1 al 99: ") # TODO: conv a número
    numero = int(entrada)
    
    if numero == numero_secreto:
        print("Felicitaciones has adivinado el número secreto")
        adivinado = True
    elif numero < numero_secreto:
        print("El número es mayor al ingresado")
    else: 
        print("El número es menor al ingresado")
    
    cant_intentos += 1

if not cant_intentos < max_intentos:
    print("Game Over! No has podido adivinar dentro de los 5 intentos")

