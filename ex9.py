taille = float(input("Donnez la taille :"))
Poids = float(input("Donnez le poids"))
IMC = Poids / taille * 2
if IMC < 16.5:
    print("Famine")
elif IMC < 8.5:
    print("Maigreur")
elif IMC < 25:
    print("corpulence normale")
elif IMC < 30:
    print("Surpoids")
elif IMC < 35:
    print("obesite moderee")
elif IMC < 40:
    print("obesite severe")
else:
    print("obesite morbide ou massive")
