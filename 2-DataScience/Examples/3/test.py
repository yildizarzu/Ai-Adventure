import numpy as np
import pandas as pd

dataFrame= pd.read_excel("bicycle_prices.xlsx")
dataFrame.head()

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

#Yeni bisiklet özelliklerini içeren bir liste oluşturur.
yeniBisikletOzellikleri = [[1751,1750]]

#Yeni bisiklet özelliklerini daha önce eğitim verileri üzerinde kullanılan ölçekleyici (scaler) ile ölçekler.
yeniBisikletOzellikleri = scaler.transform(yeniBisikletOzellikleri)


from tensorflow.keras.models import load_model


#Daha önce kaydedilen modeli bisiklet_modeli.h5 dosyasından yükler.
sonradanCagirilanModel= load_model("bisiklet_modeli.h5")

#Yüklenen model ile yeni bisiklet özellikleri için tahmin yapar
sonradanCagirilanModel.predict(yeniBisikletOzellikleri)

print("Yeni özelliklere göre yapılan tahmin")
#Yüklenen modelin yaptığı tahminleri ekrana yazdırır.
print(sonradanCagirilanModel.predict(yeniBisikletOzellikleri))