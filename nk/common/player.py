"""
Player class
"""


class Player:

    def __init__(self, name='new player'):
        self.name = name

    def set_name(self):
        """
        Sets name of player by prompting.
        """
        name = input('Plase enter a name of yours\n')
        self.name = name
