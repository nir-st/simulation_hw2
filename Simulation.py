
class Simulation():
    def __init__(self, room, entities, guides):
        self.room = room
        self.entities = entities
        self.guides = guides
        self.is_simulating = False
        self.current_time = 0

    def run_simulate(self):
        while self.current_time < 5000:
            self.run_interval()
            self.current_time = self.current_time + 1

    def run_interval(self):
        for guide in self.guides:
            self.get_direction_to_door(guide)
            # guide.get_desired_location(room.)


    def get_direction_to_door(self, guide):
        guide_possition = guide.get_position_at_k(self.current_time)
        door_positions = self.room.get_door_locations()
        if guide.knows_one_door:
            door_position = door_positions[0]
        else:
            # if guide_possition.distance_to
            # door_position =








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