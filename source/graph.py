"""
usage:
python3.7 source/graph.py
description:
A parody of Joy Division's Unknown Pleasures album cover
"""
import numpy as np
import matplotlib.pyplot as plt


def add_txt(axes):
    """Add text to the plot

    Parameters
    ----------
    axes : 
    """
    axes.text(0.5, 1.0, "FOURIER ", transform=axes.transAxes,
              ha="right", va="bottom", color="w",
              family="sans-serif", fontweight="light", fontsize=16)

    axes.text(0.5, 1.0, "UNCHAINED", transform=axes.transAxes,
              ha="left", va="bottom", color="w",
              family="sans-serif", fontweight="bold", fontsize=16)


def format_axes(axes):
    """Size the axes and add ticks

    Parameters
    ----------
    axes : 
    """
    axes.set_xlim(0, 10)
    axes.set_xticks([])

    axes.set_ylim(0, 10)
    axes.set_yticks([])


def plot_waves(axes):
    """Plot the successive sine waves on the graph"""
    lines = []
    X = np.linspace(0, 10, 512)
    for i in range(1, 6):
        xscale = 1 - i / 20.
        lw = 1.5 - i / 100.0

        y_delta = 1.6 * i
        freq = (2 * i)
        phase = np.pi/2

        line, = axes.plot(X, np.sin((freq * X) + phase) +
                          y_delta, color="w", lw=lw)
        lines.append(line)
    return lines


def main():
    """Run all executable code"""
    fig = plt.figure(figsize=(8, 8), facecolor="black")
    axes = fig.add_subplot(111, frameon=False)

    add_txt(axes)

    format_axes(axes)

    plot_waves(axes)

    plt.show()


if __name__ == "__main__":
    main()
