import tensorflow as tf
a = tf.Variable([3], dtype=tf.float32)
b = tf.Variable([4], dtype=tf.float32)
x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)
linear_model = x*a + b
print(sess.run(linear_model, {x: [1, 2, 3, 4, 8], y: [1, 5, 4, 8, 6]}))
J = tf.square(linear_model-y)
J = tf.reduce_sum(J)
print(sess.run(J, {x: [1, 2, 3, 4, 8], y: [1, 5, 4, 8, 6]}))
