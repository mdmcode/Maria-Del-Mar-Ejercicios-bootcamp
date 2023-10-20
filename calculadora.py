from math import *

def operar(n1, n2, operador):
    resultado = None
    if operador == '+':
        resultado = int(n1) + int(n2)
    if operador == '-':
        resultado = int(n1) - int(n2)
    if operador == '/':
        resultado = int(n1) / int(n2)
    if operador == '*':
        resultado = int(n1) * int(n2)

    return resultado

print("Bienvenido a la calculadora")

while True:
    primerNumero = int(input("Ingrese el primer numero: "))
    operador = input("Ingrese el operador: ")
    segundoNumero = int(input("Ingrese el segundo numero: "))

    result = operar(primerNumero, segundoNumero, operador)
    print(f"El resultado es {result}\n")

    continuar = input("¿Desea salir? ")

    if continuar.lower() == 'si':
        break
    else: 
        pass