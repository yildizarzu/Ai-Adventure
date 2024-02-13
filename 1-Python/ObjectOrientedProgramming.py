
""" OBJECT ORIENTED PROGRAMMING """

""" #CLASS: Yöntemleri (methods) ve değişkenleri (variables) olan yeniden kullanılabilir bir kod yığını. 
    #İçerisinde metotlar barındıran fonksiyonlar gibi düşünebiliriz.
    #Geleneksel olarak bir sınıf adı CamelCase(ClassName şeklinde) kullanır.

#CONSTRUCTOR: Nesneyi oluşturur. Yapıcı metottur.bir nesne yaratmak için çağrılan özel bir işlev türüdür. 
    #Yeni nesneyi kullanıma hazırlar, genellikle yapıcının gerekli üye değişkenlerini ayarlamak için kullandığı argümanları kabul eder.

#ATTRIBUTE: Class' a özgü yetenek/özellik

#METHODS : OOP'te sınıftan türetilmiş her bir nesneye hizmet eden ve belli bir görevi yerine getiren fonksiyona method denir.
    #Method self parametresi alır ve Class içerisinde yer alır.

#FUNCTIONS: Belirli bir görevi yerine getiren komutlar kümesidir.

#ENCAPSULATION/ KAPSULLEME: Metot veya variable erişimlerini kısıtlamaktır. 
    #Encapsulation yapılan yapılara direkt erişim mümkün değildir. Erişimi get ve set metotlarıyla yapabiliriz.

#INHERITANCE/ KALITIM / MİRAS : Önceden oluşturulmuş bir sınıftan attribute, method vs miras almak kullanmaktır.
    # PARENT CLASS: Miras alınan class
    # CHILD CLASS: Alt class, Parent Class'tan türetilir.
"""

#%% CLASS: Yöntemleri (methods) ve değişkenleri (variables) olan yeniden kullanılabilir bir kod yığını. 
    #İçerisinde metotlar barındıran fonksiyonlar gibi düşünebiliriz.
    #Geleneksel olarak bir sınıf adı CamelCase(ClassName şeklinde) kullanır.

#ATTRIBUTE: Class' a özgü yetenek/özellik



employee1_name= "Arzu"
employee1_age= 27

class Employee:
    #attribute = departman, name, age
    #behaviour = pass
    employee1_departmen= "it"
    

employee1=Employee()
print(employee1.employee1_departmen)

employee1.employee1_departmen="hr"
print(employee1.employee1_departmen)

#%% METHODS : OOP'te sınıftan türetilmiş her bir nesneye hizmet eden ve belli bir görevi yerine getiren fonksiyona method denir.
    #Method self parametresi alır ve Class içerisinde yer alır.
#Square: class
class Square(object):
    
    edge = 8 # edge: attribute
    
    # area:methods. self: object'i ifade eder. object' e ait attribute kullanımını sağlar.
    def area(self):
        area = self.edge * self.edge
        print("Square Area:", area)
        return area

square1=Square()
square1.area()

square1.edge=11
square1.area()

#%% FUNCTIONS: Belirli bir görevi yerine getiren komutlar kümesidir.

#♣Employee: class
class Employee(object):
    
    #attributes
    age=25
    salary=100000
    
    #method
    def ageSalaryRatio(self):
        a=self.age/self.salary
        return a

#function
def ageSalaryRatio(age, salary):
    a=age/salary
    return a


employee1=Employee()
print("Method Ratio:", employee1.ageSalaryRatio())

print("Funtion Ratio:", ageSalaryRatio(30, 100000))

#%% CONSTRUCTOR / INITIALIZER : Nesneyi oluşturur. Yapıcı metottur. Bir nesne yaratmak için çağrılan özel bir işlev türüdür. 
    #Yeni nesneyi kullanıma hazırlar, genellikle yapıcının gerekli üye değişkenlerini ayarlamak için kullandığı argümanları kabul eder.
    #__init__ fonksiyonu constructer'dır. init Classta ilk çalışan metottur. Bu aslında bir sınıf tanımı yapılırken, belirli özellikler ile başlamasını istediğiniz sınıfa tanımlama yapmak için kullanılır.

class Employee(object):
    
    def __init__(self, a,b):
        self.name=a
        self.age=b
        
    def getAge(self):
        return self.age
    
    def getInfo(self):
        return "Name:"+ self.name + " Age:"+ str(self.age)

e1=Employee("Arzu", 27)
print(e1.getAge())
print(e1.getInfo())

e2=Employee("Gokhan", 29)
print(e2.getAge())
print(e2.getInfo())

#%% Hesap Makinesi Örneği

class Calculator(object):
    
    #constructor/initializer
    def __init__ (self, v1,v2):
        
        #attributes
        self.value1=int(v1)
        self.value2=int(v2)
    
    #methods
    def addition(self):
        print("1.Value + 2.Value= ", self.value1 + self.value2)
    
    def subtraction(self):
        print("1.Value - 2.Value= ", self.value1 - self.value2)
    
    def multiplication(self):
        print("1.Value * 2.Value= ", self.value1 * self.value2)
    
    def division(self):
        print("1.Value / 2.Value= ", self.value1 / self.value2)
    


print("Choose addition:1, subtraction:2, multiplication:3, division:4")
selection = input("Select 1, 2, 3, 4 ")

v1 = input("1.Value:")
v2 = input("2.Value:")
c1= Calculator(v1,v2)

def swich(selection):
    
    if(selection=="1"):
        result= c1.addition()
    
    if(selection=="2"):
        result= c1.subtraction()
    
    if(selection=="3"):
        result= c1.multiplication()
    
    if(selection=="4"):
        result= c1.division()
    else: 
        print("unacceptable choice")

swich(selection)

#%% ENCAPSULATION/ KAPSULLEME: Metot veya variable erişimlerini kısıtlamaktır. 
    #Encapsulation yapılan yapılara direkt erişim mümkün değildir. Erişimi get ve set metotlarıyla yapabiliriz.



class BankAccount(object):
    
    def __init__(self, name, money, address):
        self.name=name #default olarak global tanımlanır.
        self.__money=money # attribute önüne __ koyarak private tanımlayabiliriz yani encapsulation yapabiliriz
        self.address=address
        
    #Encapsulation yapılan yapılara direkt erişim mümkün değildir. Erişimi get ve set metotlarıyla yapabiliriz.
    
    #Money değerini getir
    def getMoney(self):
        return self.__money
    
    #yeni money değerini ata
    def setMoney(self, amount):
        self.__money = amount
    
    #private method
    def __increase(self):
        self.__money = self.__money + 500


person1= BankAccount("Arzu", 1000, "istanbul")

#hata vercektir. money attribute private olduğu için direkt değer atanamaz veya görüntülenemez.
#print("get money: ", person1.__money)
#person1.__money=2000

print("get money: ", person1.getMoney())

person1.setMoney(5000)

print("after set method: ", person1.getMoney())

#person1.__increase()
#print("after set method: ", person1.getMoney())

#%% INHERITANCE/ KALITIM / MİRAS : Önceden oluşturulmuş bir sınıftan attribute, method vs miras almak kullanmaktır.
    # PARENT CLASS: Miras alınan class
    # CHILD CLASS: Alt class, Parent Class'tan türetilir.
    
    