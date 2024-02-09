#  Hacer un programa que contenga la siguiente lista: [1,2,3,4,5,6,7,8,9,10] pedir al
# usuario que ingrese un elemento que desea agregar y luego ingrese la posición en
# que desea agregarlo, finalmente debe mostrar la lista con el elemento agregado.
lista= [1,2,3,4,5,6,7,8,9,10]
clear=int(input("Ingresa pocision: "))
number=int(input("Ingresa numero a agregar: "))

lista.insert(clear,number)
print(lista)