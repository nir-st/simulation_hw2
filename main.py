from Room import Room
from Simulation import Simulation
from Guide import Guide
from Entity import Entity
from Position import Position
import random
import numpy as np
import matplotlib.pyplot as plt
from itertools import combinations


# -------------------------------------------------------------------------- #
#                                     Q1a                                    #
# -------------------------------------------------------------------------- #
def q1a():
    room = Room(20, 20, [Position(20, 10)])
    guide = Guide(Position(10, 10), 1.5, False)
    entities = []
    guides = [guide]
    simulation = Simulation(room, entities, guides)
    simulation.run_simulate()
    simulation.print_stats()
    simulation.draw_routes()


# -------------------------------------------------------------------------- #
#                                     Q1b+Q1c                                    #
# -------------------------------------------------------------------------- #
def q1b_c():
    room = Room(20, 20, [Position(20, 10)])
    simulations_end_times =[]
    guides_after_sim = []
    max_time_to_evacuate = 0
    max_guide_steps = 0
    for i in range(200):
        guides_x_position = random.randint(0, 20)
        guides_y_position = random.randint(0, 20)
        guide = Guide(Position(guides_x_position, guides_y_position), 1.5, True)
        entities = []
        guides = [guide]
        simulation = Simulation(room, entities, guides)
        simulation.run_simulate()
        simulations_end_times.append(simulation.end_time)
        guides_after_sim.append(guide)
        if simulation.end_time > max_time_to_evacuate:
            max_time_to_evacuate = simulation.end_time
        if len(guide.positions) > max_guide_steps:
            max_guide_steps = len(guide.positions)

    plt.title("Time to evacuate")
    plt.xlabel("Time in seconds")
    plt.ylabel("Number of events")
    plt.hist(simulations_end_times, bins=8)
    print(f'Maximum finish time {max_time_to_evacuate} seconds')
    print(f'Average time to evacuate was {sum(simulations_end_times) / 200} seconds')
    plt.show()

    # ---------Q1c---------- #

    collusion_count = 0
    for i in range(0, max_guide_steps):
        current_step = []
        for guide in guides_after_sim:
            if i < len(guide.positions)-1:
                current_step.append(guide.positions[i])
        positions_combinations = list(combinations(current_step, 2))
        for positions_pair in positions_combinations:
            distance_between_points = positions_pair[0].distance_to(positions_pair[1])
            if distance_between_points != 0 and distance_between_points < 0.5:
                collusion_count += 1
    print(collusion_count)


# -------------------------------------------------------------------------- #
#                                     Q2a                                    #
# -------------------------------------------------------------------------- #
def q2a():
    # num_of_guides = [20, 50, 100, 200]
    num_of_guides = [50]
    room = Room(20, 20, [Position(20, 10)])
    for N in num_of_guides:
        simulation = Simulation(room, [], [])
        simulation.add_guides_randomly(N, 1.5, True)
        simulation.run_simulate()
        print(f'\nInitial number of guides: {N}')
        simulation.print_stats()
        simulation.animate()


# -------------------------------------------------------------------------- #
#                                     Q2b                                    #
# -------------------------------------------------------------------------- #
def q2b():
    num_of_guides = [10, 50, 100, 200, 300]
    room = Room(20, 20, [Position(20, 10)])
    end_times = []

    for N in num_of_guides:
        simulation = Simulation(room, [], [])
        simulation.add_guides_randomly(N, 1.5, False)
        simulation.run_simulate()
        # simulation.animate()
        print(f'finished simulation of of {N} guides. Evacuation time: {simulation.end_time}')
        end_times.append(simulation.end_time)

    plt.plot(num_of_guides, end_times)
    plt.title('Time to evacuate based on the number of guides')
    plt.ylabel('time to evacuate in seconds')
    plt.xlabel('number of guides in the room')
    plt.show()


# -------------------------------------------------------------------------- #
#                                     Q2c                                    #
# -------------------------------------------------------------------------- #
def q2c():
    num_of_guides = [10, 50, 100, 150, 200, 250, 300]
    room = Room(20, 20, [Position(20, 10)])
    end_times = []

    for N in num_of_guides:
        simulation = Simulation(room, [], [])
        simulation.add_guides_randomly(round((N/3) * 2), 1.5, False)
        simulation.add_guides_randomly(round(N/3), 0.5, False)
        simulation.run_simulate()
        print(f'finished simulation of of {N} guides. Evacuation time: {simulation.end_time}')
        end_times.append(simulation.end_time)

    plt.plot(num_of_guides, end_times)
    plt.title('Time to evacuate based on the number of guides (with 30% slower entities)')
    plt.ylabel('time to evacuate in seconds')
    plt.xlabel('number of guides in the room')
    plt.plot(num_of_guides, end_times)
    plt.show()
# -------------------------------------------------------------------------- #
#                                     Q3                                  #
# -------------------------------------------------------------------------- #

