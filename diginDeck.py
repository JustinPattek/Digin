import random
from diginCard import *
from diginMap import *

# make two lists one for the amount of each card
# and one for the name of each card
# I can get rid of the for loops and make it only one for loop too
COIN_ONE = 13
COIN_THREE = 5
SWORD = 5
ABILITY = 0
SHOP = 0
SHOVEL = 5
DARK_SHOVEL = 3
WHISKEY = 5
ROCK = 10
PURSE = 5
FROG = 5
DIRT = 20
BOOTS = 3
BOMB = 20


class Deck:
    def __init__(self):
        self.__deck = []

 
        num = 0
        while num<COIN_ONE:
            self.__deck.append(Card("coin_one",0,0,0))
            num+=1
        num = 0
        while num<COIN_THREE:
            self.__deck.append(Card("coin_three",0,0,0))
            num+=1
        num = 0
        while num<SWORD:
            self.__deck.append(Card("sword",0,1,0))
            num+=1

        num = 0
        while num<ABILITY:
            self.__deck.append(Card("ability",0,0,1))
            num+=1

        num = 0
        while num<SHOP:
            self.__deck.append(Card("shop",0,0,1))
            num+=1
        num = 0
        while num<SHOVEL:
            self.__deck.append(Card("shovel",0,1,0))
            num+=1
        num = 0
        while num<DARK_SHOVEL:
            self.__deck.append(Card("dark_shovel",1,1,0))
            num+=1
        num = 0
        while num<WHISKEY:
            self.__deck.append(Card("whiskey",1,1,0))
            num+=1
        num = 0
        while num<ROCK:
            self.__deck.append(Card("rock",1,0,0))
            num+=1

        num = 0
        while num<PURSE:
            self.__deck.append(Card("purse",1,1,0))
            num+=1

        num = 0
        while num<FROG:
            self.__deck.append(Card("frog",1,1,0))
            num+=1
        num = 0
        while num<DIRT:
            self.__deck.append(Card("dirt",0,0,0))
            num+=1

        num = 0
        while num<BOOTS:
            self.__deck.append(Card("boots",0,1,0))
            num+=1

        num = 0
        while num<BOMB:
            self.__deck.append(Card("bomb",1,1,0))
            num+=1
        
      

    def getNumCards(self):
        return len(self.__deck)

    def getDeck(self):
        return self.__deck

    def shuffleCards(self):
        random.shuffle(self.__deck)

    def printDeck(self):
        nameDeck = []
        for card in self.__deck:
            print(card.getName())
            nameDeck.append(card.getName())
        return nameDeck
