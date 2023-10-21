x, y = input("donnez deux nombres :").split()
oper = input("donnez l'operation :")
if oper == '+':
    res = float(x) + float(y)
    print("resultat ", res)
elif oper == '-':
    res = float(x) - float(y)
    print("resultat ", res)
elif oper == '*':
    res = float(x) * float(y)
    print("resultat ", res)
elif oper == '/':
    res = float(x) / float(y)
    print("resultat ", res)
else:
    print("operation non valide")