nbra = int(input("nombre articles :"))
prix = 0
if nbra <= 2:
    for i in range(nbra):
        noma = input(f"Nom article{i + 1} :")
        qu = int(input(f"la quantite d'article{i + 1} :"))
        pru = float(input(f"le prix unitaire d'article{i + 1} :"))
        prix += qu * pru
        print("totale d'article", noma, " :", qu * pru)
montant = prix * 0.2 + prix
print("totale de votre facture ", montant)
