""" SYNTAX ERRORS """
# %% syntax error
print(9)
# print 9

int(10.0)
# int 10.0

i = 0
while(i<10):
    print(i)
    i = i+1
    
# %%  exceptions 
a = 10
b = "2"
liste = [1,2,3]
print(sum(liste))
# print(a+b) 
print(str(a)+b)

k = 10
zero = 0
print(k)
#a = k/zero # hata

if(zero==0):
    a = 0
else:
    a = k/zero
    
try: 
    a = k/zero
except ZeroDivisionError:
    a = 0
    
# index error
list1 = [1,2,3,4]
#list1[15]

# module not found error
#import numpyy 

# file not found error
import pandas as pd
#pd.read_csv("asd")

# type error
#"2" + 2

# value error
#int("sad")

try:
    1/1
except:
    print("except")
else:
    print("else")
finally:
    print("done")
    
#%%  Exception Handling

"""Exception =>	Tüm hataların temel sınıftır.
StopIteration =>	Bir iterasyonun next() metodu bir nesneyi göstermediğinde oluşur.
SystemExit =>	sys.exit() fonksiyonu tarafından oluşur.
StandardError =>	StopIteration ve SystemExit dışındaki tüm yerleşik istisnalar için temel sınıftır.
ArithmeticError =>	Sayısal hesaplamalar için ortaya çıkan tüm hatalar için temel sınıftır.
OverflowError =>	Bir hesaplama, sayısal bir tür için maksimum sınırı aştığında oluşur.
FloatingPointError =>	Float hesaplama başarısız olduğunda oluşur.
ZeroDivisionError =>	Sıfıra bölme veya mod alma işleminde ortaya çıkar.
AssertionError =>	Assert ifadesinin başarısız olması durumunda ortaya çıkar.
AttributeError =>	Öznitelik referansı veya atamasının başarısız olması durumunda ortaya çıkar.
EOFError =>	raw_input() veya input() fonksiyonundan girdi olmadığında ve dosyanın sonuna ulaşıldığında ortaya çıkar.
ImportError	=> Bir import işlemi başarısız olduğunda oluşur.
KeyboardInterrupt =>	Kullanıcı program yürütmeyi kestiğinde (genellikle Ctrl + c tuşlarına basıldığında) ortaya çıkar.
LookupError =>	Tüm arama hataları için temel sınıftır.
IndexError =>	Bir sıralı yapıda (list veya tüple gibi) indeks bulunmadığı zaman ortaya çıkar.
KeyError =>	Bir dictionary’de belirli bir anahtar bulunmadığı zaman ortaya çıkar.
NameError =>	Bir tanımlayıcı yerel veya global isim uzayında bulunmadığı zaman ortaya çıkar.
UnboundLocalError =>	Bir fonksiyon veya metotta yerel bir değişkene erişmeye çalışırken ortaya çıkar, ancak bu değişkene değer atanmamıştır.
EnvironmentError =>	Python çevresinin dışında ortaya çıkan tüm istisnalar için temel sınıftır.
IOError =>	Var olmayan bir dosyayı açmaya çalışırken, yazdırma sırasında veya open() fonksiyonu gibi bir giriş / çıkış işlemi başarısız olduğunda ortaya çıkar. Bir anlamda işletim sistemi ile ilgili sorunlar olarak düşünülebilir.
SyntaxError =>	Python sözdiziminde bir hata olduğunda oluşur.
IndentationError =>	Girinti düzgün şekilde belirtilmediğinde ortaya çıkar.
SystemError =>	Python yorumlayıcısı bir iç sorun bulduğunda ortaya çıkar, ancak bu hatayla karşılaşıldığında yorumlayıcı yorumlama işlemine devam eder.
SystemExit =>	Python yorumlayıcısı sys.exit() fonksiyonunu kullanarak bırakıldığında ortaya çıkar. Kodda ele alınmazsa, yorumlayıcı program çalışmasını bırakır.
TypeError =>	Belirtilen veri türü için geçersiz olan bir fonksiyon veya işlem denendiğinde oluşur.
ValueError =>	Bir veri türü için yerleşik fonksiyon geçerli bir argüman türüne sahip olduğunda ortaya çıkar, ancak argümanların belirtilen geçersiz değerleri vardır.
RuntimeError =>	Oluşturulan bir hata herhangi bir kategoriye girmediğinde oluşur.
NotImplementedError =>	Kalıtımlı bir sınıfta uygulanması gereken soyut (abstract) bir yöntem gerçekte uygulanmadığında ortaya çıkar.
"""