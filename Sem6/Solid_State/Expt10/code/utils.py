import numpy as np


def read_input(time = 2, dt = 4000, board=None):
    x, y = board.capture1('A1',int(time*1000000/dt),int(dt))
    return np.array(x), np.array(y)