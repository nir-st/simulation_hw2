
from Room import Room
from Simulation import Simulation
from Guide import Guide
from Position import Position

if __name__ == '__main__':
    room = Room(20, 20, [Position(20, 10)])
    guide = Guide(Position(10, 10), 1.5, True)
    entities = []
    guides = [guide]

    simulation = Simulation(room, entities, guides)
    simulation.run_simulate()
    print("done")


