import math

import matplotlib.pyplot as plt
from matplotlib.patches import Circle


# ======================================================
# REFERENCE ILLUSTRATION
# ======================================================

def draw_reference():

    fig, ax = plt.subplots(
        figsize=(4, 2.8)
    )

    # ----------------------------------
    # geometry
    # ----------------------------------

    diameter = 6
    dome_depth = 0.8

    radius = diameter / 2

    # circle

    circle = Circle(
        (0, 0),
        radius,
        fill=False,
        lw=2,
        color="royalblue",
    )

    ax.add_patch(circle)

    # chord line

    y = -radius + dome_depth

    x = math.sqrt(
        radius**2 - y**2
    )

    ax.plot(
        [-x, x],
        [y, y],
        lw=2,
        color="royalblue",
    )

    # center

    ax.plot(
        0,
        0,
        "ko",
        ms=4,
    )

    # ----------------------------------
    # diameter arrow
    # ----------------------------------

    ax.annotate(
        "",
        xy=(radius, 0.3),
        xytext=(-radius, 0.3),
        arrowprops={
            "arrowstyle": "<->"
        },
    )

    ax.text(
        0,
        0.55,
        "Diameter",
        ha="center",
        fontsize=9,
    )

    # ----------------------------------
    # dome depth arrow
    # ----------------------------------

    ax.annotate(
        "",
        xy=(x + 0.4, y),
        xytext=(x + 0.4, -radius),
        arrowprops={
            "arrowstyle": "<->"
        },
    )

    ax.text(
        x + 0.7,
        (y - radius) / 2,
        "Dome\nDepth",
        fontsize=8,
        va="center",
    )

    # ----------------------------------
    # axes
    # ----------------------------------

    ax.set_xlim(-4, 4)

    ax.set_ylim(-4, 3)

    ax.set_aspect("equal")

    ax.axis("off")

    return fig
