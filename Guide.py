import Entity
import Position


class Guide(Entity):
    def __init__(self, starting_position, velocity, is_know_left_door):
        super().__init__(starting_position, velocity)
        self.is_know_left_door = is_know_left_door


# p = Position(1, 1)
# g = Guide(p, 1, False)
