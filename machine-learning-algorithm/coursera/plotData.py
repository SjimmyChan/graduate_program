def plotData(X, y):

    import matplotlib.pyplot as plt
    import numpy as np

    pos = np.where(y==1)
    neg = np.where(y==0)

    p1 = plt.plot(X[pos,0], X[pos,1], marker='+', markersize=9, color='k')[0]
    p2 = plt.plot(X[neg,0], X[neg,1], marker='o', markersize=7, color='y')[0]

    return plt, p1, p2