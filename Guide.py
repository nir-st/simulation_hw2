class Guide(Entity):
    def __init__(self, starting_position, velocity, is_know_left_door):
        super().__init__(starting_position, velocity)
        self.is_know_left_door = is_know_left_door
