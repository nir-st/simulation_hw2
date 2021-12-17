from Entity import Entity


class Guide(Entity):
    def __init__(self, starting_position, velocity, knows_left_door):
        super().__init__(starting_position, velocity)
        self.knows_left_door = knows_left_door
        self.direction_to_door = None

    def get_desired_location(self):
        current_position = self.positions[len(self.positions) - 1]
        distance = self.velocity * 0.02
        return current_position.calc_new_position(self.direction_to_door, distance)

    def find_direction_to_door(self, room):
        curr_position = self.positions[0]
        door_positions = room.get_doors_locations()
        if len(room.get_doors_locations()) == 1:
            direction_to_door = curr_position.direction_to(door_positions[0])
        elif self.knows_left_door:
            if curr_position.distance_to(door_positions[0]) < curr_position.distance_to(door_positions[1]):
                direction_to_door = curr_position.direction_to(door_positions[0])
            else:
                direction_to_door = curr_position.direction_to(door_positions[1])
        else:
            direction_to_door = curr_position.direction_to(door_positions[0])
        self.direction_to_door = direction_to_door
