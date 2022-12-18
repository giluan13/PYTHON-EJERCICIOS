def calcularArea(a, b):
    area = (b* a) / 2 
    return area
print("Ingresar altura")
a = float(input())
print("ingresar base")
b = float(input())

print("El area es"  + str(calcularArea(a, b)))
