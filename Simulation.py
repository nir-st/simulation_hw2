# from Animation import yo
import random
import matplotlib.pyplot as plt

from Entity import Entity
from Guide import Guide
from Position import Position
import Animation


class Simulation:

    RADIUS_FROM_DOOR_TO_EXIT = 0.8
    RADIUS_ENTITY_SPOT = 0.3
    MAX_TIME_TO_EVACUATE = 5000

    def __init__(self, room, entities, guides, visible_distance=20):
        self.room = room
        self.entities = entities
        self.guides = guides
        self.is_simulating = False
        self.current_time = 0  # k
        self.visible_distance = visible_distance
        self.got_out_guides = []
        self.got_out_entities = []
        self.end_time = 0

    def add_guides_randomly(self, N, velocity, is_knows_left_door):
        # N = number of guides to add
        for i in range(N):
            X = random.randint(1, 19)
            Y = random.randint(1, 19)
            pos = Position(X, Y)
            attempts = 0
            while not self.is_location_available(pos):
                attempts += 1
                if attempts > 500:
                    raise EnvironmentError("Can't find spots for more guides in the room")
                X = random.randint(1, 19)
                Y = random.randint(1, 19)
                pos.set_vals(X, Y)
            guide = Guide(pos, velocity, is_knows_left_door)
            self.guides.append(guide)

    def add_entities_randomly(self, N, velocity):
        # N = number of entities to add
        for i in range(N):
            X = random.randint(1, 19)
            Y = random.randint(1, 19)
            pos = Position(X, Y)
            attempts = 0
            while not self.is_location_available(pos):
                attempts += 1
                if attempts > 500:
                    raise EnvironmentError("Can't find spots for more entities in the room")
                X = random.randint(1, 19)
                Y = random.randint(1, 19)
                pos.set_vals(X, Y)
            entity = Entity(pos, velocity)
            self.entities.append(entity)

    def run_simulate(self):
        for guide in self.guides:
            guide.find_direction_to_door(self.room)
        while self.current_time < self.MAX_TIME_TO_EVACUATE and (self.guides or self.entities):
            self.run_interval()
            self.current_time = self.current_time + 1
        self.end_time = self.current_time * 0.02

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

    def is_location_available(self, location, excluded_entity=None, entitys_direction=None):
        for entity in self.entities:
            if excluded_entity != entity:
                if entity.get_position_at_k(self.current_time).is_inside_radius(location, self.RADIUS_ENTITY_SPOT):
                    if excluded_entity:
                        angel_to = location.direction_to(excluded_entity.get_position_at_k(self.current_time))
                        angel_diff = abs((entitys_direction - angel_to + 180) % 360 - 180)
                        if entitys_direction and angel_diff > 45:
                            return False
        for guide in self.guides:
            if excluded_entity != guide:
                if guide.get_position_at_k(self.current_time).is_inside_radius(location, self.RADIUS_ENTITY_SPOT):
                    if excluded_entity:
                        angel_to = location.direction_to(excluded_entity.get_position_at_k(self.current_time))
                        angel_diff = abs((entitys_direction - angel_to + 180) % 360 - 180)
                        if entitys_direction and angel_diff > 45:
                            return False
        return True

    def print_stats(self):
        if self.is_room_empty():
            print(f'room was evacuated in {self.end_time} seconds')
        else:
            print(f'Number of guides left in the room: {len(self.guides)}')
            print(f'Number of entities left in the room: {len(self.entities)}')
        print(f'Number of guides got out of the room: {len(self.got_out_guides)}')
        print(f'Number of entities got out of the room: {len(self.got_out_entities)}')

    def is_room_empty(self):
        return len(self.guides) == 0 and len(self.entities) == 0

    def move_guides(self):
        guides_to_remove = []
        for guide in self.guides:
            desired_location = guide.get_desired_location()
            if self.is_location_available(desired_location, guide, guide.direction_to_door):
                guide.set_position_at_k(desired_location)
                if guide.is_near_door(self.room.get_doors_locations(), self.RADIUS_FROM_DOOR_TO_EXIT):
                    guides_to_remove.append(guide)
            else:
                if not self.is_closest_to_door(guide.get_position_at_k(self.current_time)):
                    previous_position = guide.get_previous_position()
                    if self.is_location_available(previous_position):
                        guide.set_position_at_k(previous_position)
                else:
                    guide.stay_in_place()
        for guide in guides_to_remove:
            self.guides.remove(guide)
            self.got_out_guides.append(guide)

    def is_closest_to_door(self, pos):
        dis_to_door = self.room.distance_to_nearest_door(pos)
        for guide in self.guides:
            other_dis_to_door = self.room.distance_to_nearest_door(guide.get_position_at_k(self.current_time))
            if other_dis_to_door < dis_to_door:
                return False
        return True

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
            if self.is_location_available(desired_location, entity, desired_direction):
                entity.set_position_at_k(desired_location)
                if entity.is_near_door(self.room.get_doors_locations(), self.RADIUS_FROM_DOOR_TO_EXIT):
                    entities_to_remove.append(entity)
            else:
                if not self.is_closest_to_door(entity.get_position_at_k(self.current_time)):
                    previous_position = entity.get_previous_position()
                    if self.is_location_available(previous_position):
                        entity.set_position_at_k(previous_position)
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
                distance = excluded_entitys_pos.distance_to(entitys_pos)
                if distance < min_dis:
                    min_dis = distance
                    nearest_entity = entity
        if min_dis <= self.visible_distance:
            return nearest_entity
        return None

    def animate(self):
        all_guides_positions = [g.positions for g in self.guides] + [g.positions for g in self.got_out_guides]
        all_entities_positions = [e.positions for e in self.entities] + [e.positions for e in self.got_out_entities]
        Animation.animate(all_guides_positions, all_entities_positions)
