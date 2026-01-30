#Programa para calcular el área y el perimetro de un circulo de radio R

#Librerias
import math

print("----------------------------------")
print("---Area y perimetro del circulo---")
print("----------------------------------")

#input
r = input("Ingrese el valor del radio del circulo: ")
r = int(r)

#procesing
a = math.pi*r**2
p= 2*math.pi*r

#output
print("----------------------------------")
print("-----------Resultados-------------")
print("----------------------------------")
print("El área del círculo es: " +str(a))
print("El perimetro del circulo es: " + str(p))
print("------------------------------------")
