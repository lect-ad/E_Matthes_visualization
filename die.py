from random import randint


class Die:
    """Represents single die."""

    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        """Returns random int from 1 to number of sides."""
        return randint(1, self.num_sides)