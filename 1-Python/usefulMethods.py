# range() => Sayı dizisi oluşturur. range() metodu isteğe bağlı olarak toplam 3 parametre alabilir : başlangıç, bitiş ve artırma

print(*range(5,50,5))
print(*range(5,50,-5))

for i in list(range(15)):
    print(i)
    
for i in range(0,10):
    print(i)
    
# enumerate() => Listedeki hem elemanı hem de indeksi getirir.
for eleman in enumerate(list(range(5,15))):
    print(eleman)
    print("index:" + str(eleman[0])+ "  value:"+ str(eleman[1]))
    
# random => rastgele sayılar ve öğeler oluşturur.  bir dizi rastgele sayı oluşturma, bir öğe seçme veya karıştırma işlemleri yapar.

from random import randint
print(randint(0, 100))

new_list=list(range(0,10))

#shuffle => karıştırma işlemi yapar.
from random import shuffle

shuffle(new_list)
print(new_list)

#zip =>  birden fazla dizisel elemanın öğelerini birbiriyle eşleştirerek bir zip objesi oluşturur. Her bir eleman tuple tipindedir.

fruit_list=["banana","apple","pineapple"]
calorie_list=[100,200,300]
day_list=["sunday","monday","wednesday"]

zipped_list= list(zip(fruit_list,calorie_list,day_list))

print(zipped_list)

# *args => Sınırsız sayıda parametreli fonksiyon oluşturmak için kullanılır.

def show_number(*numbers):
    print(numbers)

show_number(1,2,34,6)

# **kwargs => Çift yıldızlı (**) parametrelerin tek yıldızlı (*) parametrelerden en önemli farkı, fonksiyonu çağırırken anahtar değer ilişkisiyle çağırabilmemizdir.

# Fonksiyon parametresinden önce çift yıldız(**) kullandığımız için sonucumuz sözlük (dictionary) olarak döner

def function1(**parameter):
    print(parameter)
    
function1(value1="Arzu", value2=27)
function1(value1="Arzu", value2=27, value3=True, value4=15.3)

# *args ve **kwargs birlikte kullanımı

def function(*args, **kwargs):
    for i in args:
        print(i)
    
    for k,v in kwargs.items():
        print("key:",k,"Value:",v)
        
function(1,2,3,'args' , value= 'kwargs')

#Lambda => Lambda tek satırlık fonksiyonlardır. Birden fazla parametre kabul ederler, fakat tek bir işlem yapabilirler.

addition = lambda a, b : a + b
print (addition(5, 6))

#map() => bir liste ya da demet gibi iterasyon yapılabilir veri türlerinin her bir verisini bir fonksiyona tek tek parametre olarak göndermek için kullanılır.

l = [1, 2, 3, 4, 5]
l_square = []
for i in l:
    l_square.append(i**2)
 
print(l)
print(l_square)

l_square = list(map(lambda x: x**2, l))
 
print(l)
print(l_square) 


def multiplication(x):
    return (x*x)
def addition(x):
    return (x+x)

funcs = [multiplication, addition]
for i in range(5):
    values = list(map(lambda x: x(i), funcs))
    print(values)

#filter => Filter bir fonksiyondan True dönen elementler için bir liste oluşturur. fro döngüsüne benzer yerleşik hızlı bir fonksiyondur.

l = list(range(-5, 5))
print(l)
bigger_than_zero_l = list(filter(lambda x: x > 0, l))
print(bigger_than_zero_l)

#reduce => bir liste üzerine bazı hesaplamaları gerçekleştirmek ve bir sonuç döndürmek için çok kullanışlı bir fonksiyondur.

sonuc = 1
l = [1, 2, 3, 4, 5, 6]
for oge in l:
    sonuc *= oge

print(sonuc)


from functools import reduce
l = [1, 2, 3, 4, 5, 6]
sonuc = reduce((lambda x, y: x * y), l)
print(sonuc)
