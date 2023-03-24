
# bir metnin baş harfi ve son harfi için değişkenin adının sonuna [0], [-1] eklenerek kullanılır

print("hi world")


x = "Zehra'nin mekani"
print(x[3:])  # ra'nin mekani
print(x[:3])   # Zeh
print(x[1:7:2])  # 1 ile 7 arasındaki harfleri 2'şer 2'şer atlayarak verir.
print(x[::-1])  # metni tersten yazdırır. 

#     LİSTELER

myList = [1,2,3,4,5]
myList.remove(2)
myList.append(6) #sona ekleme
myList.count(2)	 #2 sayısının listedeki sayısı miktarı 	
myList.pop()	 # son ekleneni siler yani 6 silinir.
myList.sort()	 # küçükten büyüğe sıralar, bizimki zaten sıralı


myStringList = ["Zehra", "Emir", "Nisa"]
myStringList2 = ["Ali", "Ayşe"]

TotalList = myStringList + myStringList2 
print(TotalList)
TotalList.sort() 
print(TotalList)


#İç içe geçmiş listeler  => nested list

nestedList = ["Zehra", 28, [1,2,3,4], "Emir"]
print(nestedList[3][2])
print(nestedList[1])

print(nestedList[1:3])
print(nestedList[::2])


## DICTIONARY
 
yemekKaloriSözlüğü = {"elma":10, "muz":20, "kivi":30}
print(yemekKaloriSözlüğü["muz"])
print(yemekKaloriSözlüğü.keys())
yemekKaloriSözlüğü["karpuz"] = 40
print(yemekKaloriSözlüğü.keys())
print(yemekKaloriSözlüğü)
 
# SET 
# içerisinde tekil eleman bulunan yapılar
  
