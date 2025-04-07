numeroTotal = 0
while True:
    numero = int(input("Ingresa un número para sumar: "))
    if numero == 0:
        break
    numeroTotal = numeroTotal + numero

print("Suma total:", numeroTotal)
