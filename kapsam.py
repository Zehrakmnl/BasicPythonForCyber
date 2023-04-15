# scope - kapsam
# python burada bazı kurallara bakıyor bunlar:
# Local -> enclosing -> Global -> Built-In
# bu sıra ile kontrol gerçekleşiyor. Konumları aşağıda yorum satırı olarak verilmiştir.
# bilginin nereden alınacağını belirledik.

myName = "Zehra"
#global
def nameFunction1():
    myName = "Zara"
    #enclosing
    def nameFunction2():
        myName = "Zeğra"
        #local
        print(myName)
    
    nameFunction2()
nameFunction1()

# eğer bu 3 konumda da bir tanımlama yapılmamışsa istenen değişken için 
# o zaman python'da tanımlanmış olup olmadığına baılıyor. Yani Built-in

# local içerisindeki tanımlama kaldırılırsa...

myName = "Zehra"
#global
def nameFunction1():
    myName = "Zara"
    #enclosing
    def nameFunction2():
        #local
        print(myName)

    nameFunction2()
nameFunction1()

#enclosing içerisindeki tanımlama kaldırılırsa...

myName = "Zehra"
#global
def nameFunction1():    
    def nameFunction2():
        print(myName)

    nameFunction2()
nameFunction1()