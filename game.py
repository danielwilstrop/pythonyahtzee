from dice import Dice
from player import Player
from scorecard import Scorecard
dice = Dice()

class Game:
    players = 0
    player_list = []
    current_player  = None

    def __init__(self):
        pass
    
    def main(self):
        print("Welcome to terminal Yahtzee! Written in python, by Dan Wilstrop!")

        while self.players < 1 or self.players > 4:
            print("How many players are there going to be? (1-4)")
            self.players = int(input())
        print(f"Great theres going to be {self.players} players")

        for i in range(int(self.players)):
            print(f"Please enter the name of player {i + 1}")
            self.add_player(input())
        self.current_player = self.player_list[0]
        self.play_game()
            
    def add_player(self, name):
        self.player_list.append(Player(name))

    def next_player(self):
        index = self.player_list.index(self.current_player)
        if index + 1 < len(self.player_list):
            self.current_player = self.player_list[index + 1]
        else:
            self.current_player = self.player_list[0]

    def play_game(self):
        print("Lets play Yahtzee!")

   
# game = Game()
# game.main()

# score = Scorecard()
# print(score.get_scores())

x = [1,2,1,1,1,]

print(x.count(1))





