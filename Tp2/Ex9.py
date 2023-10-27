tc = input("convertion d' Euro en dh (mad) saisir ED / de Dh en Euro saisir DE : ")
while (tc != "ED" and tc != "DE"):
    tc = input("convertion d' Euro en dh (mad) saisir ED / de Dh en Euro saisir DE : ")
v = float(input("donnez la premiere valeur :"))
liste = []
while v > 0:
    if tc == "ED":
        liste.append(v * 10.86)
    else:
        liste.append(v / 10.86)
    v = float(input("donnez une autre  valeur :"))

for element in liste:
    print(element,end=" ")