def q3a():
    num_of_guides = [10, 50, 100, 150, 200, 250, 300]
    room = Room(20, 20, [Position(0, 10),Position(20, 10)])
    end_times = []

    for N in num_of_guides:
        simulation = Simulation(room, [], [])
        simulation.add_guides_randomly(round(N / 2), 1.5, True)
        simulation.add_guides_randomly(round(N / 2), 1.5, False)
        simulation.run_simulate()
        print(f'finished simulation of of {N} guides. Evacuation time: {simulation.end_time}')
        end_times.append(simulation.end_time)

    plt.plot(num_of_guides, end_times)
    plt.title('Time to evacuate based on the number of guides and two doors')
    plt.ylabel('time to evacuate in seconds')
    plt.xlabel('number of guides in the room')
    plt.plot(num_of_guides, end_times)
    plt.show()

def q3b():
    num_of_guides = [10, 50, 100, 150, 200, 250, 300]
    room = Room(20, 20, [Position(0, 10),Position(20, 10)])
    end_times = []

    for N in num_of_guides:
        simulation = Simulation(room, [], [])
        simulation.add_guides_randomly(N, 1.5, True)
        simulation.run_simulate()
        print(f'finished simulation of of {N} guides. Evacuation time: {simulation.end_time}')
        end_times.append(simulation.end_time)

    plt.plot(num_of_guides, end_times)
    plt.title('Time to evacuate based on the half number of guides knows two doors')
    plt.ylabel('time to evacuate in seconds')
    plt.xlabel('number of guides in the room')
    plt.plot(num_of_guides, end_times)
    plt.show()



# -------------------------------------------------------------------------- #
#                                     Q4                                 #
# -------------------------------------------------------------------------- #


def q4a():
    num_of_guides = [(1,50), (5,100), (10,200), (15,300)]
    room = Room(20, 20, [Position(0, 10),Position(20, 10)])
    end_times = []
    num_of_g_e = []
    survivors=[]

    for N in num_of_guides:
        simulation = Simulation(room, [], [])
        num_of_g_e.append(str(N))
        simulation.add_guides_randomly( N[0], 0.75, True)
        simulation.add_entities_randomly(N[1], 0.75)

        simulation.run_simulate()
        survivors.append(N[1]+N[0]-simulation.stayed_in_room())
        end_times.append(simulation.end_time)




    plt.plot(num_of_g_e, survivors,'-ok')
    plt.title('Evacuation based on the guides (5%) knows two doors and entities that follow what they see in 4 meters')
    plt.ylabel('number of survivors')
    plt.xlabel('number of guides, entities in the room')
    plt.plot(num_of_g_e, survivors, '-ok')
    plt.show()

# -------------------------------------------------------------------------- #

def q4b():
    num_of_guides = [(5,50), (10,100), (20,200), (30,300)]
    room = Room(20, 20, [Position(0, 10),Position(20, 10)])
    end_times = []
    num_of_g_e = []
    survivors=[]

    for N in num_of_guides:
        simulation = Simulation(room, [], [])
        num_of_g_e.append(str(N))
        simulation.add_guides_randomly( N[0], 0.75, True)
        simulation.add_entities_randomly(N[1], 0.75)

        simulation.run_simulate()
        survivors.append(N[1]+N[0]-simulation.stayed_in_room())
        end_times.append(simulation.end_time)




    plt.plot(num_of_g_e, survivors,'-ok')
    plt.title('Evacuation based on the guides (10%) knows two doors and entities that follow what they see in 4 meters')
    plt.ylabel('number of survivors')
    plt.xlabel('number of guides, entities in the room')
    plt.plot(num_of_g_e, survivors, '-ok')
    plt.show()



# -------------------------------------------------------------------------- #

def q4c():
    num_of_guides = [(0, 50), (0, 100), (0, 200), (0, 300)]
    room = Room(20, 20, [Position(0, 10), Position(20, 10)])
    end_times = []
    num_of_g_e = []
    survivors = []

    for N in num_of_guides:
        simulation = Simulation(room, [], [])
        num_of_g_e.append(str(N))
        simulation.add_guides_randomly(N[0], 0.75, True)
        simulation.add_entities_randomly(N[1], 0.75)

        simulation.run_simulate()
        survivors.append(N[1] + N[0] - simulation.stayed_in_room())
        end_times.append(simulation.end_time)

    plt.plot(num_of_g_e, survivors, '-ok')
    plt.title('Evacuation based on the guides (0%) knows two doors and entities that follow what they see in 4 meters')
    plt.ylabel('number of survivors')
    plt.xlabel('number of guides, entities in the room')
    plt.plot(num_of_g_e, survivors, '-ok')
    plt.show()


