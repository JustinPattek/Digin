import random
import numpy as np
from diginDeck import *
from diginCard import *






class Map:
    def __init__(self,newDeck,width,height):
        self.card_map = []
        for _ in range(height):
            self.card_map.append([])
            for _ in range(width):
                card = newDeck.getDeck().pop()
                self.card_map[-1].append(card)
            
        

    def getMap(self):
        return self.card_map
    
    def shuffleMap(self):
        random.shuffle(self.card_map)
    
    def __str__(self):
        s='\n'.join(['\t'.join([str(item.getName()) for item in row]) for row in self.card_map])
        return s + '\n'
