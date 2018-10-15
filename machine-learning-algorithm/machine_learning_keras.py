from keras.models import Sequential
from keras.layers import Dense, Activation, Flatten
import numpy as np
import json

def data_training(stockid, correlation_data, correlation_ratio, twstock_data):
    x = correlation_data
    y = twstock_data
    cr = correlation_ratio

    t1 = list()
    for s1 in range(92):
        t2 = list()
        for s2 in range(91):
            t3 = list()
            t3.append(x[s2][s1])
            t3.append(cr[s2][0])
            t2.append(t3)
        t1.append(t2)
    t = np.array(t1)
    y = np.array(y)

    model = Sequential()
    model.add(Flatten(input_shape=(91,2)))
    model.add(Dense(1024,activation='relu'))
    model.add(Dense(512,activation='relu'))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mae', metrics=['mae'])
    model.fit(t, y, batch_size=4, epochs=80, initial_epoch=0)
    model.save_weights('data\{}.h5'.format(stockid))
    print("save {} model complete".format(stockid))
    del model

def get_predict(stockid, correlated_data, correlated_ratio):
    x = correlated_data
    cr = correlated_ratio

    t1 = list()
    for s2 in range(91):
        t2 = list()
        t2.append(x[s2])
        t2.append(cr[s2])
        t1.append(t2)
    t = np.array(t1)
    t = t[np.newaxis, :, :]
    print(t.shape)

    model = Sequential()
    model.add(Flatten(input_shape=(91,2)))
    model.add(Dense(1024,activation='relu'))
    model.add(Dense(512,activation='relu'))
    model.add(Dense(1))
    model.load_weights('data\{}.h5'.format(stockid))
    
    return model.predict(t)

