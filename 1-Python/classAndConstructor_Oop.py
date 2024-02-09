""" OBJECT ORIENTED PROGRAMMING """
#%%

"""CLASS - CONSTRUCTOR"""

#Class: Yöntemleri (methods) ve değişkenleri (variables) olan yeniden kullanılabilir bir kod yığını. 
#İçerisinde metotlar barındıran fonksiyonlar gibi düşünebiliriz.
#Geleneksel olarak bir sınıf adı CamelCase(ClassName şeklinde) kullanır.
#Constructor: Nesneyi oluşturur. Yapıcı metottur.bir nesne yaratmak için çağrılan özel bir işlev türüdür. 
#Yeni nesneyi kullanıma hazırlar, genellikle yapıcının gerekli üye değişkenlerini ayarlamak için kullandığı argümanları kabul eder.

#%% 
#Tanımlayacağınız bütün sınıfların __init__() method’u vardır. 
#init Classta ilk çalışan metottur. Bu aslında bir sınıf tanımı yapılırken, belirli özellikler ile başlamasını istediğiniz sınıfa tanımlama yapmak için kullanılır.

class Calisan:
    zam_orani = 1.8
    counter = 0
    
    def __init__(self, isim, soyisim,maas): #Constructor
        self.isim=isim
        self.soyisim=soyisim
        self.maas=maas
        self.email=isim+soyisim+"asd.com"
        
    def giveNameSurname(self):
        return self.isim +" "+ self.soyisim
    
    def zam_yap(self):
        self.maas = self.maas + self.maas*self.zam_orani
        
isci1 = Calisan("Arzu", "Yildiz", 100)
print(isci1.giveNameSurname())

# class variable
calisan1 = Calisan("ali", "veli",100) 
print("ilk maas: ",calisan1.maas)
calisan1.zam_yap()
print("yeni maas: ",calisan1.maas)

calisan2 = Calisan("ayse", "hatice",200) 
calisan3 = Calisan("ayse", "yelda",600) 
calisan4 = Calisan("eren", "hilal",500) 


#  class example
liste  = [calisan1,calisan2,calisan3,calisan4]


maxi_maas = -1
index = -1
for each in liste:
    if(each.maas>maxi_maas):
        maxi_maas = each.maas
        index = each
        
print(maxi_maas)
print(index.giveNameSurname())
