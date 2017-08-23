import numpy as np
import tensorflow as tf
from tensorflow.examples.tutorials.mnist.input_data import read_data_sets

mnist = read_data_sets("/MNIST_data/", one_hot=True)

X_train, Y_train = mnist.train.next_batch(5000)
X_test, Y_test = mnist.test.next_batch(100)

xtr = tf.placeholder(tf.float32, [None, 28*28])
ytr = tf.placeholder(tf.float32, [None, 10])
xte = tf.placeholder(tf.float32, [28*28])

K=3
nearest_neighbors = tf.Variable([0, 0, 0])

distance = tf.negative((tf.reduce_sum(tf.abs(tf.subtract(xtr, xte)), axis=1)))
values, indices = tf.nn.top_k(distance, k=K, sorted=False)

nn = []
for i in range(K):
    nn.append(tf.argmax(ytr[indices[0], 0]))

nearest_neighbors = nn

print
