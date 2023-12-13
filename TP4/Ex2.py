class Batiment:
    def __init__(self, adress):
        self.__adresse = adress

    def getAdresse(self):
        return self.__adresse

    def setAdress(self, a):
        self.__adresse = a

    def __str__(self):
        return "L'adresse de batiment : {}".format(self.__adresse)


class Maison(Batiment):
    def __init__(self, adress, nbr):
        super().__init__(adress)
        self.__nbrPieces = nbr

    def getNbr(self):
        return self.__nbrPieces

    def setNbr(self, nombre):
        self.__nbrPieces = nombre

    def __str__(self):
        return super().__str__()+"    Le nombre de pieces de la maison est : {}".format(self.__nbrPieces)


class Immeuble(Batiment):
    def __init__(self, adress, nbr):
        super().__init__(adress)
        self.__nbAppart = nbr

    def setNbAppart(self, nbr):
        self.__nbAppart = nbr

    def getNbApprt(self):
        return self.__nbAppart

    def __str__(self):
        return super().__str__() + "  Le nombre d'appartement de l'imeuble : {}".format(self.__nbAppart)


a = Batiment("Residence al wahda Dcheira")
b= Maison("Agdal Bloc B No 64",15)
c=Immeuble("Inezgane Bloc C No 5",25)
print(a.__str__())
print(b.__str__())
print(c.__str__())