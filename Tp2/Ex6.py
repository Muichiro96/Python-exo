List = [1, -30, 1, -2, 50, 1, 2, 100]
n = int(input("donnez un nombre :"))
while n in List:
    List.remove(n)
for el in List:
    print(el,end=" ")
