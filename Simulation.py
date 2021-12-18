from Animation import yo
import random
import matplotlib.pyplot as plt


class Simulation:
    def __init__(self, room, entities, guides, visible_distance=20):
        self.room = room
        self.entities = entities
        self.guides = guides
        self.is_simulating = False
        self.current_time = 0  # k
        self.visible_distance = visible_distance
        self.got_out_guides = []
        self.got_out_entities = []

    def run_simulate(self):
        for guide in self.guides:
            guide.find_direction_to_door(self.room)
        while self.current_time < 5000 and (self.guides or self.entities):
            self.run_interval()
            self.current_time = self.current_time + 1
        print(f'finished in {self.current_time * 0.02} seconds')

        yo (self.got_out_guides[0].positions, self.got_out_entities[0].positions)

    def run_interval(self):
        self.move_guides()
        self.move_entities()

    def move_entity_randomly(self, entity):
        random_direction = random.randint(0, 360)
        desired_position = entity.get_desired_location(random_direction)
        while not self.check_valid_position(desired_position):
            random_direction = random.randint(0, 360)
            desired_position = entity.get_desired_location(random_direction)
        return random_direction

    def is_location_available(self, location, excluded_entity):
        # add walls
        for entity in self.entities:
            if excluded_entity != entity:
                if entity.get_position_at_k(self.current_time).is_inside_radius(location, 0.5):
                    return False
        for guide in self.guides:
            if excluded_entity != guide:
                if guide.get_position_at_k(self.current_time).is_inside_radius(location, 0.5):
                    return False
        return True

    def move_guides(self):
        guides_to_remove = []
        for guide in self.guides:
            desired_location = guide.get_desired_location()
            if self.is_location_available(desired_location, guide):
                guide.set_position_at_k(desired_location)
                if guide.is_near_door(self.room.get_doors_locations(), 0.3):
                    guides_to_remove.append(guide)
            else:
                guide.stay_in_place()
        for guide in guides_to_remove:
            self.guides.remove(guide)
            self.got_out_guides.append(guide)

    def check_valid_position(self, position):
        if position.x <= 0 or position.x >= self.room.get_width() or position.y <= 0 or position.y >= self.room.get_length():
            return False
        return True

    def move_entities(self):
        # if close enough to the door, go to it
        # else: if close enough to a guide, go to it (probably will make it stuck because he will
        #                                             stand in the guide's way. maybe if he near
        #                                             a guide he just walks to the door's direction..)
        # else: if close enough to entity, go to it
        # else: random direction
        entities_to_remove = []
        for entity in self.entities:
            if entity.is_near_door(self.room.get_doors_locations(), self.visible_distance):
                desired_direction = entity.get_direction_to_door(self.room)
            else:
                nearest_guide = self.get_nearest_guide(entity)
                if nearest_guide:
                    distance_to_nearest_guide = entity.get_position_at_k(self.current_time).distance_to(nearest_guide.get_position_at_k(self.current_time))
                    if distance_to_nearest_guide < 1:
                        desired_direction = entity.get_direction_to_door(self.room)
                    else:
                        desired_direction = entity.get_position_at_k(self.current_time).direction_to(nearest_guide.get_position_at_k(self.current_time))
                else:
                    nearest_entity = self.get_nearest_entity(entity)
                    if nearest_entity:
                        desired_direction = entity.get_position_at_k(self.current_time).direction_to(nearest_entity.get_position_at_k(self.current_time))
                    else:
                        desired_direction = self.move_entity_randomly(entity)
            desired_location = entity.get_desired_location(desired_direction)
            if self.is_location_available(desired_location, entity):
                entity.set_position_at_k(desired_location)
                if entity.is_near_door(self.room.get_doors_locations(), 0.3):
                    entities_to_remove.append(entity)
            else:
                entity.stay_in_place()
        for entity in entities_to_remove:
            self.entities.remove(entity)
            self.got_out_entities.append(entity)

    def get_nearest_guide(self, entity):
        min_dis = self.room.get_maximum_distance()
        nearest_guide = None
        for guide in self.guides:
            entitys_pos = entity.get_position_at_k(self.current_time)
            guides_pos = guide.get_position_at_k(self.current_time)
            distance = entitys_pos.distance_to(guides_pos)
            if distance < min_dis:
                min_dis = distance
                nearest_guide = guide
        if min_dis <= self.visible_distance:
            return nearest_guide
        return None

    def get_nearest_entity(self, excluded_entity):
        min_dis = self.room.get_maximum_distance()
        nearest_entity = None
        for entity in self.entities:
            if entity != excluded_entity:
                excluded_entitys_pos = excluded_entity.get_position_at_k(self.current_time)
                entitys_pos = entity.get_position_at_k(self.current_time)
                distance = excluded_entitys_pos.distance_to(entity_pos)
                if distance < min_dis:
                    min_dis = distance
                    nearest_entity = entity
        if min_dis <= self.visible_distance:
            return nearest_entity
        return None
