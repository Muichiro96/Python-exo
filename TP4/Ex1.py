class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def getX(self):
        return self.__x

    def setX(self, abs):
        self.__x = abs

    def getY(self):
        return self.__y

    def setY(self, cord):
        self.__y = cord

    def __str__(self):
        return "l'abssice du point x : {}\nl'ordonee du point y : {}".format(self.__x, self.__y)


a = Point(1, 2)
print(a.__str__())


class Rectangle(Point):
    def __init__(self, abs, cord, largeur, longueur):
        super().__init__(abs, cord)
        self.__largeur = largeur
        self.__longueur = longueur

    def getLargeur(self):
        return self.__largeur

    def setLargeur(self, la):
        self.__largeur = la

    def getLongueur(self):
        return self.__longueur

    def setLongueur(self, lo):
        self.__longueur = lo

    def aire(self):
        return self.__longueur * self.__largeur

    def __str__(self):
        return super().__str__() + "\nla largeur est :{}".format(self.__largeur) + "\nla longueur est : {}".format(
            self.__longueur)


r = Rectangle(1, 3, 3, 4)
print(r.__str__())


class Parallelepipede(Rectangle):
    def __init__(self, abs, cord, larg, long, haut):
        super().__init__(abs, cord, larg, long)
        self.__hauteur = haut

    def getHauteur(self):
        return self.__hauteur

    def setHauteur(self, h):
        self.__hauteur = h

    def aire(self):
        return 2 * self.__hauteur * self.getLargeur() + 2 * self.getLongueur() * self.getLargeur() + 2 * self.getLongueur() * self.__hauteur

    def volume(self):
        return self.__hauteur * self.getLargeur() * self.getLongueur()

    def __str__(self):
        return super().__str__() + "la hauteur est {}".format(self.__hauteur)
