#nesne odaklı ilerlerken fonksiyonlara başlıyoruz.
    #Bazi metodlar, kullanimlar hakkinda bilgi edinmek istediğimizde şu şekilde bir kullanim sağlayabliriz.
    #mylist = [1,2,3]
    #help(mylist.extend)

def basicFunc():
    print("Executed basic function")

#farklı bir kullanım örneği
def defaultValue(name="Zehra"):
    # eğer fonksiyon içerisinde name değişkenine bir değer atanmazsa 'Zehra' kullanılır.
    name = input("What is your name?  ")
    print(f"my name is {name}") 
defaultValue()

# input
def inputFunc():
    name = input("who are you?  ")
    print (f"hi {name} nice to meet you")
inputFunc()

# return
def returnFunc(x):
    a=x
    f = 1
    while a>0:
        f = f*a
        a=a-1
    return f
print(returnFunc(5))

# kaç parametre alındığının belirsiz olduğu durumlar için kullanım

def infinityEqual(*args):
    return sum(args)

# belirsiz parametreleri sözlük olarak kayıt altına almak için kullanım
def keyWordsFunc(**kwargs): 
    return(kwargs)
print(keyWordsFunc(apple="red/green",banana="yellow" ))



