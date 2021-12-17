import math


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, other_position):
        return math.sqrt(math.pow(self.x - other_position.x, 2) + math.pow(self.y - other_position.y, 2))

    def direction_to(self, other_position):
        # returns degree
        deltaX = other_position.x - self.x
        deltaY = other_position.y - self.y
        return math.atan2(deltaY, deltaX) * 180 / math.pi

    def calc_new_position(self, direction, distance):
        new_x = self.x + distance * math.cos(direction * math.pi / 180)
        new_y = self.y + distance * math.sin(direction * math.pi / 180)
        return Position(new_x, new_y)

    def is_inside_radius(self, other_position, radius):
        return (math.pow((self.x - other_position.x), 2)) + (math.pow((self.y - other_position.y), 2)) < math.pow(radius, 2)

    def __repr__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
