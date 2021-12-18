import Drawer
from Room import Room
from Simulation import Simulation
from Guide import Guide
from Entity import Entity
from Position import Position
import random
import numpy as np
import matplotlib.pyplot as plt


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
    #todo: print plot (animation?)


# -------------------------------------------------------------------------- #
#                                     Q1b                                    #
# -------------------------------------------------------------------------- #
def q1b():
    room = Room(20, 20, [Position(20, 10)])
    simulations_end_times =[]
    max_time_to_evacuate = 0
    for i in range(200):
        guides_x_position = random.randint(0, 20)
        guides_y_position = random.randint(0, 20)
        guide = Guide(Position(guides_x_position, guides_y_position), 1.5, True)
        entities = []
        guides = [guide]
        simulation = Simulation(room, entities, guides)
        simulation.run_simulate()
        simulations_end_times.append(simulation.end_time)
        if simulation.end_time > max_time_to_evacuate:
            max_time_to_evacuate = simulation.end_time

    plt.title("Time to evacuate")
    plt.xlabel("Time in seconds")
    plt.ylabel("Number of events")
    plt.hist(simulations_end_times, bins=8)
    plt.show()
    print(f'Maximum finish time {max_time_to_evacuate} seconds')
    print(f'Average time to evacuate was {sum(simulations_end_times) / 200} seconds')


# -------------------------------------------------------------------------- #
#                                     Q1c                                    #
# -------------------------------------------------------------------------- #
#TODO


# -------------------------------------------------------------------------- #
#                                     Q2a                                    #
# -------------------------------------------------------------------------- #
def q2a():
    num_of_guides = [20, 50, 100]
    room = Room(20, 20, [Position(20, 10)])
    for N in num_of_guides:
        simulation = Simulation(room, [], [])
        simulation.add_guides_randomly(N, 1.5, False)
        simulation.run_simulate()
        print(f'\nInitial number of guides: {N}')
        simulation.print_stats()
        # Drawer.draw_shit([g.positions for g in simulation.guides] + [g.positions for g in simulation.got_out_guides], [])


if __name__ == '__main__':
    # q1a()
    # q1b()
    q2a()
