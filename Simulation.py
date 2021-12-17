class Simulation:
    def __init__(self, room, entities, guides):
        self.room = room
        self.entities = entities
        self.guides = guides
        self.is_simulating = False
        self.current_time = 0

    def run_simulate(self):
        for guide in self.guides:
            guide.find_direction_to_door(self.room)
        while self.current_time < 5000 and (self.guides or self.entities):
            self.run_interval()
            self.current_time = self.current_time + 1

    def run_interval(self):
        self.move_guide()
        # self.move_entities()

    def move_guides(self):
        guides_to_remove = []
        for guide in self.guides:
            desired_location = guide.get_desired_location()
            if self.is_location_available(desired_location, guide):
                guide.set_position_at_k(desired_location)
                if guide.is_at_door(self.room.get_doors_locations()):
                    guides_to_remove.append(guide)
        for guide in guides_to_remove:
            self.guides.remove(guide)

    def is_location_available(self, location, excluded_entity):
        # add walls
        for entity in self.entities:
            if excluded_entity != entity:
                if entity.get_position_at_k(self.current_time).is_inside_position(location, 1):
                    return False
        for guide in self.guides:
            if excluded_entity != guide:
                if guide.get_position_at_k(self.current_time).is_inside_radius(location, 1):
                    return False
        return True
