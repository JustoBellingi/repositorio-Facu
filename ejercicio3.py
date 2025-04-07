num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

suma = 0
for i in range(num1 + 1, num2):
    suma += i

print("La suma es:", suma)
