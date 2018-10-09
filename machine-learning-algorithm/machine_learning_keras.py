from keras.models import Sequential
from keras.layers import Dense, Activation
import numpy as np
import json


#def readjson(filename):
#    with open(filename,'r') as load_f:
#        load_dict = json.load(load_f)
#    return load_dict

def data_training(stockid, correlation_data, correlation_ratio, twstock_data):
    #x = readjson("correlated.json")
    #y = readjson("twstock.json")
    #cr = readjson("correlated_ratio.json")

    x = np.array(correlation_data)
    y = np.array(twstock_data)
    cr = np.array(correlation_ratio)
    m, n = x.shape
    x = np.transpose(x)

    n = []
    t=0
    for correlation_ratio in x:
        c=0
        nn = []
        for ratio in correlation_ratio:
            #nn.append((b-np.mean(x, axis=0))/np.std(x, axis=0))
            #s = (b-np.mean(x, axis=1)[t])/np.std(x, axis=1)[t]
            nn.append(ratio)
            nn.append(cr[c][0])
            c = c+1
        n.append(nn)
        t = t+1
    x = np.array(n)

    M = m*2
    model = Sequential()
    model.add(Dense(1024,input_shape=(M,),activation='relu'))
    model.add(Dense(512,activation='relu'))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mae', metrics=['mae'])
    model.fit(x, y, batch_size=4, epochs=80, initial_epoch=0)
    model.save_weights('data\{}.h5'.format(stockid))
    print("save {} model complete".format(stockid))
    del model

def get_predict(stockid, correlated_data, len_of_data):

    M = len_of_data*2
    model = Sequential()
    model.add(Dense(1024,input_shape=(M,),activation='relu'))
    model.add(Dense(512,activation='relu'))
    model.add(Dense(1))
    model.load_weights('data\{}.h5'.format(stockid))
    print("get {} predict complete".format(stockid))
    
    return model.predict(correlated_data)

