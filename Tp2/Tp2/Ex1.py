n = input("donnez un chiffre :")
somme = 0
for i in range(0, 4):
    somme += int(n * (i + 1))
print(somme)
