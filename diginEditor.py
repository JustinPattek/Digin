from diginDeck import *
from diginCard import *
from diginMap import *

newDeck = Deck()
newDeck.shuffleCards()
#newDeck.printDeck()
#print(newDeck.getNumCards())
print("---------------------------------------------------")
newMap = Map(newDeck,6,6)
#newMap.shuffleMap()
print(newMap)
