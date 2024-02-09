# Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un
# palíndromo.

lista=list(input("ingresa palindromo: "))
if lista==lista.reverse():
    print("no es un palindromo")
else:
    print("ESte es palindromo")
print(lista)
