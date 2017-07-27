import tensorflow as tf
W = tf.Variable([.3], dtype=tf.float32)
b = tf.Variable([-.3], dtype=tf.float32)
x = tf.placeholder(tf.float32)
linear_model = W * x + b
y = tf.placeholder(tf.float32)
J = tf.reduce_sum(tf.square(linear_model-y))
grad_desc = tf.train.GradientDescentOptimizer(0.01)
#GradientDescentOptimizer parameter accepts values less than 0.01
train = grad_desc.minimize(J)
X_train = [1, 2, 3, 4, 5]
Y_train = [0, -1, -2, -3, 6]
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

curr_W, curr_b, curr_loss = sess.run([W, b, J], {x: X_train, y: Y_train})
print("W: %s b: %s loss: %s"%(curr_W, curr_b, curr_loss))

for i in range(2000):
    sess.run(train, {x: X_train, y: Y_train})

curr_W, curr_b, curr_loss = sess.run([W, b, J], {x: X_train, y: Y_train})
print("W: %s b: %s loss: %s"%(curr_W, curr_b, curr_loss))
