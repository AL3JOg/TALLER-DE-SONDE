# Hacer un programa que junte en una sola lista las dos siguientes: [1,2,3,4,5] y
# [6,7,8,9,10] y al final muestre la lista nueva.
x=[1,2,3,4,5] 
y=[6,7,8,9,10]
x.extend(y)
print(x)