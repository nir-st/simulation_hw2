import Entity
import Position


class Guide(Entity):
    def __init__(self, starting_position, velocity, knows_left_door,knows_right_door):
        super().__init__(starting_position, velocity)
        self.knows_left_door = knows_left_door
        self.knows_right_door = knows_right_door


    def get_direction_to_door(self, room, k):
        curr_possition = self.get_position_at_k(k)
        door_positions = room.get_door_locations()

        if self.knows_left_door and self.knows_right_door:

            if curr_possition.distance_to(door_positions[0]) < curr_possition.distance_to(door_positions[1]):
                return curr_possition.direction_to(door_positions[0])
            return curr_possition.direction_to(door_positions[1])
        elif self.knows_left_door:
            return curr_possition.direction_to(door_positions[0])
        else:
            return curr_possition.direction_to(door_positions[1])


# p = Position(1, 1)
# g = Guide(p, 1, False)
