
#!/usr/bin/python3
"""
Defines a class
"""

class MyClass:
    """
    Define a class
    """
    def __init__(self, name, number = 4):
        self.__name = name
        self.number = number
        self.is_team_red = (self.number % 2) == 0

    def win(self):
        self.score += 1

    def lose(Self):
        self.score -= 1

    def __str__(self):
        return "[Myclass] {} - {:d} => {:d}".format(self.__name, self.number, self.score)
