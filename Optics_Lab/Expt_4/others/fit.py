import numpy as np

def least_square_fitting(func, x, y, variables=2, theta=None):
    import numpy as np
    if not theta:
        theta = np.random.rand(variables)
    y_pred = func(x, *theta)
    J = np.sum((y - y_pred) ** 2)  # cost function (SSE)
    slope = [(y-y_pred)]