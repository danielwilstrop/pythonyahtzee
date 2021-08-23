from collections import Counter

class Scorecard:
    scores = [{1:0, 2:0, 3:0, 4:0, 5:0, 6:0},
                {'Bonus':0},
                {'3 of a kind':0},
                {'4 of a kind':0},
                {'FullHouse':0},
                {'Small Straight':0},
                {"Large Straight": 0},
                {"Yahtzee!":0},
                {"Chance": 0}]

    def __init__(self):
        pass

    def get_scores(self):
        return self.scores
    
    def get_total_score(self):
        top = sum(self.scores[0].values())
        bottom_list = []
        bottom_list.append(*self.scores[1].values())
        bottom_list.append(*self.scores[2].values())
        bottom_list.append(*self.scores[3].values())
        bottom_list.append(*self.scores[4].values())
        bottom_list.append(*self.scores[5].values())
        bottom_list.append(*self.scores[6].values())
        bottom_list.append(*self.scores[7].values())
        bottom_list.append(*self.scores[8].values())
        return sum(bottom_list) + top

    def add_top(self, row, amount):
        self.scores[0][row] = amount

    def has_bonus(self):
        values = self.scores[0].values()
        total = sum(values)
        if total >= 63:
            self.scores[1] = {'bonus':35}

    def three_of_kind(self, list):
        if list.count(list[0]) >= 3 or list.count(list[1]) >= 3 or list.count(list[2]):
            self.scores[2] = {'3 of a kind':sum(list)}
        else:
            self.scores[2] = {'3 of a kind': 0}

    def four_of_kind(self, list):
          if list.count(list[0]) >= 4 or list.count(list[1]) >= 4:
              self.scores[3] = {'4 of a kind':sum(list)}
          else:
              self.scores[3] = {'3 of a kind': 0}

    def full_house(self, list):
        sorted_list = sorted(list)
        start = sorted_list[0]
        end = sorted_list[4]
        if list.count(start) == 2 and list.count(end) == 3:
            self.scores[4] = {'FullHouse':25}
        elif list.count(start) == 3 and list.count(end) == 2:
            self.scores[4] = {'FullHouse':25}
        else:
            self.scores[4] = {'FullHouse':0}

    def small_straight(self, list):
        smallest_num = min(list)
        if smallest_num + 1 in list and smallest_num + 2 in list and smallest_num +3 in list:
            self.scores[5] = {'Small Straight':30}
        else:
            self.scores[5] = {'Small Straight':0}

    def large_straight(self, list):
        smallest_num = min(list)
        if smallest_num + 1 in list and smallest_num + 2 in list and smallest_num +3 in list and smallest_num + 4 in list:
            self.scores[6] = {'Large Straight':40}
        else:
            self.scores[6] = {'Large Straight':0}

    def yahtzee(self, list):
         if list.count(list[0]) == 5:
             self.scores[7] = {"Yahtzee!":50}
         else:
             self.scores[7] = {"Yahtzee!":0}
    
    def chance(self, list):
        self.scores[8] = {"Chance": sum(list)}


#Tests
three = [6,6,6,3,4]
four = [4,4,4,4,6]
small = [2,3,4,5,4]
large = [1,2,3,4,5]
yat = [2,2,2,2,2]
fh = [3,4,4,3,4]





