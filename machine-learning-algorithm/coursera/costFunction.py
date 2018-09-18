def costFunction(theta, X, y, return_grad=False):

    import numpy as np
    from sigmoid import sigmoid

    m = len(y)
    J = 0
    grad = np.zeros(theta.shape)

    h = sigmoid(np.dot(X, theta))
    J = -(1./m) * ((y * np.transpose(np.log(h))) + (1-y) * np.transpose(np.log(1-h))).sum()
    grad = (1./m) * np.dot(h.T - y, X).T

    if return_grad == True:
        return J, np.transpose(grad)
    elif return_grad == False:
        return J
