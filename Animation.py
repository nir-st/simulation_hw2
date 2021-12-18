import matplotlib.pyplot as plt
import matplotlib.animation
import numpy as np


def animate(guides_positions, entities_positions):
    number_of_frames = 0

    gps = []
    eps = []

    for gp in guides_positions:
        gps.append(gp[0::10])
        if len(gp) > number_of_frames:
            number_of_frames = len(gp)

    for ep in entities_positions:
        eps.append(ep[0::10])
        if len(ep) > number_of_frames:
            number_of_frames = len(ep)

    fig = plt.figure()
    ax = fig.add_subplot(111)

    for gp in guides_positions:
        gx0 = gp[0].x
        gy0 = gp[0].y
        ax.scatter([gx0], [gy0], c="r", marker=".")

    for ep in entities_positions:
        ex0 = ep[0].x
        ey0 = ep[0].y
        ax.scatter([ex0], [ey0], c="b", marker=".")

    def plot(i, gps, eps, ax, plt):
        plt.cla()
        plt.title(f'Time Elapsed: {round(i*0.2)} seconds')
        plt.xlim(0, 20)
        plt.ylim(0, 20)
        for gp in gps:
            if i < len(gp):
                gx0 = gp[i].x
                gy0 = gp[i].y
                ax.scatter([gx0], [gy0], c="r", marker=".", label="guide")
        for ep in eps:
            if i < len(ep):
                ex0 = ep[i].x
                ey0 = ep[i].y
                ax.scatter([ex0], [ey0], c="b", marker=".", label="non-guide")

    ani = matplotlib.animation.FuncAnimation(fig, plot, fargs=(gps, eps, ax, plt,),
                frames=number_of_frames-1, interval=1, repeat=False)

    plt.xlim(0, 20)
    plt.ylim(0, 20)
    plt.title("Evacuation route")
    plt.show()
