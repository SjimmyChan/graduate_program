def costFunctionReg(theta, X, y, lambda_reg, return_grad=False):

    import numpy as np
    from sigmoid import sigmoid

    m = len(y)

    J = 0
    grad = np.zeros(theta.shape)

    h = sigmoid(np.dot(X, theta))
    reg = (float(lambda_reg)/(2*m)) * np.power(theta[1:theta.shape[0]], 2).sum()
    J = -(1./m) * (y * np.transpose(np.log(h)) + (1-y) * np.transpose(np.log(1-h))).sum() + reg
    grad = (1./m) * np.dot(h.T - y, X).T + (float(lambda_reg/m)) * theta
    grad_no_regularization = (1./m) * np.dot(h.T - y, X).T
    grad[0] = grad_no_regularization[0]

    if return_grad == True:
        return J, grad.flatten()
    elif return_grad == False:
        return J