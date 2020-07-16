import os
os.environ['TF_CPP_MIN_LOG_}LEVEL'] = '2'

import tensorflow as tf

hello = tf.constant('Hello, TensorFlow!')

print(hello.numpy())