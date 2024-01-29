CantidadPanes=int(input("Ingresa la cantidad de panes vendidos que no son del dia: "))
PrecioPan=3.49
PrecioTotal=CantidadPanes*PrecioPan
PanNoFresco=(60/100)*PrecioTotal
i=1
while CantidadPanes>i:

    print("El precio habitual de la barra de pan es de: ",PrecioPan)
    print("Precio con descuento del 60%: ",PanNoFresco)
    i+=1
    
