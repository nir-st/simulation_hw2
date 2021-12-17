import math


class Room:
    def __init__(self, width, length, doors_locations):
        self.width = width
        self.length = length
        self.doors_locations = doors_locations
        self.maximum_distance = math.sqrt(math.pow(length, 2) + math.pow(width, 2))

    def get_doors_locations(self):
        return self.doors_locations

    def get_length(self):
        return self.length

    def get_width(self):
        return self.width

    def get_maximum_distance(self):
        return self.maximum_distance