import math


class Room:
    def __init__(self, width, length, doors_locations):
        self.width = width
        self.length = length
        self.doors_locations = doors_locations

    def get_doors_locations(self):
        return self.doors_locations

    def get_length(self):
        return self.length

    def get_width(self):
        return self.width

    def get_maximum_distance():
        return math.sqrt(math.pow(selfwidth(), 2) + math.pow(self.width, 2))