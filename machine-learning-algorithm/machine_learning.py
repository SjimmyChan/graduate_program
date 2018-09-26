from __future__ import print_function
import tensorflow as tf
import numpy as np

def add_layer(inputs, in_size, out_size, activation_function=None):
    # add one more layer and return the output of this layer
    Weights = tf.Variable(tf.random_normal([in_size, out_size]))
    biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)
    Wx_plus_b = tf.matmul(inputs, Weights) + biases
    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)
    return outputs

# define placeholder for inputs to network
xs = tf.placeholder(tf.float32)
ys = tf.placeholder(tf.float32)

def data_training(X, y):
    # add hidden layer
    l1 = add_layer(xs, 1, 10, activation_function=tf.nn.relu)
    # add output layer
    predict = add_layer(l1, 10, 1, activation_function=None)

    # the error between prediction and real data
    loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - predict),
                        reduction_indices=[1]))
    train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

    # tf.initialize_all_variables()
    init = tf.global_variables_initializer()
    sess = tf.Session()
    sess.run(init)

    for i in range(1000):
        # training
        sess.run(train_step, feed_dict={xs: x_data, ys: y_data})
    return sess, predict

def get_prediction(session, predict, X):
    session.run(predict, feed_dict = {xs: X})
    return predict

# Make up some real data
x_data = np.linspace(-1,1,300)[:, np.newaxis]
noise = np.random.normal(0, 0.05, x_data.shape)
y_data = np.square(x_data) - 0.5 + noise

X = np.array([0.2])[:, np.newaxis]
prediction = 0
session, prediction = data_training(x_data, y_data)
prediction = get_prediction(session, prediction, X)

saver = tf.train.Saver()
saver.save(session, save_path = 'data/', global_step=1)

all_var = tf.trainable_variables()

for layer in all_var:
    print(layer.name)
    print(session.run(layer))