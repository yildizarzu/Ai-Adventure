
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
        # PARENT CLASS: Super Class, Miras alınan class
        # CHILD CLASS: Sub Class, Alt class, Parent Class'tan türetilir.
        
    #ABSTRACT CLASS: OOP'de nesnesi yaratılamayan Class'lardır. Sub class/ child class'lar için template/şablon görevi görürler.
        #Super Class'ta Abstract metot olan metotlar Sub Class'ta da kullanılmak zorundadır.
        #Abstract metotlar içeren Class'lardan direkt nesne türetilemez.
    
    #OVERRIDING: Geçersiz kılmaktır. 
        Super Class ve Sub Class'ta aynı isme sahip metotlar olduğunda Sub Class'taki metot öncelikli çalışır.
    
    #POLYMORPHISM: Çok şekillilik/çeşitlilik. Aynı isimde farklı işlevler gören Class'lar. Super Class'ta olan bir metot Sub Class'ta da var ve değerleri farklı ise bu Polymorphism'dir.

    #Constant Variable: Sonucu değişmeyen her yerde aynı variable. Büyük Harflerle yazılır.  
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
    # super().__init__()  PArent class'ın init metoduna erişebilmeyi sağlar.
    
class Animal():
    def __init__(self):
        print("Animal created")
    
    def display(self):
        print("Animal")
        
    def walk(self):
        print("animal walk")
        
class Monkey(Animal):
    def __init__(self):
    
        #super() : parent class'ın init metoduna erişebilmeyi sağlar.
        super().__init__()
        print("Monkey is created")
    
    def display(self):
        print("Monkey")
        
    def climb(self):
        print("Monkey can climb")

class Bird(Animal):
    def __init__(self):
    
        #super() : parent class'ın init metoduna erişebilmeyi sağlar.
        super().__init__()
        print("Bird is created")
    
    def display(self):
        print("Bird")
        
    def fly(self):
        print("Bird can fly")

monkey1=Monkey()
monkey1.walk()
monkey1.climb()

bird1=Bird()
bird1.walk()
bird1.fly()

#%% INHERITANCE EXAMPLE

#Super, Parent Class
class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        
    def display(self):
        print(self.name+ " "+self.surname)

# Sub, Child Class
class Employee(Person):
    
    def __init__(self, name, surname, salary):
        
        #super().__init__(name, surname)  // Person.__init__(self, name, surname) ile aynı iş
        Person.__init__(self, name, surname)
        
        self.salary = salary
        
    def display(self):
        print(self.name+ " "+self.surname+" "+str(self.salary))
        
        
        
person1=Person("Arzu", "Toprak")
person1.display()
employee1=Employee("Gökhan", "Toprak",100)
employee1.display()
        

#%% ABSTRACT CLASS:  Sub class/ child class'lar için template/şablon görevi görürler.
#Super Class'ta Abstract metot olan metotlar Sub Class'ta da kullanılmak zorundadır.
#Abstract metotlar içeren Class'lardan direkt nesne türetilemez.

from abc import ABC, abstractmethod

class Animal(ABC): #Super class

     @abstractmethod
     def walk(self): pass
     
     @abstractmethod
     def run(self): pass
 
class Bird(Animal): #Sub Class

      def __init__(self):
          print("bird")
    
    #Super Class'ta Abstract metot olan metotlar Sub Class'ta da kullanılmak zorundadır.
      def walk(self):
          print("walk")
          
      def run(self):
          print("run")
          
#Abstract metotlar içeren Class'lardan direkt nesne türetilemez.
#animal1= Animal()
bird1=Bird()


#%%OVERRIDING: Geçersiz kılmaktır. Super Class ve Sub Class'ta aynı isme sahip metotlar olduğunda Sub Class'taki metot öncelikli çalışır.

class Animal: #parent

    def toString(self):
        print("Animal")
 
class Monkey(Animal): #parent

    def toString(self):
        print("Monkey")
    
animal1= Animal()
animal1.toString()

monkey1=Monkey()
monkey1.toString() #Monkey toString metodu Animal'ın toString metodunu Overridding ediyor. Geçersiz kılıyor.

        
#%% POLYMORPHISM: Çok şekillilik/çeşitlilik Super Class'ta olan bir metot Sub Class'ta da var ve değerleri farklı ise bu Polymorphism'dir.
    
class Employee:
    
    def raisee(self):
        raise_rate = 0.1
        return 100+100*raise_rate
    
class ComputerEngineer(Employee):
    
    def raisee(self):
        raise_rate = 0.2
        return 100+100*raise_rate
        
        
class Teacher(Employee):
    
    def raisee(self):
        raise_rate = 0.3
        return 100+100*raise_rate
        
