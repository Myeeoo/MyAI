import tensorflow as tf
import os

# 定义训练数据集
x_train = [1, 2, 3, 4]
y_train = [0, -1, -2, -3]

# 定义模型结构
model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(units=1, input_shape=[1]))

# 编译模型
model.compile(optimizer=tf.keras.optimizers.Adam(0.1), loss='mean_squared_error')

# 训练模型sd
model.fit(x_train, y_train, epochs=1000)

# 保存模型
model.save('model')

# 使用模型进行预测
print(model.predict([10]))

print(os.path.exists('model'))