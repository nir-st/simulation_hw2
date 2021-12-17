import matplotlib.pyplot as plt


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

    def set_position_at_k(self, position):
        self.positions.append(position)

    def get_direction_to_door(self, room):
        curr_position = self.positions[len(self.positions) - 1]
        door_positions = room.get_doors_locations()
        if len(room.get_doors_locations()) == 1:
            return curr_position.direction_to(door_positions[0])
        else:
            if curr_position.distance_to(door_positions[0]) < curr_position.distance_to(door_positions[1]):
                return curr_position.direction_to(door_positions[0])
            return curr_position.direction_to(door_positions[1])

    def is_near_door(self, door_positions, radius):
        last = len(self.positions) - 1
        curr_pos = self.get_position_at_k(last)
        for door_position in door_positions:
            if curr_pos.is_inside_radius(door_position, radius):
                return True
        return False

    def exit(self):
        self.plot_route()
        print(f'exiting. time: {(len(self.positions) - 1) * 0.02}. location: {self.positions[len(self.positions) - 1]}.')

    def plot_route(self):
        x = []
        y = []
        for pos in self.positions:
            x.append(pos.x)
            y.append(pos.y)
        plt.scatter(x, y)
        plt.xlim([0, 20])
        plt.ylim([0, 20])
        plt.show()
