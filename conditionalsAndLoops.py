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
    

