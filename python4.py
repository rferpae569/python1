peso=float(input("ingresa tu peso en kg:"))
estatura=float(input("Ingresa tu estatura en metros:"))

imc=round(peso/estatura**2,2)

print("Tu indice de masa corporal es", imc)