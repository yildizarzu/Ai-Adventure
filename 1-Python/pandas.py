""" PANDAS : DataFrame denilen yapılar içiçn geliştirilmiştir hızlı ve etikili bir kütüphanedir. Excel benzeri yapılar DataFrame'dir.NumPy'a benzerdir.
 ML için en iyi kütüphanedir. Dosyalar arası geçiş çok rahattır. 
 Missing Data için çözüm üretilebilir.
 Reshape ile datayı etkili kullandırabilir.
 
"""

import pandas as pd

dictionary = { "NAME":["arzu","gokhan","eren","ali","gizem","orhan"],
              "AGE":[27,29,22,31,21,31],
              "SALARY":[100,150,240,350,400,450]}

dataFrame1= pd.DataFrame(dictionary)

#Son eleman hariç
head = dataFrame1.head()

#ilk 3 eleman
head3 = dataFrame1.head(3)

#İlk eleman hariç
tail = dataFrame1.tail()

#son 3 eleman
tail3 = dataFrame1.tail(3)

#%% 

print(dataFrame1.columns)
print(dataFrame1.info())
print(dataFrame1.dtypes)

#Describe sadece numeric feature= column (age, salary) ile işlem yapar. Data Science için önemlidir. Sayısal hesaplamalar yapar. Ortalama alma, medyan hesaplama vs.
print(dataFrame1.describe())

# %% INDEXING & SLICING


print(dataFrame1["AGE"])
print(dataFrame1.AGE)

dataFrame1["yeni feature"] = [-1,-2,-3,-4,-5,-6]

print(dataFrame1.loc[:, "AGE"])

print(dataFrame1.loc[:3, "AGE"])

# 0 ile 3 arasındaki satıeları AGE ile NAME arasındaki feature datalarını getir.
print(dataFrame1.loc[:3, "AGE":"NAME"])

# 0 ile 3 arasındaki satıeları sadece AGE ile NAME feature datalarını getir.
print(dataFrame1.loc[:3, ["AGE","NAME"]])

#Data ları tersten yazdır
print(dataFrame1.loc[::-1,:])

#NAME de dahil NAME e kadar olan column'ları yazdır.
print(dataFrame1.loc[:,:"NAME"])

#Tüm satırların NAME column'ı getir.
print(dataFrame1.loc[:,"NAME"])

#Column değerilerini indexle getirir. İndexi 2 olan Column datalarını getir.
print(dataFrame1.iloc[:,2])

#%% FILTERING

filter1= dataFrame1.SALARY >250
filtersdata1= dataFrame1[filter1]

filter2= dataFrame1.AGE >29
filtersdata2= dataFrame1[filter2]

# %% LIST COMPREHENSION

import numpy as np

dataFrame1["yeni feature"] = [-1,-2,-3,-4,-5,-6]
average_salary = dataFrame1.SALARY.mean()

# average_salary_np = np.mean(dataFrame1.SALARY)


dataFrame1["maas seviyesi"] = ["dusuk" if average_salary > each else "yuksek" for each in dataFrame1.SALARY]

#for each in dataFrame1.MAAS:
#    if(ortalama_maas > each):
#        print("dusuk")
#    else:
#        print("yukse")

a=dataFrame1.columns

print(a)
b=dataFrame1.columns = [ each.lower() for each in dataFrame1.columns] 
print(b)

c=dataFrame1.columns = [each.split()[0]+"_"+each.split()[1] if(len(each.split())>1) else each for each in dataFrame1.columns]
print(c)


# %% drop and concatenating

dataFrame1.drop(["yeni_feature"],axis=1,inplace = True)

# dataFrame1 = dataFrame1.drop(["yeni_feature"],axis=1)

data1 = dataFrame1.head()
data2 = dataFrame1.tail()

# vertical
data_concat = pd.concat([data1,data2],axis=0)


# horizontal

salary = dataFrame1.salary
age = dataFrame1.salary

data_h_concat = pd.concat([salary,age],axis=1)

# %% transforming data

dataFrame1["list_comp"] = [ each*2 for each in dataFrame1.age]

# apply() : Bir fonksiyonu bütün DataFrame değerlerine uygular.

def multiply(age):
    return age*2
    
dataFrame1["apply_metodu"] = dataFrame1.age.apply(multiply)

