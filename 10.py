Vegepimiento,Vegetofu ="pimiento", "tofu"
NoPeperoni,NoJamon,Nosalmon="peperoni", "jamon","salmon"
A="si"
B="no"
cliente=input("Quiere pizza vegetariana? ")


if cliente==A:
    print("Si quiere ")
    Vege=input("que ingrediente deseas para tu pizza? pimiento o tofu ")
    if Vege==Vegepimiento:
        print("pizza vegetariana con Pimiento, mozzarella y tomate")
    else:
        print("pizza vegetariana con Tofu, mozzarella y tomate")
            
else: 
    print("NO quiere pizza vegetariana")
    NoVege=input("que ingrediente deseas para tu pizza? peperoni, jamon o salmon ")
    if NoVege==NoPeperoni:
        print("pizza normal con peperoni, mozzarella y tomate ")
    elif NoVege==NoJamon:
        print("pizza normal con jamon, mozzarella y tomate ")
    else:
        print("pizza normal con salmon, mozzarella y tomate")

