import matplotlib.figure as fgr
import numpy as np


def f(fi, a):
    return a / fi


def degrees_to_radian(x):
    return x * np.pi / 180


def func_plot(min_fi, max_fi, a):
    fig = fgr.Figure(figsize=(5, 4), dpi=100)
    fi = np.linspace(degrees_to_radian(min_fi), degrees_to_radian(max_fi), 1000)
    r = [f(x, a) for x in fi]
    ax = fig.add_subplot(111, polar=True)
    ax.plot(fi, r)
    return fig
