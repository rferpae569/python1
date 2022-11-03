import datetime
try:
    num=int(input("Escribe un numero: "))
    if num<0:
        raise "Error numero negativo"
    for i in range(0,num,2):
        print(i,end=" ")
except ValueError as e:
    print("Error debe ser un numero: {e}")
except KeyboardInterrupt as e2:
    print(e2)
except:
    print("Excepcion generica")
    