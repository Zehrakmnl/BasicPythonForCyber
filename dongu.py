#Döngüler

myList = [10,20,30,40,50,60]
myList2 = [135,250,307,49,57,123]
myName = "Hatice Zehra Kamanlı"
#For döngüsü 

for x in myList:
    print(x/5*6)

print("\n2. listede tek sayılar yazdırılıyor :\n")
for a in myList2:
    if a%2 ==1:
        print(a)

for letter in myName:
    print(letter)

#siber güvenlikte karşımıza çok çıkabilecek bir örenek 
mixList = [(3,4),(8,2),(9,12),(20,16)]
for (x,y) in mixList:
    print(x)
    print(y)

#bir süreliğine içi boş olacak
for temp in myList:
    pass


#WHILE -> bir şey olduğu sürece
longList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

x = 5
while x > 0:
    print(x)
    x=x-1
    
