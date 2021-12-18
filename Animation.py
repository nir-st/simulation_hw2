import matplotlib.pyplot as plt
import matplotlib.animation
import numpy as np


def yo(guides_positions):
    number_of_frames = 0

    gps = []
    for gp in guides_positions:
        gps.append(gp[0::10])
        if len(gp) > number_of_frames:
            number_of_frames = len(gp)

    fig = plt.figure()
    ax = fig.add_subplot(111)

    for gp in guides_positions:
        gx0 = gp[0].x
        gy0 = gp[0].y
        ax.scatter([gx0], [gy0], c="r", marker=".")

    def plot(i, gps, ax, plt):
        plt.cla()
        plt.title(f'Time Elapsed: {round(i*0.2)} seconds')
        plt.xlim(0, 20)
        plt.ylim(0, 20)
        for gp in gps:
            if i < len(gp):
                gx0 = gp[i].x
                gy0 = gp[i].y
                ax.scatter([gx0], [gy0], c="r", marker=".", label="guide")

    ani = matplotlib.animation.FuncAnimation(fig, plot, fargs=(gps, ax, plt,),
                frames=number_of_frames-1, interval=1, repeat=False)

    plt.xlim(0, 20)
    plt.ylim(0, 20)
    plt.title("Evacuation route")
    plt.show()
