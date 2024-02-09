"""VARIABLES"""

# %%
# Variable (degisken)
"""Veri saklamak için oluşturduğumuz alanlara variable(değişken) denir."""
var1 = 10 # integer = int
var2 = 15 
gun = "pazartesi" # string
var3 = 10.0 # double (float)
var5 = 10
# 5var = 10  # hata verir
var6 = 10
Var7 = 19  # standart convention of python'a gore buyuk harfle baslamasi uygun degil

# %%
# String 

s = "bugun gunlerden pazartesi"

variable_type = type(s)   # str = string

print(s)

var1 = "ankara"
var2 = "ist"
var3 = var1+var2

var4 = "100"
var5 = "200"
var6 = var4+var5

uzunluk = len(var6) 

# var6[3]

# %%
#Number (int)
integer_deneme = -50
# double = float = ondalikli sayi
float_deneme = -30.7

# %%
#List 
#Liste öğeleri sıralıdır, değiştirilebilir ve yinelenen değerlere izin verir. Listeler birden fazla öğeyi tek bir değişkende depolamak için kullanılır.
list1 = [1,2,3,4,5,6]
type(list1)

list_str = ["ptesi","sali","cars"]
type(list_str)

value = list1[1]
print(value)

last_value = list[-1]

liste_divide = list[0:3]

list1.append(7)
list1.remove(3) #listedeki 3 değerini siler
list1.reverse() #listeyi ters çevirir
print(list1)
list2 = [1,5,4,3,6,7,2]
list2.sort()

string_int_liste = [1,2,3,"aa","bb"]

#%%
#Tuple
# Tuplelar birden fazla öğeyi tek bir değişkende depolamak için kullanılır. Tuple, sıralı ve değiştirilemeyen bir koleksiyondur.

tuple1=(1,2,3,4,5,6)
#tuple değişkeninin metotlarını bulmak için Console ekranına dir(tuple1) yazabiliriz. Metotların ne işe yaradığını ise Console help(tuple.count) ile öğrenebiliriz.

print(tuple1.count(5)) #tuple da 5 değeri kaç tane var

#%%
#Dictionary: Sözlükler, veri değerlerini anahtar:değer çiftlerinde depolamak için kullanılır.Dictionary, sıralı(>=Python3.7), değiştirilebilir ve kopyalara izin vermeyen bir koleksiyondur.
#dictionary={key1:value1, key2:value2...}
dictionary = {"ali":32,"veli":45,"ayse":13}
print(dictionary["ali"])
dictionary["ali"]=20
print(dictionary["ali"])
print(dictionary.keys())
print(dictionary.values())

#%%
"""FUNCTIONS"""

# %%
#Built in Functions: daha önce yazılmış hazır fonksiyonlar.
str1= "deneme"
float1 = 10.6 
float2=float(10)
int1= int(float1)
round1= round(float1)
str2 = "1005"

# %%
#User Define Functions: kullanıcı tarafından tanımlanan fonksiyonlar

var1 = 20
var2 = 50

output = (((var1+var2)*50)/100.0)*var1/var2

# fonksiyon parametresi = input
def benim_ilk_func(a,b):
    
    """
    bu benim ilk denemem
    
    parametre: 
        
    return: 
    """
    output = (((a+b)*50)/100.0)*a/b
    
    return output
    
sonuc = benim_ilk_func(var1,var2)

#%%
#Default ve Flexible Functions: Default (Belirli parametreler alan), Flexible(Dinamik parametreler alan)

def default_func(r, pi:3.14):
    #Çember çevresini hesaplayan fonk.
    output=2*pi*r
    return output

def flexible_func(boy, kilo,*args):
    print(args)
    output=(boy+kilo)*args[0]
    return output
print(flexible_func(162, 54,15,20,11))

#%%
#Lambda Functions: Tek satırlık fonksiyonlardır, birden fazla parametre alabilirler fakat tek bir işlem yapabilirler.

#x in karesini alır.
lambda_func=lambda x:x*x
print(lambda_func(3))