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
    data_twstock = np.array(y)
    data_correlated = np.array(X)
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
        sess.run(train_step, feed_dict={xs: data_correlated, ys: data_twstock})
    return sess, predict

#def get_prediction(session, X):
#    session.run(predict, feed_dict = {xs: X})
#    return predict

#saver = tf.train.Saver()
#saver.save(session, save_path = 'data/', global_step=1)

#all_var = tf.trainable_variables()

#for layer in all_var:
#    print(layer.name)
#    print(session.run(layer))