asig=[]
nota=[]
A="salir"
i=True

while i:
    mat=input("Materia: ")
    if mat==A:
            print("saliendo.....")
            i=False
            continue
    asig.append(mat)
    note=float(input("nota: "))
    nota.append(note)

for i in range(0,len(asig)):
      print("La materia",asig[i],"tienes la nota de: ",nota[i])