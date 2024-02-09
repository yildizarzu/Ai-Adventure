""" Bilimsel hesaplamaları hızlı bir şekilde yapmamızı sağlayan "matematik" kütüpnhanesidir.
    - NumPy çok fazla karmaşık çalışma gerektirmeden makine öğrenmesi modellerinin performansını artırmak için harika seçenektir.
    - NumPy dizileri homojendir. Aynı veri tipi elemanları içerir.
    - Yüksek performanslı N boyutlu dizi
    -Şekil manipülasyonu
    - Veri temizleme/ manipülasyon
    - İstatistiksel işlemler ve lineer cebir  """

# importing
import numpy as np

#%%
# numpy basics
array = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])  # 1*15 vector

#.shape : Numpy array nesnesinin kaç satır ve sütundan oluştuğunu gösteren bir tupple nesnesi döndürür.
print(array.shape)

#reshape : Numpy array’i yeniden şekillendirir.
a = array.reshape(3,5)
print("shape: ",a.shape)

# .ndim :  Numpy array nesnesinin boyutunu döndürür.
print("dimension: ", a.ndim)

print("data type: ",a.dtype.name)
print("size: ",a.size)

print("type: ",type(a))

array1 = np.array([[1,2,3,4],[5,6,7,8],[9,8,7,5]])

#np.zeros() : Bu fonksiyon belirtilen satır ve sütuna sahip 0'lardan oluşan bir matris döndürür.
zeros = np.zeros((3,4))

zeros[0,0] = 5
print(zeros)

np.ones((3,4))

np.empty((2,3))

#np.arange() : Sıralı bir array oluşturmak için np.arange komutundan yararlanabiliriz. Python’daki range() fonksiyonuna benzer. Belirtilen başlangıç değerinden başlayıp, her seferinde adım sayısı kadar arttırarak ,bitiş değerine kadar olan sayıları bulunduran bir numpy dizisi dödürür. 
a = np.arange(10,50,5)
print(a)

#np.linspace :  İki değer arasında olan sayıları eşit olarak böler. 0 ve 100 arasını 5 eşit parçaya böl ve göster
a = np.linspace(0,100,5)
print(a)

#%%

#numpy basic operations

a = np.array([1,2,3])
b = np.array([4,5,6])

print(a+b)
print(a-b)

#a**2 karesini almak
print(a**2)

print(np.sin(a))

print(a<2)


a = np.array([[1,2,3],[4,5,6]])
b = np.array([[1,2,3],[4,5,6]])

# element wise prodcut
print(a*b)
print(b.T)

# matrix prodcut 
# .dot matris çarpımı yapar
a.dot(b.T)

print(a)
# e sayısına üslü alarak işlem yapar. e = 2.71828183 
print(np.exp(a))

a = np.random.random((5,5))

print(a.sum())
print(a.max())
print(a.min())


#Toplama yapılırken axis = 0 demek sütun (column) bazında, axis = 1 ise satır (row) bazında toplamayı belirtir
print(a.sum(axis=0))
print(a.sum(axis=1))

#  sqrt : karekçk alma, square : karesini almak
print(np.sqrt(a))
print(np.square(a)) # a**2

print(np.add(a,a))

#%%

array = np.array([1,2,3,4,5,6,7])   #  vector dimension = 1

print(array[0])

print(array[0:4])

reverse_array = array[::-1]
print(reverse_array)


array1 = np.array([[1,2,3,4,5],[6,7,8,9,10]])

# array[hangi elemana bakılacak, neresine bakılacak]
print(array1[1,1])

print(array1[:,1])


print(array1[1,1:4])


print(array1[-1,:])
print(array1[:,-1])

# %%
# shape manipulation
array = np.array([[1,2,3],[4,5,6],[7,8,9]])

# ravel: flatten yani tek satıra dönüştürür.
a = array.ravel()

print(a)

array2 = a.reshape(3,3)

arrayT = array2.T

print(arrayT.shape)


array5 = np.array([[1,2],[3,4],[4,5]])


#array5 = np.column_stack((array1,array1))

# %% stacking arrays

array1 = np.array([[1,2],[3,4]])
array2 = np.array([[-1,-2],[-3,-4]])

# vstack: veritical dikey birleştirme yapar
array3 = np.vstack((array1,array2))

print(array3)
# horizontal
#array([[1, 2],[-1, -2],
#       [3, 4]],[-3, -4]]

# hstack: horizontal yatay birleştirme yapar.
array4 = np.hstack((array1,array2))
print(array4)

#%% convert and copy

liste = [1,2,3,4]   # list

array = np.array(liste) #np.array

liste2 = list(array)

a = np.array([1,2,3])

b = a
b[0] = 5
c = a

d =  np.array([1,2,3])

e = d.copy()

f = d.copy()
