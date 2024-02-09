lista=[]
for i in range (0,10):
    nume=int(input("Ingresa un numero entero: "))
    lista.append(nume)
    if nume<1:
        print("ERROR NO PUEDES INGRESAR NUMEROS NEGATIVOS")
        break

lista.sort()
lista.reverse()
print(lista)