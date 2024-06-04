import pandas as pd
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import load_model


# 1. Eğitim verilerinin yüklenmesi

train_data = pd.read_csv("train_data.csv")

#2.Verilerin ayrılması (girdiler ve hedef değişkenler)

x_train= train_data.drop('target', axis=1)
y_train= train_data['target']

# 3.Verilerin Ölçeklenmesi
scaler=StandardScaler()
x_train=scaler.fit_transform(x_train)

# 4.Modelin Oluşturulması

model = Sequential([
    Dense(64, activation='relu'),
    Dense(x_train.shape[1], activation="relu"),
    Dense(32, activation="relu"),
    Dense(1)])

model.compile(optimizer='adam', loss='mean_squared_error')

# 5.Modelin eğitilmesi
model.fit(x_train, y_train, epochs=50, batch_size=32, verbose=1)

#6.Modelin kaydedilmesi

model.save('trained_model.h5')

# 7.Ölçekleyecinin kaydedilmesi

import joblib

joblib.dump(scaler, 'scaler.save')