# -------------------------------------------------------------------------- #
#                                     Q5                                    #
# -------------------------------------------------------------------------- #
def q5_1door():
    vision = 3
    num_entities = 50
    room = Room(20, 20, [Position(20, 10)])

    num_of_iterations = 3
    times = {
        'case1': [],
        'case2': [],
        'case3': [],
        'case4': []
    }

    # CASE 1: one guides at the center of the room
    for i in range(num_of_iterations):
        case1_guide1 = Guide(Position(10, 10), 1.5, False)

        simulation = Simulation(room, [], [case1_guide1], vision)
        simulation.add_entities_randomly(num_entities, 1.5)
        simulation.run_simulate()
        times['case1'].append(simulation.end_time)
        # simulation.animate()
        print(f'finished iteration {i} of case 1')

    # CASE 2: one guide at the center of the wall opposite the door
    for i in range(num_of_iterations):
        case2_guide1 = Guide(Position(0.5, 10), 1.5, False)

        simulation = Simulation(room, [], [case2_guide1], vision)
        simulation.add_entities_randomly(num_entities, 1.5)
        simulation.run_simulate()
        times['case2'].append(simulation.end_time)
        # simulation.animate()
        print(f'finished iteration {i} of case 2')

    # CASE 3: two guides standing each at the center of the top and bottom wall
    for i in range(num_of_iterations):
        case3_guide1 = Guide(Position(10, 19.5), 1.5, True)
        case3_guide2 = Guide(Position(10, 0.5), 1.5, True)

        simulation = Simulation(room, [], [case3_guide1, case3_guide2], vision)
        simulation.add_entities_randomly(num_entities, 1.5)
        simulation.run_simulate()
        times['case3'].append(simulation.end_time)
        # simulation.animate()
        print(f'finished iteration {i} of case 3')

    # CASE 4: two guides standing at the corners far from the door
    for i in range(num_of_iterations):
        case4_guide1 = Guide(Position(0.5, 19.5), 1.5, True)
        case4_guide2 = Guide(Position(0.5, 0.5), 1.5, True)

        simulation = Simulation(room, [], [case4_guide1, case4_guide2], vision)
        simulation.add_entities_randomly(num_entities, 1.5)
        simulation.run_simulate()
        times['case4'].append(simulation.end_time)
        # simulation.animate()
        print(f'finished iteration {i} of case 4')

    print('Evacuation time average:')
    print(f'CASE I: {sum(times["case1"]) / num_of_iterations}')
    print(f'CASE II: {sum(times["case2"]) / num_of_iterations}')
    print(f'CASE III: {sum(times["case3"]) / num_of_iterations}')
    print(f'CASE IV: {sum(times["case4"]) / num_of_iterations}')



def q5_2doors():
    vision = 5
    num_entities = 75
    room = Room(20, 20, [Position(20, 10), Position(0, 10)])

    num_of_iterations = 5
    times = {
        'case1': [],
        'case2': [],
        'case3': []
    }

    # CASE 1: two guides at the center of the room, each going to a different door.
    for i in range(num_of_iterations):
        case1_guide1 = Guide(Position(9.5, 10), 1.5, True)
        case1_guide2 = Guide(Position(10.5, 10), 1.5, True)

        simulation = Simulation(room, [], [case1_guide1, case1_guide2], vision)
        simulation.add_entities_randomly(num_entities, 1.5)
        simulation.run_simulate()
        times['case1'].append(simulation.end_time)
        # simulation.animate()

    # CASE 2: two guides standing near the walls at the center of the room, each going to a different door
    for i in range(num_of_iterations):
        case2_guide1 = Guide(Position(9.5, 0.5), 1.5, True)
        case2_guide2 = Guide(Position(10.5, 0.5), 1.5, True)

        simulation = Simulation(room, [], [case2_guide1, case2_guide2], vision)
        simulation.add_entities_randomly(num_entities, 1.5)
        simulation.run_simulate()
        times['case2'].append(simulation.end_time)
        # simulation.animate()

    # CASE 3: two guides standing each on a different wall and going to a different door
    for i in range(num_of_iterations):
        case3_guide1 = Guide(Position(9.5, 19.5), 1.5, True)
        case3_guide2 = Guide(Position(10.5, 0.5), 1.5, True)

        simulation = Simulation(room, [], [case3_guide1, case3_guide2], vision)
        simulation.add_entities_randomly(num_entities, 1.5)
        simulation.run_simulate()
        times['case3'].append(simulation.end_time)
        # simulation.animate()

    print('Evacuation time average:')
    print(f'CASE I: {sum(times["case1"]) / num_of_iterations}')
    print(f'CASE II: {sum(times["case2"]) / num_of_iterations}')
    print(f'CASE III: {sum(times["case3"]) / num_of_iterations}')


if __name__ == '__main__':
    # q1a()
    # q1b_c()
    # q2a()
    # q2b()
    # q2c()
    #q4a()
    #q4b()
    q4c()
    # q5_1door()
    # q5_2doors()
