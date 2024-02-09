# Crear dos listas vacías, una para nombres de usuario y otra para edades, el
# programa debe pedir al usuario que ingrese un nombre y una edad (todas las veces
# que quiera hasta que escriba salir como nombre) al final se debe mostrar el nombre
# de cada usuario y si es o no mayor de edad
nombres=[]
edades=[]
mayor=18
exit="salir"

while True:
    names=input("Ingresa tu nombre: ")
    if names==exit:
        False
        print("adios")
        break
    nombres.append(names)
    year=int(input("Edad: "))
    edades.append(year)
    
for i in range (0,len(nombres)):
    print("Nombre: ",nombres[i],"Nombre: ",edades[i])
    if edades[i]<18:
        print("Es menor de edad")
    else:
        print("Es mayor de edad")

   


