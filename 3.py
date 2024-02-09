# Escribir un programa que le pida al usuario ingresar nombres de personas, una vez
# que el usuario escriba me voy debe parar de preguntar por nombres y mostrar los
# que el usuario agregó ordenados de la z a la a.
names=[]
exit="me voy"
i=True
while i:
    nome=input("Ingresa nombre de la persona: ")
    if nome==exit:
        i=False
        print("Ya te saliste mi valecita...")
        continue
    names.append(nome)

names.sort()
names.reverse()
print(names)