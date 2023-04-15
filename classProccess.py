# instantiation yani örnekleme terimi istediğimiz objeye belirlenen sınıfın özelliklerini tanımlarkenki kullanıma verilen addır.

from typing import Self


myDictionary = dict() # by şekilde tanımlanır.

# Görecceğimiz terimler -> instance & attribute & instantie & init-initialize
# class oluşturma 
class AslanBurcu():
    Element = ""
    Gezegen = "Gunes"
    Tas_Stone = "Yakut"

Zehra = AslanBurcu()
Zehra.Element = "Ateş"
print(Zehra.Element)


# init metodu 
# class değişkeni oluşturduğumuzda parametre vermek zorunda olma durumunu inceleyelim

class pcProperties():

    def __init__(Self,Marka, Ram) :  # Burada 'self' sabit olarak kullanılmaktadır.
        Self.Marka= Marka
        Self.Ram= Ram
         
    Marka = ""
    Islemci = "Intel"
    Ram = ""
    GarantiSuresi = False

myPC = pcProperties("Asus", "16GB")
print(myPC.GarantiSuresi)
print(myPC.Marka)
print(myPC.Ram)





