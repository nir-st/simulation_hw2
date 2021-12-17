class Simulation():
    def __init__(self, room, entities, guides):
        self.room = room
        self.entities = entities
        self.guides = guides
        self.is_simulating = False
        self.current_time = 0

    def run_simulate(self):
        for guide in self.guides:
            guide.find_direction_to_door(self.room)
        while self.current_time < 50000 and (self.guides or self.entities):
            self.run_interval()
            self.current_time = self.current_time + 1
        print(self.guides[0].positions)

    def run_interval(self):
        guides_to_remove = []
        for guide in self.guides:
            desired_location = guide.get_desired_location()
            if (self.is_location_available(desired_location, guide)):
                guide.set_position_at_k(desired_location)
                if guide.is_at_door(self.room.get_doors_locations()):
                    print("the guide is out")
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

    def check_valid_move(self, position):
        if position.x<=0 or position.x>= self.room.get_width() or position.y<=0 or position.y>=self.room.get_length():
            return False
        return True









# funciton move():
# 		while not has_finished:
#
# 			exited_guides = []
# 			exited_entites = []
#
# 			for guide in guides_in_room:
# 				preferred_direction = get_direction_to_door(guide.get_location(), guide.is_know_about_left_door)
# 				desired_location = guide.get_desired_location(preferred_direction)
# 				if not is_occupied(desired_location):
# 					guide.move(desired_location)
# 				if has_exited(guide):
# 					exited_guides.add(guide)
#
# 			for entity in entities_in_room:
# 				preferred_direction = entity.get_previous_direction()
# 				if is_near_door(entity):
# 					preferred_direction = get_direction_to_door(entity.get_location())
# 				elif len(guides_in_room) > 0:
# 					preferred_direction = get_directino_to_nearest_guide(entity)
# 				desired_location = entity.get_desired_location(preferred_location)
# 				if not is_ocupied(desired_location):
# 					entity.move(desired_location)
# 				is has_exited(guide):
# 					exited_entities.add(guide)
#
# 				for guide in exited_guides:
# 					guides_in_room.remove(guide)
#
# 				for entity in exited_entities:
# 					entities_in_room.remove(entity)
# class Simulation: