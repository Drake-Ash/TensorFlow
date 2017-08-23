import tensorflow as tf
import numpy as np

data = []
data_set = open("KNN_data.csv", "r")
for addr in data_set:
     quotes = addr.split(',')
     fields = [f.strip('"') for f in quotes]
     data.append([int(f) for f in fields])

x_train = [[0 for x in range(2)] for y in range(len(data))]
y_train = [0 for x in range(len(data))]

for i in range(len(data)):
    x_train[i][0] = data[i][0]
    x_train[i][1] = data[i][1]
    y_train[i] = data[i][2]

xtr = tf.placeholder(tf.float32, [None, 2])
ytr = tf.placeholder(tf.float32, [None, 1])
xte = tf.placeholder(tf.float32)

K = 3

distance = tf.negative(tf.reduce_sum(tf.abs(xtr,xte), axis=1))
values, indices = tf.nn.top_k(distance, k=K, sorted=False)

sess = tf.InteractiveSession()
init = tf.global_variables_initializer()
sess.run(init)
