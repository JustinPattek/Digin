from diginDeck import *
from diginMap import *

class Card:

    def __init__(self, name, pickup, equip, special):
        self.__name = name
        self.__pickup = pickup
        self.__equip = equip
        self.__special = special

    def setName(self,name):
        self.__name = name
    def setPickup(self,pickup):
        self.__pickup = pickup
    def setEquip(self,equip):
        self.__equip = equip
    def setSpecial(self,special):
        self.__special = special


    def getName(self):
        return self.__name
    def getPickup(self):
        return self.__pickup
    def getEquip(self):
        return self.__equip
    def getSpecial(self):
        return self.__special
    
