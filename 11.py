while True:
    entrada_de_eco = input("Hola mundo")
    if entrada_de_eco.lower() == 'salir':
        print("Saliendo")
        break
    else:
        print("Eco:", entrada_de_eco)