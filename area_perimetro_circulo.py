#programa para calcular el área y el perimetro de un circulo de radio R

#inicio
import math
r = input("digite el radio del circulo: ")
π = 3,1416
a = 0
p = 0

#proceso
print()
print("procesando...")
print()

r = int(r)

a = π * (r * r)
p = 2 * π * r

#output :P
print("el área del circulo es: " + str(a))
print("el preimetro del circulo es:" + str(p))

print()
print("(presione Enter para salir)")
input()

