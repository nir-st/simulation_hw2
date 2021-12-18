import matplotlib.pyplot as plt


def draw_routes(guides_posistions, entitys_positions):

    fig = plt.figure()
    ax1 = fig.add_subplot(111)

    ax1.scatter([20], [10], c="b", marker="s")

    for gp in guides_posistions:
        guide_xs = []
        guide_ys = []
        for pos in gp:
            guide_xs.append(pos.x)
            guide_ys.append(pos.y)
        ax1.scatter(guide_xs, guide_ys, c="y", marker=".")

    for ep in entitys_positions:
        entity_xs = []
        entity_ys = []
        for pos in ep:
            entity_xs.append(pos.x)
            entity_ys.append(pos.y)
        ax1.scatter(entity_xs, entity_ys, c="r", marker=".")

    plt.xlabel('X coordinate')
    plt.ylabel('Y coordinate')
    plt.title("Guides Route")
    plt.xlim([0, 20])
    plt.ylim([0, 20])
    plt.show()
