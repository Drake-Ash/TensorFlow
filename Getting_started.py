import tensorflow as tf
a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
tf.global_variables_initializer()
node_adder = a+b
session = tf.Session()
print(session.run(node_adder,{a:4,b:5}))