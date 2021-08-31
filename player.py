from dice import Dice
from scorecard import Scorecard
import time
dice = Dice()

class Player:
    name = ''
    roll = 1
    dice = []
    chosen_dice = []
    score = Scorecard()
    
    def __init__(self, name):
        self.name = name

    def take_turn(self):
        if self.roll == 3:
            self.take_roll()
            self.add_to_score()
        elif self.roll == 1 or self.roll == 2:
            self.take_roll()
            self.choose_dice()

    def next_turn(self):
        self.dice = []
        self.choosen_dice = []
        self.roll = 1
    
    def next_roll(self):
        if self.roll < 5:
            self.roll = self.roll +1
            self.take_turn()
        else:
            self.roll = 1
            
    def take_roll(self):
        print("Rolling dice...")
        time.sleep(0.8)
        print("Your dice are...")
        for i in range(5 - len(self.dice)):
           self.dice.append(Dice.roll())
        print(self.dice)
        
    def choose_dice(self): 
        self.chosen_dice = []
        for i in range(len(self.dice)):
            print("Would you lime to keep dice 1? Its a " + str(self.dice[i]) + " Y/N")
            choice = input().lower()
            if choice == 'y':
                self.chosen_dice.append(self.dice[i])
        self.dice = self.chosen_dice
        self.next_roll()

    def get_score(self):
        self.score.has_bonus()
        return self.score.get_total_score()

    def add_to_score(self):
        print("Where would you like to put this turns score?")
        print("Select carefully as if you dont have the correct dice your score will be marked as a zero!")
        print("Please choose from Ones, Twos, Threes, Fours, Fives, Sixes, 3K(3 of a kind), 4K(4 of a kind), FH(Full House), SS(small straight), LS(Large Straight), Y(Yahtzee), C(Chance)")
        choice = input().lower()
        if choice == 'ones':
            ones = self.dice.count(1) 
            self.score.add_top(0, ones)
        elif choice == 'twos':
            twos = self.dice.count(2) * 2
            self.score.add_top(1, twos)
        elif choice == 'threes':
            threes = self.dice.count(3) * 3
            self.score.add_top(2, threes)
        elif choice == 'fours':
            fours = self.dice.count(4) * 4
            self.score.add_top(3, fours)
        elif choice == 'fives':
            fives = self.dice.count(5) * 5
            self.score.add_top(4, fives)
        elif choice == 'sixes':
            sixes = self.dice.count(6) * 6
            self.score.add_top(5, sixes)
        elif choice == '3k':
            self.score.three_of_kind(self.dice)
        elif choice == '4k':
            self.score.four_of_kind(self.dice)
        elif choice == 'fh':
            self.score.full_house(self.dice)
        elif choice == 'ss':
            self.score.small_straight(self.dice)
        elif choice == 'ls':
            self.score.large_straight(self.dice)
        elif choice == 'y':
            self.score.yahtzee(self.dice)
        elif choice == 'c':
            self.score.chance(self.dice)
        else:
            print("Unrecongnised repsonse")
            self.add_to_score()
        self.next_turn()




        
        

