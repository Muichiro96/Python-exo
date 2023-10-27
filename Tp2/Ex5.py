List = [1, -30, 0, -2, 50, 4, 2, 100]
val = int(input("Donnez la  valeur a inserer : "))
List.insert(0, val)
List.sort()
for elemnt in List:
    print(elemnt, end="\t")
