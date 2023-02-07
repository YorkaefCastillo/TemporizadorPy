import time

ador,Titulo = "","cuenta regresiva"

print(f"{ador.center(50,'*')}")
print(f"{Titulo.center(50).upper()}")
print(f"{ador.center(50,'*')}")

#Bloque de cuenta regresiva
def cuenta_regresiva(t):
    while t:
        minutos, segundos = divmod(t,60)
        timer = f"{minutos}:{segundos}"
        print(timer, end="\r")
        time.sleep(1)
        t -=1
    print("Tiempo completo")



#pide  el tiepo en segundos 
t = int(input("Ingrese el tiempo en segundos: "))

#muestra bloque anterior 
cuenta_regresiva(t)
