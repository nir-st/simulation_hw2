from Room import Room
from Simulation import Simulation
from Guide import Guide
from Entity import Entity
from Position import Position
import random
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
    for i in range(100):
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
    # q2a()
    # q2b()
    q2c()