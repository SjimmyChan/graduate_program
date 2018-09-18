def predict(theta, X):

    import numpy as np
    from sigmoid import sigmoid

    m = X.shape[0] # Number of training examples

    # You need to return the following variables correctly
    p = np.zeros((m, 1))

    sigValue = sigmoid( np.dot(X,theta) )
    p = sigValue >= 0.5

    return p