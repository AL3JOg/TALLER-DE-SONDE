def producto_escalar(u, v):
   for i in u:
         u[i+1] * v[i+1]
         return sum(u)
   
u = (1, 2, 3)
v = (4, 5, 6)

print(producto_escalar(u, v))
