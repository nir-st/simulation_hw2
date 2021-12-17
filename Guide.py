import Entity


class Guide(Entity):
    def __init__(self, starting_position, velocity, knows_left_door):
        super().__init__(starting_position, velocity)
        self.knows_left_door = knows_left_door
        self.direction_to_door = None

    def get_direction_to_door(self, room, k):
        curr_position = self.get_positions[0]
        door_positions = room.get_door_locations()
        if self.knows_left_door:
            if curr_position.distance_to(door_positions[0]) < curr_position.distance_to(door_positions[1]):
                direction_to_door = curr_position.direction_to(door_positions[0])
            else:
                direction_to_door = curr_position.direction_to(door_positions[1])
        else:
            direction_to_door = curr_position.direction_to(door_positions[0])
        self.direction_to_door = direction_to_door
