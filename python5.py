import random

numero1=random.randint(2,10)
numero2=random.randint(2,10)
resultado=numero1*numero2

print("¿Cual es el resultado de la siguiente multiplicacion")
print(numero1, "*", numero2)
respuesta=int(input("Respuesta: "))

if respuesta==resultado:
    print ("Respuesta correcta")
else:
    print("Respuesta incorrecta. La respuesta correcta es:", resultado)