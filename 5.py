# Escribir un programa que almacene el abecedario en una lista, al final debe mostrar
# las letras que están en posiciones que son múltiplos de 3.

abc=[ "a", "b", "c", "d", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
for i in range(0,27):   
    resto=i%3
    if resto>=1:   
        continue
    else:
        print(abc[i])
        

        