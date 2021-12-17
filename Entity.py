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

    def get_direction_to_door(self, room, k):
        curr_position = self.get_position_at_k(k)
        door_positions = room.get_door_locations()
        if curr_position.distance_to(door_positions[0]) < curr_position.distance_to(door_positions[1]):
            return curr_position.direction_to(door_positions[0])
        return curr_position.direction_to(door_positions[1])

    def is_at_door(self,doors):
        last= len(self.positions)-1
        curr_pos = self.get_position_at_k(self.positions[last])
        for door in doors:
            if door.distance_to(curr_pos)==0.0:
                return True
        return False


