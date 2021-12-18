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
    guide = Guide(Position(5, 10), 1.5, True)
    entities = []
    guides = [guide]
    simulation = Simulation(room, entities, guides)
    simulation.run_simulate()
    simulation.print_stats()
    Drawer.draw_shit([g.positions for g in simulation.guides] + [g.positions for g in simulation.got_out_guides], [])


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
    num_of_guides = [20, 50, 100, 200]
    room = Room(20, 20, [Position(20, 10)])
    for N in num_of_guides:
        simulation = Simulation(room, [], [])
        simulation.add_guides_randomly(N, 1.5, False)
        simulation.run_simulate()
        print(f'\nInitial number of guides: {N}')
        simulation.print_stats()
        simulation.animate()


# -------------------------------------------------------------------------- #
#                                     Q2b                                    #
# -------------------------------------------------------------------------- #
def q2b():
    num_of_guides = [25, 50, 75, 100, 125, 150, 175, 200]
    room = Room(20, 20, [Position(20, 10)])
    end_times = []

    for N in num_of_guides:
        simulation = Simulation(room, [], [])
        simulation.add_guides_randomly(N, 1.5, False)
        simulation.run_simulate()
        # simulation.print_stats()
        Drawer.draw_shit([g.positions for g in simulation.guides] + [g.positions for g in simulation.got_out_guides], [])
        # simulation.animate()
        print(f'finished simulation of of {N} guides. Evacuation time: {simulation.end_time}')
        end_times.append(simulation.end_time)

    plt.plot(num_of_guides, end_times)
    plt.show()


# -------------------------------------------------------------------------- #
#                                     Q2c                                    #
# -------------------------------------------------------------------------- #
def q2c():
    num_of_guides = [10, 50, 100, 200, 250, 300]
    room = Room(20, 20, [Position(20, 10)])
    end_times = []

    for N in num_of_guides:
        simulation = Simulation(room, [], [])
        simulation.add_guides_randomly(round((N/3) * 2), 1.5, False)
        simulation.add_guides_randomly(round(N/3), 0.5, False)
        simulation.run_simulate()
        # simulation.print_stats()
        # simulation.animate()
        print(f'finished simulation of of {N} guides. Evacuation time: {simulation.end_time}')
        end_times.append(simulation.end_time)

    plt.plot(num_of_guides, end_times)
    plt.show()


if __name__ == '__main__':
    # q1a()
    # q1b()
    q1b_c()

    # q2a()
    # q2b()
    q2c()