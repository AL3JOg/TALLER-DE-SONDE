# Hacer un programa que contenga la siguiente lista: [1,2,3,4,5,6,7,8,9,10] pedir al
# usuario que ingrese un valor que desea eliminar de esta lista, realizar la eliminación
# y mostrar la nueva lista.
lista= [1,2,3,4,5,6,7,8,9,10]
delet=int(input("que valor deseas eliminar: "))

lista.remove(delet)
print(lista)