employee1=Employee()
print(employee1.raisee())

computer_enginner=ComputerEngineer()
print(computer_enginner.raisee())

teacher1=Teacher()
print(teacher1.raisee())

#%% OOP EXAMPLE
from abc import ABC, abstractmethod

#INHERITANCE
class Shape(ABC): #Super/Parent Class
    
    #abstract method
    @abstractmethod
    def area(self):
        pass
    
    #abstract method
    @abstractmethod
    def perimeter(self):
        pass
    
    #Overriding and polymorphism
    def toString(self):
        print("Shape")
        
class Square(Shape): #Sub/Child Class
    
    def __init__(self,side):
        self.__side= side  #Encapsulation private Attribute
        
    def area(self):
        return self.__side**2
    
    def perimeter(self):
        return self.__side*4
    
    #Overriding and polymorphism
    def toString(self):
        print("Square")
        
class Circle(Shape): #Sub/Child Class
    
    #Constant Variable: Sonucu değişmeyen her yerde aynı variable
    PI = 3.14
    
    
    def __init__(self,radius):
        self.__radius= radius  #Encapsulation private Attribute
        
    def area(self):
        return self.PI * self.__radius**2  #pi*r^2
     
    def perimeter(self):
        return 2 * self.PI * self.__radius  #2*pi*r
    
    #Overriding and polymorphism
    def toString(self):
        print("Circle")
        
        
circle1=Circle(5)
print(circle1.area())
print(circle1.perimeter())
print(circle1.toString())
        
  
square1=Square(5)
print(square1.area())
print(square1.perimeter())
print(square1.toString())
  

#%% OOP EXAMPLE 2

import datetime


#Parent Class
class VehicleRent:

    def __init__(self, stock):
        self.stock = stock
        self.now = 0
    
    def displayStock(self):
        print("{} vehicle available to rent".format(self.stock))
        return self.stock
    
    def rentHourly(self, n):
        
        if n <= 0:
            print("Number should be positive")
            return None
        
        elif n > self.stock:
            print("Sorry, {} vehicle available to rent".format(self.stock))
            return None
        
        else:
            self.now = datetime.datetime.now()
            print("Rented a {} vehicle for hourly at {} hours".format(n,self.now.hour))
            
            self.stock -= n 
            
            return self.now
    
    def rentDaily(self, n):
        
        if n <= 0:
           print("Number should be positive")
           return None
       
        elif n > self.stock:
           print("Sorry, {} vehicle available to rent".format(self.stock))
           return None
       
        else:
           self.now = datetime.datetime.now()
           print("Rented a {} vehicle for daily at {} hours".format(n,self.now.hour))
           
           self.stock -= n 
           
           return self.now
       
    def returnVehicle(self, request,brand):
        
        car_hour_price = 10
        car_day_price = car_hour_price*8/10*24
        bike_hour_price = 5
        bike_day_price = bike_hour_price*7/10*24
        
        rentalTime, rentalBasis, numOfVehicle = request
        bill = 0
        
        if brand == "car":
            if rentalTime and rentalBasis and numOfVehicle:
                self.stock += numOfVehicle
                now = datetime.datetime.now()
                rentalPeriod = now - rentalTime 
                
                if rentalBasis == 1: # hourly
                    bill = rentalPeriod.seconds/3600*car_hour_price*numOfVehicle
                
                elif rentalBasis == 2: # daily
                    bill = rentalPeriod.seconds/(3600*24)*car_day_price*numOfVehicle
                    
                if (2 <= numOfVehicle):
                    print("You have extra 20% discount")
                    bill = bill*0.8
                
                print("Thank you for returning your car")
                print("Price: $ {}".format(bill))
                return bill
        elif brand == "bike":
            if rentalTime and rentalBasis and numOfVehicle:
                self.stock += numOfVehicle
                now = datetime.datetime.now()
                rentalPeriod = now - rentalTime 
                
                if rentalBasis == 1: # hourly
                    bill = rentalPeriod.seconds/3600*bike_hour_price*numOfVehicle
                
                elif rentalBasis == 2: # daily
                    bill = rentalPeriod.seconds/(3600*24)*bike_day_price*numOfVehicle
                    
                if (4 <= numOfVehicle):
                    print("You have extra 20% discount")
                    bill = bill*0.8
                
                print("Thank you for returning your bike")
                print("Price: $ {}".format(bill))
                return bill
        else:
            print("You do not rent a vehicle")
            return None
    
    
#Child Class
class CarRent(VehicleRent):
    
    global discount_rate
    discount_rate = 15
    
    def __init__(self,stock):
        super().__init__(stock)
        
        
    def discount(self,b):
        bill = b - (b*discount_rate)/100
        return bill
    
