import math

class Scorecard:
    scores = [{1:0, 2:0, 3:0, 4:0, 5:0, 6:0},
                {'Bonus':0},
                {'3 of a kind':0},
                {'4 of a kind':0},
                {'FullHouse':0},
                {'Small Straight':0},
                {"Large Straight": 0},
                {"Yahtzee!":0},
                {"Y-Bonus":0},
                {"Chance": 0}]

    def __init__(self):
        pass

    def get_scores(self):
        return self.scores

    def add_top(self, row, amount):
        self.scores[0][row] = amount

    def has_bonus(self):
        values = self.scores[0].values()
        total = sum(values)
        if total >= 63:
            self.scores[1] = 35

    def three_of_kind(self, list):
        if list.count(list[0]) >= 3 or list.count(list[1]) >= 3 or list.count(list[2]):
            self.scores[2] = sum(list)
        else:
            self.scores[2] = 0

    def four_of_kind(self, list):
          if list.count(list[0]) >= 4 or list.count(list[1]) >= 4:
              self.scores[3] = sum(list)
          else:
              self.scores[3] = 0

    def full_house(self, zero = False):
          if zero:
            self.scores[4] = 0
          else:
            self.scores[4] = 25
    
    def small_straight(self, list):
        sorted = list.sort().pop(4)
        sorted2 = list.sort().pop(0)
        if sorted == [1,2,3,4] or sorted == [2,3,4,5] or sorted2 == [3,4,5,6]:
            self.scores[5] = 30
        else:
            self.scores[5] = 0
        
    def large_straight(self, list):
        sorted = list.sort()
        if sorted == [2,3,4,5,6] or sorted == [1,2,3,4,5]:
            self.scores[6] = 40
        else:
            self.scores[6] = 0

    def yahtzee(self, list):
         if list.count(list[0]) == 5:
             self.scores[7] = 50
         else:
             self.scores[7] = 0

    def yahtzee_bonus(self):
        self.scores[8] = self.scores[8] + 100
    
    def chance(self, list):
        self.scores[9] = sum(list)


x = Scorecard()
x.add_top(1,3)
x.add_top(2,6)
x.add_top(3,9)
x.add_top(4,12)
x.add_top(5,15)
x.add_top(6,18)

x.has_bonus()