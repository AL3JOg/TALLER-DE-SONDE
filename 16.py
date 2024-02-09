# Hacer un programa que cree una lista vacía, luego debe mostrar un menú con las
# siguientes opciones:
# -1 para agregar elementos a la lista
# -2 para buscar la posición de un elemento en la lista
# -3 para eliminar un elemento por la posición del mismo en la lista
# -4 para eliminar un elemento por el valor del mismo en la lista
# -5 para ver la lista
# -6 para salir y finalmente se debe mostrar la lista
# -7 para agregar una lista a la lista original, los valores se deben ingresar separados
# por una coma
# -8 para vaciar la lista
# -9 para saber cuántas veces está un elemento en la lista
# -10 para agregar un elemento en la posición que desee el usuario
# -11 para mostrar la lista al revés pero sin modificar la primera
# -12 para mostrar la lista ordenada de menor a mayor si se puede sin afectar la lista
# original
# -13 para mostrar la lista ordenada de mayor a menor si se puede sin afectar la lista
# origina
lista=[]

b=["1 para agregar elementos a la lista","2 para buscar la posición de un elemento en la lista","3 para eliminar un elemento por la posición del mismo en la lista","4 para eliminar un elemento por el valor del mismo en la lista","5 para ver la lista","6 para salir y finalmente se debe mostrar la lista","7 para agregar una lista a la lista original, los valores se deben ingresar separados por una coma","8 para vaciar la lista","9 para saber cuántas veces está un elemento en la lista","10 para agregar un elemento en la posición que desee el usuario","11 para mostrar la lista al revés pero sin modificar la primera","12 para mostrar la lista ordenada de menor a mayor si se puede sin afectar la lista original","13 para mostrar la lista ordenada de mayor a menor si se puede sin afectar la lista original"]
while True:
    for i in range(0,len(b)):
        print(b[i])
    elige=int(input("Ingresa: "))
    if elige==1:
        ingresar=input("Agregar: ")
        lista.append(ingresar)
    elif elige==2:
        busca=input("Buscador: ")
        lista.index(busca)
    elif elige==3:
        bor=int(input("Ingresa posicion a borrar: "))
        lista.pop(bor)
    elif elige==4:
        dell=input("Valor a eliminar: ")
        lista.remove(dell)
    elif elige==5:
        print(lista)
    elif elige==6:
       print(lista)
       print("Estoy cansado jefe...")
       break
    elif elige==7:
        op=input("Elementos de la nueva lista a agregar(ESCRIBE salir PARA TERMINAR): ")
        op.split()       
        lista.extend(op)
    elif elige==8:
        print("borraste la base de datos, DESPEDIDO")   
        lista.clear()
    elif elige==9:
        bus=input("Buscando cuantas veces esta: ")  
        cont=lista.count(bus)
        print(cont)
    elif elige==10:
        clear=int(input("Ingresa pocision: "))
        number=int(input("Ingresa lo que deseas agregar: "))
        lista.insert(clear,number)
    elif elige==11:
        lista.reverse()
    elif elige==12:
        lista.sort()
    elif elige==13:
        lista.sort(reverse=True)

