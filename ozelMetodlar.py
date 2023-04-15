# https://www.informit.com/articles/article.aspx?p=453682&seqNum=6

# inheritance  -> bir sınıfın özelliklerini başka bir sınıfta kullanmaya izin vermek için...

class Canli():

    def __init__(self):
        print("init worked")
    def method1(self):
        print("method1 worked")
    def method2(self):
        print("method2 worked")
Zehra = Canli()
Zehra.method1()

class Flowers(Canli): # 'Canli' kullanımı kalıtım, inheritance anlamına gelir 
    def __init__(self):
        Canli.__init__(self)
        print("Flower's init worked")
    def color(self):
        print("Blue")

rose = Flowers()
rose.color()
rose.method1()

# polymorphism  -> çok şekillilik
# Kısaca 2 farklı sınıf var. 1 ortak metod kullanıyorlar.

class Kosu():

    def __init__(self,isim):
        self.isim = isim
    def info(self):
        return self.isim + " 250 kalori yakımı sağlar. "
    
class Yuzme():
    def __init__(self,isim):
        self.isim = isim
    def info(self):
        return self.isim + " 350 kalori yakımı sağlar. "
    
kosma = Kosu("Kosma")
yuzme = Yuzme("Yuzme")

sporList = [kosma,yuzme]
for spor in sporList:
    print(spor.info())

# HERKESIN KENDI ISINI YAPMASINI SAGLAMAK TEMEL MOTTOMUZ !!!
