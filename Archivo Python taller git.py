import math
"operaciones matematicas Basicas"
a=50
b=15
c=30

Suma=a+b+c
Resta=a-b-c
Multiplicacion=a*b*c
Division=(a/b)/c

print(f"Suma = {Suma}")
print(f"Resta = {Resta}")
print(f"Multiplicacion = {Multiplicacion}")
print(f"Division = {Division}")

"operaciones complejas"
potencia=(a**b)**c
raiz=math.sqrt(a*b*c)
factorial_a= math.factorial(a)
promedio= (a+b+c)/3

combinaciones = math.comb(a, b)
permutaciones = math.perm(a, b)

print(f"Potencia = {potencia}")
print(f"Raiz = {raiz}")
print(f"Factorial de a = {factorial_a}")
print(f"Promedio = {promedio}")
print(f"Combinaciones = {combinaciones}")
print(f"Permutaciones = {permutaciones}")