# Hacer un programa que contenga la siguiente lista: [1,2,3,4,5,6,7,8,9,10] pedir al
# usuario que ingrese una posición de la lista que desea eliminar, realizar la
# eliminación y mostrar la nueva lista.
lis= [1,2,3,4,5,6,7,8,9,10]
clear=int(input("Ingresa pocision de la lista a eliminar: "))
lis.pop(clear)
print(lis)

