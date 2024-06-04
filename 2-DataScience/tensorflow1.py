"""
1) Veriyi anlamak ve hazırlamak için Pandas.
2) Eğitim ve Test verisini ayırmak
3) Model oluşturmak
"""
try:
    # 1 
    import pandas as pd
    
    dataFrame= pd.read_excel("bicycle_prices.xlsx")
    dataFrame.head()
    
    import matplotlib.pyplot as plt
    import seaborn as sbn
    
    sbn.pairplot(dataFrame)
    
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
    
    
    print( x_train.shape)
    
    print(x_test.shape)
    
    
    print(y_train.shape)
    
    
    print(y_test.shape)
    
    #Scaling : veriyi normalize etmek / Boyutunu büyütmek veya küçültmek. Sadece x verilerinde yapmak yeterli
    
    from sklearn.preprocessing import MinMaxScaler
    scaler = MinMaxScaler()
    scaler.fit(x_train)
    
    
    x_train = scaler.transform(x_train)
    x_test = scaler.transform(x_test)
    
    print(x_train)
    print(x_test)
    
    #3 
    
    import tensorflow as tf
    
    
    """from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import Dense"""
    
    #Modelimizin sınıfı Sequential
    model = tf.keras.models.Sequential()
    
    #Modelimizin içerisine katman  ekliyoruz. 
    
    #Dense(nöron sayısı, aktivasyon)
    model.add(tf.keras.layers.Dense(4,activation="relu"))
    model.add(tf.keras.layers.Dense(4,activation="relu"))
    model.add(tf.keras.layers.Dense(4,activation="relu"))
    
    model.add(tf.keras.layers.Dense(1))
    
    #Modelin derlenmesi optimizer'da adam da iyi çalışır. loss: regresyonda mse kullanılır genelde.
    model.compile(optimizer = "rmsprop",loss = "mse")
    
    #modelin eğitilmesi
    #batch_size : aynı anda kaç verinin işleneceği. 
    #epochs: Veri setinin kaç kez okunacağı. Epochs sayısı fazla gelirse ezberleyebilir. 
    
    model.fit(x_train,y_train,epochs=250)
    
except Exception as e:
    print(str(e))


















