import tensorflow as tf

# 一個常數張量 (0階 = scalar)
a = tf.constant(5)
print(a)   # tf.Tensor(5, shape=(), dtype=int32)

# 一個向量 (1階 tensor)
b = tf.constant([1, 2, 3])
print(b)   # shape=(3,)

# 一個矩陣 (2階 tensor)
c = tf.constant([[1, 2],
                 [3, 4]])
print(c)   # shape=(2,2)

# 矩陣加法
d = tf.constant([[5, 6],
                 [7, 8]])
print(tf.add(c, d))

# 矩陣乘法 (線性代數裡的矩陣乘法)
print(tf.matmul(c, d))

print(tf.subtract(c,d))