d = int(input("donnez un nombre en seconde"))
h = int(d / 3600)
c = d % 3600
m = int(c / 60)
s = c % 60
print("l'heure est", h, "h", m, "min", s, "sec")