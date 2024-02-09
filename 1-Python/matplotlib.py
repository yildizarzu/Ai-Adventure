""" MATPLOTLIB : ( VERİ GÖRSELLEŞTİRME ) NumPy + SciPy brileşimi MATLAB benzeri kütüphanedir.
- ML görevleri için veri işleme ve eğitime başlamadan önce anlamamıza yardımcı olur.
- Nesne yönelimli API'lerle çizimler ve grafikler üretmek içib PYTHON GUI araçlarını kullanır.
- Yayın kalitesinde grafikler oluşturabilir.
- Görsel stili ve düzeni özellşetirilebilir.
- Çeşitli dosya birimlerini aktarabilir.
- Yakınlaştırabilen, kaydırılabilen ve güncelleyebilen etkileşimli figürlere sahiptir.
 
"""

import pandas as pd
df = pd.read_csv("files/iris.csv")

#iris.csv dosyasındaki features:['Id', 'SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm','Species']
print(df.columns)

#Species feature için benzersiz değerleri verir. ['Iris-setosa' 'Iris-versicolor' 'Iris-virginica']
print(df.Species.unique())

print(df.info())

#Describe sadece numeric feature= column ile işlem yapar. Data Science için önemlidir. Sayısal hesaplamalar yapar. Ortalama alma, medyan hesaplama vs.
print(df.describe())

df_setosa = df[df.Species == "Iris-setosa"]
df_versicolor = df[df.Species == "Iris-versicolor"]

print(df_setosa.describe())
print(df_versicolor.describe())

# %% LINE PLOT :  bir sayı çizgisi boyunca veri sıklığını gösteren bir grafiktir.

import matplotlib.pyplot as plt

df1= df.drop(["Id"], axis=1)

#plot: grafik çizdirir
df1.plot()

#grafiği gösterir.
plt.show()

setosa = df[df.Species == "Iris-setosa"]
plt.plot(setosa.Id,setosa.PetalLengthCm,color="red",label= "setosa")

versicolor = df[df.Species == "Iris-versicolor"]
plt.plot(versicolor.Id,versicolor.PetalLengthCm,color="green",label= "versicolor")

virginica = df[df.Species == "Iris-virginica"]
plt.plot(virginica.Id,virginica.PetalLengthCm,color="blue",label= "virginica")


#Grafiklerde eksenlere isim vermek için xlabel ve ylabel kullanılır. Labelleri görebilmek için ise Legend kullanılır.
plt.xlabel("Id")
plt.ylabel("PetalLengthCm")
plt.legend()
plt.show()

#grid=True : Grafiğe ızgara ekler
df1.plot(grid=True,alpha= 0.9)
plt.show()

# %% SCATTER PLOT : iki farklı sayısal değişken için değerleri temsil etmek üzere noktalar kullanan grafiktir.

setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]
virginica = df[df.Species == "Iris-virginica"]

plt.scatter(setosa.PetalLengthCm,setosa.PetalWidthCm,color="red",label="setosa")
plt.scatter(versicolor.PetalLengthCm,versicolor.PetalWidthCm,color="green",label="versicolor")
plt.scatter(virginica.PetalLengthCm,virginica.PetalWidthCm,color="blue",label="virginica")
plt.legend()
plt.xlabel("PetalLengthCm")
plt.ylabel("PetalWidthCm")
plt.title("scatter plot")
plt.show()

# %% HISTOGRAM : gruplandırılmış bir veri dağılımının sütun grafiğiyle gösterimidir.

plt.hist(setosa.PetalLengthCm,bins= 50)
plt.xlabel("PetalLengthCm values")
plt.ylabel("frekans")
plt.title("hist")
plt.show()

# %% BAR PLOT: kategorik verileri temsil ettikleri değerlerle orantılı yükseklik veya uzunluktaki dikdörtgen çubuklarla ifade eden bir grafiktir. Çubuklar dikey veya yatay olarak çizilebilir.

import numpy as np

x = np.array([1,2,3,4,5,6,7])
a = ["turkey","usa","a","b","v","d","s"]
y = x*2+5

plt.bar(a,y)
plt.title("bar plot")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

# %% SUBPLOTS : alt grafiklerin tek bir grafikte gösterilmesini sağlar. Bu özelliği aktif etmek için subplot argümanını True yapmamız gerek.

df1.plot(grid=True,alpha= 0.9,subplots = True)
plt.show()

setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]
virginica = df[df.Species == "Iris-virginica"]

plt.subplot(2,1,1)
plt.plot(setosa.Id,setosa.PetalLengthCm,color="red",label= "setosa")
plt.ylabel("setosa -PetalLengthCm")
plt.subplot(2,1,2)
plt.plot(versicolor.Id,versicolor.PetalLengthCm,color="green",label= "versicolor")
plt.ylabel("versicolor -PetalLengthCm")
plt.show()

