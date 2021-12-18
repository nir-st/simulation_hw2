from Room import Room
from Simulation import Simulation
from Guide import Guide
from Position import Position
import random
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # -------------------------------------------------------------------------- #
    #                                     Q1a                                    #
    # -------------------------------------------------------------------------- #

    room = Room(20, 20, [Position(20, 10)])
    guide = Guide(Position(10, 10), 1.5, True)
    entities = []
    guides = [guide]

    simulation = Simulation(room, entities, guides)
    simulation.run_simulate()
    #todo: print plot (animation?)

    # -------------------------------------------------------------------------- #
    #                                     Q1b                                    #
    # -------------------------------------------------------------------------- #

    simulations_end_times =[]
    max_time_to_evacuate = 0
    for i in range(200):
        guides_x_position = random.randint(0, 20) #todo: Make sure its uniformic
        guides_y_position = random.randint(0, 20)
        guide = Guide(Position(guides_x_position, guides_y_position), 1.5, True)
        entities = []
        guides = [guide]
        simulation = Simulation(room, entities, guides)
        simulation.run_simulate()
        simulations_end_times.append(simulation.end_time)
        if simulation.end_time > max_time_to_evacuate:
            max_time_to_evacuate = simulation.end_time

    y = np.array(simulations_end_times)
    x = np.arange(0, 200)
    plt.title("Line graph")
    plt.xlabel("X axis")
    plt.ylabel("Y axis")
    plt.plot(x, y, color="green") #todo: arrange in buckets
    plt.show()
    print(f'Maximum finish time {self.max_time_to_evacuate * 0.02} seconds')



