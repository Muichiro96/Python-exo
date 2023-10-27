somme = 0
note = 0
for i in range(0, 4):
    x, y = input("note et coefficient ").split()
    somme += int(y)
    note += float(x) * int(y)
res = note / somme
print(res)
if res >= 10:
    print("semestre valide")
elif res >= 7:
    print("rattrappage")
else:
    print("non valide")