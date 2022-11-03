"""
Comentario
de varias
lineas
"""
while True:
    nombre=input("¿Como te llamas? ")
    if nombre=="":
        print("No has escrito nada",end=" \n")
    else:
        print(f"Hola {nombre} encantado",end="\n")
        print("Adios")
        break;