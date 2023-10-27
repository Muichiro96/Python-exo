import random

n = random.randint(0, 100)

for i in range(7):
    nombre = int(input("Essayer de deviner le nombre entre 0 et 100  :"))
    if nombre>100 or nombre<0:
        print("le nombre est hors d'intervalle")
    elif nombre>n:
        print("plus grand")
    elif nombre<n:
        print("plus petit")
    elif nombre==n:
        print("Bravo,c'est le nombre !!?  :)")
        break
