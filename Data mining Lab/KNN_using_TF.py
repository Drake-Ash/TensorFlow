import tensorflow as tf
import numpy as np

x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)

k = tf.placeholder(tf.float32)

sess = tf.session()
init = tf.global_variables_initializer()
sess.run(init)


