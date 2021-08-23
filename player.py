from dice import Dice
from scorecard import Scorecard

class Player:
    name = ''
    roll = 1
    dice = []
    chosen_dice = []
    score = Scorecard()
    
    def __init__(self, name):
        self.name = name

    def take_turn(self):
        if self.roll <= 4:
            self.take_roll()

    def next_turn(self):
        self.dice = []
            
    def next_roll(self):
        if self.roll == 3:
            self.roll = 1
        else:
            self.roll = self.roll + 1

    def take_roll(self):
        for i in range(5 - len(self.dice)):
           self.dice.append(Dice.roll())
        self.next_roll()

    def choose_dice(self, array):
        self.chosen_dice = []
        for i in range(len(self.dice)):
            if array[i] == 'y':
                self.chosen_dice.append(self.dice[i])
        self.dice = self.chosen_dice 



            

#roll dice 
#choose dice to keep
#roll dice 
#choose dice to keep
#roll dice 
#add dice to scorecard

#next player 
        

