# Escribir un programa que almacene las asignaturas de un curso (por ejemplo
# Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la
# nota que ha sacado en cada asignatura y elimine de la lista las asignaturas
# aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el
# usuario tiene que repetir, el usuario pierde una materia si saca menos 3.5
asig=[]
nota=[]
A="salir"
i=True
win=3.5
while i:
    mat=input("Materia: ")
    if mat==A:
            print("saliendo.....")
            i=False
            continue
    asig.append(mat)
    note=float(input("nota: "))
    nota.append(note)
    if note>=win:
         nota.remove(note)
         asig.remove(mat)          
for i in range(0,len(asig)):
      print("La materia",asig[i],"tienes la nota de: ",nota[i],"debes repetir la materia")