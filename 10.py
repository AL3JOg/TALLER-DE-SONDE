# Escribir un programa que pida el ingreso de temperaturas y se vayan agregando a
# una lista hasta que escriba la palabra salir, al final se debe mostrar el promedio de
# los valores ingresados por el usuario.
temp=[]
exit="salir"
suma=0

while True:
    temperaturas=input("Temperatura: ") 
    if temperaturas==exit:
        False
        print("que frio, adios")
        break
    pr=int(temperaturas)    
    temp.append(pr)
for i in range(0,len(temp)):
    suma=temp[i]+suma
prom=(suma/len(temp))
print("El promedio de los datos es:",prom)


    
