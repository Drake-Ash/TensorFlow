import tensorflow as tf
import numpy as np

features = [tf.contrib.layers.real_valued_column("x", dimension=1)]
estimator = tf.contrib.learn.LinearRegressor(feature_columns=features)

x_train = np.array([1., 2., 3., 4.])
y_train = np.array([.1, .2, .3, .4])

x_eval = np.array([1.01, 2.02, 3.03, 4.04])
y_eval = np.array([.11, .22, .33, .44])

input_fn = tf.contrib.learn.io.numpy_input_fn({"x": x_train}, y_train, batch_size=4, num_epochs=1000)
eval_input_fn = tf.contrib.learn.io.numpy_input_fn({"x": x_eval}, y_eval, batch_size=4, num_epochs=1000)

estimator.fit(input_fn=input_fn, steps=1000)

t_loss = estimator.evaluate(input_fn=input_fn)
e_loss = estimator.evaluate(input_fn=eval_input_fn)

print("train error:%r"% t_loss)
print("eval error:%r"% e_loss)
