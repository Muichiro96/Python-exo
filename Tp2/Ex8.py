List = [1, 2, 5, 8, 6, 2, 5, 9, 1, 8, 8, 9, 9]
indice = []
longueur = len(List)
n = int(input("donnez le nombre :"))
for i in range(longueur):
    if List[i] == n:
        indice.append(i)
print("les indices :")
for e in indice:
    print(e, end=" ")
print("\nnombre d'occurence : \n{}".format(List.count(n)))
