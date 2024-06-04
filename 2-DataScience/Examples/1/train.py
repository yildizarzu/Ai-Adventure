import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np

x_train = np.random.rand(1000,10)
y_train = np.random.rand(1000,1)


model = Sequential([Dense(64, activation='relu', input_shape=(10,)),Dense(64, activation="relu"),Dense(1)])

model.compile(optimizer='adam', loss='mean_squared_error')

model.fit(x_train,y_train,epochs=10, batch_size=32)

model.save('model.h5')

print("model eğitimi tamamlandı ve model.h5 olarak kaydedildi")