# Hacer un programa que le pida al usuario números enteros hasta que escriba la
# palabra salir al final se debe mostrar cada número con su cuadrado (es decir el
# resultado de el número elevado a la 2)
exit="salir"
while True:
    num=input("Ingresa un entero ")
    
    if (str(num)==exit):
        False
        print("saliendo...")
        break
    op=(int(num)**2)
    print(op)