class BikeRent(VehicleRent):
    
    def __init__(self, stock):
        super().__init__(stock)
    
class Customer:
    
    def __init__(self):
        self.bikes = 0
        self.rentalBasis_b = 0
        self.rentalTime_b = 0
        
        self.cars = 0
        self.rentalBasis_c = 0
        self.rentalTime_c = 0
        
        
    def requestVehicle(self, brand):
        
        if brand == "bike":
            bikes = input("How many bikes would you like to rent?")
            
            try:
                bikes = int(bikes)
            except ValueError:
                print("Number should be Number")
                return -1
            
            if bikes < 1:
                print("Number of Bikes should be greater than zero")
                return -1
            else:
                self.bikes = bikes
            return self.bikes
            
        elif brand == "car":
            cars = input("How many cars would you like to rent?")
            
            try:
                cars = int(cars)
            except ValueError:
                print("Number should be Number")
                return -1
            
            if cars < 1:
                print("Number of cars should be greater than zero")
                return -1
            else:
                self.cars = cars
            return self.cars
            
        else:
            print("Request vehicle error")
    
    
    def returnVehicle(self,brand):
        
        if brand == "bike":
            if self.rentalTime_b and self.rentalBasis_b and self.bikes:
                return self.rentalTime_b, self.rentalBasis_b,  self.bikes
            else:
                return 0,0,0
        elif brand == "car": 
            if self.rentalTime_c and self.rentalBasis_c and self.cars:
                return self.rentalTime_c, self.rentalBasis_c,  self.cars
            else:
                return 0,0,0
        else:
            print("Return vehicle Error")
    

bike = BikeRent(100)
car = CarRent(10)
customer = Customer()

main_menu = True

while True:
    
    if main_menu:
        print("""
              ***** Vehicle Rental Shop*****
              A. Bike Menu
              B. Car Menu
              Q. Exit
              """)
        main_menu = False
        
        choice = input("Enter choice: ")
        
    if choice == "A" or choice == "a":
        
        print("""
              ****** BIKE MENU*****
              1. Display available bikes
              2. Request a bike on hourly basis $ 5
              3. Request a bike on daily basis $ 84
              4. Return a bike
              5. Main Menu
              6. Exit
              """)
        choice = input("Enter choice: ")
        
        try:
            choice = int(choice)
        except ValueError:
            print("It is not integer")
            continue
        
        if choice == 1:
            bike.displayStock()
            choice = "A"
        elif choice == 2:
            customer.rentalTime_b = bike.rentHourly(customer.requestVehicle("bike"))
            customer.rentalBasis_b = 1
            main_menu = True
            print("----------------")
        elif choice == 3:
            customer.rentalTime_b = bike.rentDaily(customer.requestVehicle("bike"))
            customer.rentalBasis_b = 2
            main_menu = True
            print("----------------")
        elif choice == 4:
            customer.bill = bike.returnVehicle(customer.returnVehicle("bike"),"bike")
            customer.rentalBasis_b, customer.rentalTime_b, customer.bikes = 0,0,0
            main_menu = True
        elif choice == 5:
            main_menu = True
        elif choice ==6:
            break
        else:
            print("Invalid input. Please enter a number between 1-6 ")
            main_menu = True
        
    elif choice == "B" or choice == "b":
        
        print("""
              ****** CAR MENU*****
              1. Display available cars
              2. Request a car on hourly basis $ 10
              3. Request a car on daily basis $ 192
              4. Return a car
              5. Main Menu
              6. Exit
              """)
        choice = input("Enter choice: ")
        
        try:
            choice = int(choice)
        except ValueError:
            print("It is not integer")
            continue
        
        if choice == 1:
            car.displayStock()
            choice = "B"
        elif choice == 2:
            customer.rentalTime_c = car.rentHourly(customer.requestVehicle("car"))
            customer.rentalBasis_c = 1
            main_menu = True
            print("----------------")
        elif choice == 3:
            customer.rentalTime_c = car.rentDaily(customer.requestVehicle("car"))
            customer.rentalBasis_c = 2
            main_menu = True
            print("----------------")
        elif choice == 4:
            customer.bill = car.returnVehicle(customer.returnVehicle("car"),"car")
            customer.rentalBasis_c, customer.rentalTime_c, customer.cars = 0,0,0
            main_menu = True
        elif choice == 5:
            main_menu = True
        elif choice ==6:
            break
        else:
            print("Invalid input. Please enter a number between 1-6 ")
            main_menu = True
        
    elif choice == "Q" or choice == "q":  
        break
    
    else:
        print("Invalid Input. Please Enter A-B-Q")
        main_menu = True
    print("Thank you for using the vehicle rental shop")
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        