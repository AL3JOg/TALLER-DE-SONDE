# Hacer un programa que contenga la siguiente lista: [1,2,3,4,5,6,7,8,9,10] pedir al
# usuario que ingrese un elemento que desea buscar en la lista al final se debe buscar
# la posición en la que está dicho elemento.
lista= [1,2,3,4,5,6,7,8,9,10]
number=int(input("Ingresa numero a buscar: "))
i=lista.index(number)
print(i)
