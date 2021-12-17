import math


class Position:
    def _init_(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, other_position):
        return math.sqrt(math.pow(self.x - other_position.x, 2) + math.pow(self.y - other_position.y, 2))
