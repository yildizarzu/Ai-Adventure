"""CONDITIONALS"""

#%%%
#IF- ELSE Statement
var1 = 10
var2 = 20

if(var1 > var2):
    print("var1 buyuktur var2")
elif(var1 == var2):
    print("var and var2 esitler")
else:
    print("var1 kucuktur var2")
    

liste = [1,2,3,4,5]

value = 3
if value in liste:
    print("evet {} degeri listenin icinde".format(value))
else:
    print("hayir")

dictionary = {"ali":32,"veli":45,"ayse":13}
keys = dictionary.keys()

if "can" in keys:
    print("evet")
else:
    print("hayir")


a,b=5,7

x = "a buyuk" if a > b else "a eşit veya küçük"

print(x)

x=a>b and "a buyuk" or "a eşit veya küçük"

print(x)
data={ "NAME":["arzu","gokhan","eren","ali","gizem","orhan"],
              "AGE":[27,29,22,31,21,31],
              "SALARY":[100,150,240,350,400,450]}

data["maas_seviyesi"] = ["dusuk" if 200 > each else "yuksek" for each in data["SALARY"]]

  
#%%
#FOR LOOP
for each in range(1,11):
    print(each)
    
for each in "ankara ist":
    print(each)
    
for each in "ankara ist".split(): 
    print(each)
    
liste = [1,4,5,6,8,3,3,4,67]
 
summation = sum(liste)    

count = 0
for each in liste:
    count = count + each
    print(count)
    

liste2 = [numara ** 5 for numara in list(range(0,10))]
print(liste2)

#break=> geçerli döngüyü sonlandırır.
for harf in 'Python':
   if harf == 'h':
      break
   print('Geçerli harf :', harf)
 
#continue => Continue şartı gerçekleşince altta kalan tüm ifadeler atlanıp döngünün başına gidilir.
for harf in 'Python':
   if harf == 'h':
      continue
   print('Geçerli harf:', harf)

#pass => Continue ifadesi gerçekleştiği anda döngünün başına gidilirken pass ifadesinin bulunduğu blok içindeki kodlar çalışmaya devam eder.
for harf in 'Python':  
   if harf == 'h':
      pass
      print('Bu pass bloğu içinde')
   print('Geçerli harf:', harf)
#%%
# WHILE LOOP
liste = [1,4,5,6,8,3,3,4,67]
 
i = 0
while(i <4):
    print(i)
    i = i + 1


sinir = len(liste)   
each = 0
count = 0
while(each < sinir):
    count = count + liste[each]
    each = each + 1 

while(1):
    print("sonsuz döngü")
 
#break=> geçerli döngüyü sonlandırır.
var = 10
while var > 0:              
   print('Geçerli değer :', var)
   var = var -1
   if var == 5:
      break

#continue => Continue şartı gerçekleşince altta kalan tüm ifadeler atlanıp döngünün başına gidilir.
var = 10                    # İkinci örnek
while var > 0:              
   var = var - 1
   if var == 5 or var == 8:
      continue
   print('Geçerli değer :', var)   