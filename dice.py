import random

class Dice():
    display = [None,"""
    +--------+
    |        |
    |    O   |
    |        |
    +--------+
    """,
    """
    +--------+
    |      O |
    |        |
    | O      |
    +--------+
    """,
      """
    +--------+
    |      O |
    |    O   |
    | O      |
    +--------+
    """,
       """
    +--------+
    | O    O |
    |        |
    | O    O |
    +--------+
    """,
       """
    +--------+
    | O    O |
    |    O   |
    | O    O |
    +--------+
    """,
       """
    +--------+
    | O    O |
    | O    O |
    | O    O |
    +--------+
    """]
    
    def __init__(self):
        pass
    
    #Random dice roll from 1-6
    def roll():
        return random.randint(1, 6)

    def print_dice(self,index):
        return self.display[index]
    

    


