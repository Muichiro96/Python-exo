import math


def somme(a, b):
    s = 0
    if b > a:

        for i in range(a, b + 1):
            s += i
        return s
    else:
        return 0


def delta(a, b, c):
    return b * b - 4 * a * c


def NombreRacine(a, b, c):
    if delta(a, b, c) > 0:
        return 2
    elif delta(a, b, c) == 0:
        return 1
    else:
        return 0


def AfficheNombreRacine(a, b, c):
    print("Nombre de racines : {}".format(NombreRacine(a, b, c)))


def Racine1(a, b, c):
    return -b - math.sqrt(delta(a, b, c)) / 2 * a


def Racine2(a, b, c):
    return -b + math.sqrt(delta(a, b, c)) / 2 * a


def converstion_temps(h, m, s):
    return s + m * 60 + h * 3600


def temps_ecoule():
    print("svp donnez l horaire sous forme hh:mm:ss ")
    h1, m1, s1 = input("Donnez l'horaire 1 : ").split(sep=":")
    s1 = converstion_temps(int(h1), int(m1), int(s1))
    h2, m2, s2 = input("Donnez l'horaire 2 : ").split(sep=":")
    s2 = converstion_temps(int(h2), int(m2), int(s2))
    if s1 > s2:
        s = s1 - s2
    else:
        s = s2 - s1

    print(s)


def conversion_distance(km, m, cm):
    v1 = km / 1000
    v2 = cm / 100
    distance = v1 + m + v2
    return distance


def vitesse(Km, m, cm, h, min, s):
    d = conversion_distance(Km, m, cm)
    t = converstion_temps(h, min, s)
    return d / t


temps_ecoule()
