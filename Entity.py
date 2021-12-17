class Entity:
    def __init__(self, starting_position, velocity):
        self.velocity = velocity
        self.positions = []  # array of positions
        self.positions.append(starting_position)

    def get_desired_location(self, desired_direction):
        current_position = self.positions[len(self.positions) - 1]
        distance = self.velocity * 0.02
        return current_position.calc_new_position(desired_direction, distance)

    def get_position_at_k(self, k):
        return self.positions[k]

    def set_position_at_k(self, k, position):
        self.positions[k] = position
