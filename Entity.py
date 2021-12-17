class Entity:
    def __init__(self, starting_position, velocity):
        self.velocity = velocity
        self.positions = []  # array of positions
        self.positions[0] = starting_position

    def get_desired_location(self, desired_direction):
        current_position = self.locations[len(self.positions) - 1]
        distance = self.velocity * 0.02
        return current_position.move_to(desired_direction, distance)
