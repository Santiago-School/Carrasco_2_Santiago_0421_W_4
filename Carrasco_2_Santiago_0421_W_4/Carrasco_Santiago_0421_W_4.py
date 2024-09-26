print(" ")
print("Santiago Carrasco 3°W")
print("")

# leer los tres valores
a = float(input("introduce el valor de a: "))
b = float(input("introduce el valor de b: "))
c = float(input("introduce el valor de c: "))

if a == b or a == c or b == c:
    print("los valores no deben ser iguales")
else: 
# determinar el mayor y el menor
    mayor = max(a, b, c)
    menor = min(a, b, c)

# ahora despliegara cual es mayor y menor
print("el mayor es:", mayor)
print("el menor es:", menor)