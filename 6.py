CantidadCajas=int(input("Ingresa la cantidad de cajas: "))
PesoPayasos=112
PesoMuñeca=76
i=1
while CantidadCajas>=i:
    print("caja # ",i)
    CantidadPayasos=int(input("Ingresa la cantidad de payasos: "))
    CantidadMuñeca=int(input("Ingresa la cantidad de Muñecas: "))
    PesoTotal=(CantidadPayasos*PesoPayasos)+(CantidadMuñeca*PesoMuñeca)

    print("el peso total de la caja ",i," es de: ",PesoTotal,"kg")
    i+=1


