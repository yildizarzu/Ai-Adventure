"""
1) Veriyi anlamak ve hazırlamak için Pandas.
2) Eğitim ve Test verisini ayırmak
3) Model oluşturmak
"""

import numpy as np
# 1 
import pandas as pd

dataFrame= pd.read_excel("bicycle_prices.xlsx")
dataFrame.head()


# 2 
from sklearn.model_selection import train_test_split

#train_test_split
    
# y = wx + b
# y -> label

# y fiyat sonuçları / çıktılar, y_train : label öğrenim verisi, y_test: label test verisi
y = dataFrame["Fiyat"].values

# x -> feature (özellik)
# x özellikler / girdiler, x_train : özellik öğrenim verisi, x_test: özellik test verisi
x = dataFrame[["BisikletOzellik1","BisikletOzellik2"]].values

#test_size: test verisinin % oranı. 
# random_state: aynı sayıyı veren kişilerde aynı algoritma kullanılır ve aynı test ve eğitim verileriyle işlem yaptırır.
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.33,random_state=15)

#Scaling : veriyi normalize etmek / Boyutunu büyütmek veya küçültmek. Sadece x verilerinde yapmak yeterli 
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
scaler.fit(x_train)

x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)

#3
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

#Modelimizin sınıfı Sequential
#Modelimizin içerisine katman  ekliyoruz. 
#Dense(nöron sayısı, aktivasyon)
model = Sequential([Dense(4, activation='relu'),Dense(4, activation="relu"),Dense(4, activation="relu"),Dense(1)])

#Modelin derlenmesi optimizer'da adam da iyi çalışır. loss: regresyonda mse kullanılır genelde.
model.compile(optimizer='adam', loss='mean_squared_error')

#modelin eğitilmesi
#batch_size : aynı anda kaç verinin işleneceği. 
#epochs: Veri setinin kaç kez okunacağı. Epochs sayısı fazla gelirse ezberleyebilir. 

model.fit(x_train,y_train,epochs=250, batch_size=32)

#modelin kaydedilmesi
#model.save('model.h5')
#model.save('my_model.keras')

print("model eğitimi tamamlandı ve model.h5 olarak kaydedildi")


import seaborn as sbn
import matplotlib.pyplot as plt

#dataFrame'deki sayısal değişkenler arasındaki ilişkileri ve dağılımları görselleştir
sbn.pairplot(dataFrame)

#modelin eğitim sürecinde her epoch için hesaplanan kayıp değerlerini içeren bir listeyi temsil eder. Bu değerler, modelin eğitim performansını değerlendirmek ve izlemek için kullanılır.
loss = model.history.history["loss"]

#Modelin eğitim sürecindeki loss(kayıp) değerlerinin bir çizgi grafiğini oluşturur.
sbn.lineplot(x=range(len(loss)),y=loss)
# Eğitim verisi üzerindeki kayıp değerini değerlendirme
trainLoss = model.evaluate(x_train,y_train, verbose=0)
# Test verisi üzerindeki kayıp değerini değerlendirme
testLoss = model.evaluate(x_test,y_test,verbose=0)

#veri setindeki girdiler için modelden tahminler yapar ve bu tahminleri testTahminleri değişkenine atar.
testTahminleri = model.predict(x_test)
print("Test Tahminleri")
print(testTahminleri)

#y_test değerlerini içeren bir pandas DataFrame oluşturur ve bu sütuna "Gerçek Y" adını verir.
tahminDf = pd.DataFrame(y_test,columns=["Gerçek Y"])
#testTahminleri dizisini yeniden şekillendirir ve bir pandas Series'e dönüştürür. Buradaki 330 değeri, test verilerindeki örnek sayısıdır.
testTahminleri = pd.Series(testTahminleri.reshape(330,))

#tahminDf ile testTahminleri Series'ini sütunlar olarak birleştirir.
tahminDf = pd.concat([tahminDf,testTahminleri],axis=1)

#tahminDf DataFrame'in sütun adlarını "Gerçek Y" ve "Tahmin Y" olarak ayarlar.
tahminDf.columns = ["Gerçek Y", "Tahmin Y"]

#Gerçek ve tahmin edilen değerler arasındaki ilişkiyi scatter plot (dağılım grafiği) kullanarak görselleştiri
sbn.scatterplot(x = "Gerçek Y", y = "Tahmin Y", data = tahminDf)
#tahminDf içindeki verilerin çiftler arasındaki ilişkilerini görselleştiren bir pair plot oluşturur.
sbn.pairplot(tahminDf)

from sklearn.metrics import mean_absolute_error, mean_squared_error

#Gerçek ve tahmin edilen değerler arasındaki ortalama mutlak hatayı hesaplar.
mean_absolute_error(tahminDf["Gerçek Y"],tahminDf["Tahmin Y"])

#Gerçek ve tahmin edilen değerler arasındaki ortalama kare hatayı hesaplar.
mean_squared_error(tahminDf["Gerçek Y"],tahminDf["Tahmin Y"])

print("DataFrame Describe")
#dataFrame veri kümesinin özet istatistiklerini ekrana yazdırır (ortalama, standart sapma, minimum, maksimum vb.).
print(dataFrame.describe())

#Modeli bisiklet_modeli.h5 dosyasına kaydeder.
model.save("bisiklet_modeli.h5")





















