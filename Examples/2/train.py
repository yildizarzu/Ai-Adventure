import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

dataFrame= pd.read_excel("bicycle_prices.xlsx")
dataFrame.head()

y = dataFrame["Fiyat"].values
x = dataFrame[["BisikletOzellik1","BisikletOzellik2"]].values

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.33,random_state=15)

scaler = MinMaxScaler()
scaler.fit(x_train)

x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)


model = Sequential([Dense(4, activation='relu'),Dense(4, activation="relu"),Dense(4, activation="relu"),Dense(1)])

#model.compile(optimizer='adam', loss='mean_squared_error')
model.compile(optimizer = "rmsprop",loss = "mse")
model.fit(x_train,y_train,epochs=250, batch_size=32)

model.save('model.h5')

print("model eğitimi tamamlandı ve model.h5 olarak kaydedildi")