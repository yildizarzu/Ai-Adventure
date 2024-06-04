import pandas as pd
import joblib
from tensorflow.keras.models import load_model

#1. Test verilerini yükleme

test_data=pd.read_csv('test_data.csv')

#2.Verilerin ayrılması (girdiler ve hedef değişkenler)

x_test= test_data.drop('target', axis=1)
y_test= test_data['target']

# 3.Ölçekleyicinin Yüklenmesi
scaler=joblib.load('scaler.save')
x_test = scaler.transform(x_test)

#4.Modelin Yüklenmesi
model= load_model ('trained_model.h5')

#5.Test verisi üzerinde tahmin yapılması
test_predictions = model.predict(x_test)

# 6. Tahminlerin ve Gerçek değerlerin DataFrame 'e dönüşütürlmesi
results_df = pd.DataFrame({'Gerçek Y': y_test, 'Tahmin Y':test_predictions.flatten()})

#7. Sonuçların Görselleştirilmesi

import seaborn as sbn
import matplotlib.pyplot as plt

sbn.scatterplot( x='Gerçek Y', y='Tahmin Y', data=results_df)
plt.xlabel('Gerçek Y')
plt.ylabel('Tahmin Y')
plt.title('Gerçek ve Tahmin Değerlerinin Dağılımı')
plt.show()

sbn.pairplot(results_df)
plt.show()

#8. Hata metriklerinin hesaplanması
from sklearn.metrics import mean_absolute_error, mean_squared_error

mae=mean_absolute_error(results_df['Gerçek Y'], results_df['Tahmin Y'])
mse=mean_squared_error(results_df['Gerçek Y'], results_df['Tahmin Y'])

print(f"Ortalama Mutlak Hata (MAE): {mae}")
print(f"Ortalama Kare Hata (MSE): {mse}")