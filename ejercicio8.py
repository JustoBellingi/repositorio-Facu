numero = 100 

pares = 0
impares = 0
positivos = 0
negativos = 0

for n in range(numero):
    n = int(input("Ingresa un número: "))
    if n % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1
    if n > 0:
        positivos = positivos + 1
    elif n < 0:
        negativos = negativos + 1

print("Cantidad de pares:", pares)
print("Cantidad de impares:", impares)
print("Cantidad de positivos:", positivos)
print("Cantidad de negativos:", negativos)
