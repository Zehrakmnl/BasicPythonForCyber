# map fonksiyonu
# bir veri dizisini başka bir veri dizisinde kullanımını kolaylaştıran bir fonksiyondur.

"""
    map fonksiyonunu help(map) ile sorduğumuzda
    class map(object)
 |  map(func, *iterables) --> map object
 |
 |  Make an iterator that computes the function using arguments from
 |  each of the iterables.  Stops when the shortest iterable is exhausted........,

    şeklinde bir çikti aliriz.
"""
# iterables -> DİZİYİ TEK TEK GEZEBİLECEĞİMİZ ANLAMINA GELMEKTEDİR.
# BİR DİZİNİN TÜM ELEMANLARINA BİR FONKSİYON UYGULANMAK İSTENMEKTEYSE  
# map(func, *iterables) func YERİNE KULLANILACAK OLAN FONKSİYONU
# iterables YERİNE DE ELEMANLARI KULLANILACAK OLAN DİZİYİ YAZIYORUZ.
# list(map(func, *iterables)) şeklinde kullanımda bir liste haline getirilecektir. 

def devide(x):
    x = x/2
    return x
mixNumList = [46,24,88,32,26,28,97,94]

mapList = list(map(devide,mixNumList))
print(mapList)


# filter fonksiyonu

mixStrList = ["Zehra", "Zara", "Zegra", "Zahra", "Zira", "Hatice Zehra Kamanlı"]
def cehckName(x):
    return "Zehra" in x
filterList = list(filter(cehckName,mixStrList))
print(filterList)

mapStrList = list(map(cehckName,mixStrList))
print(mapStrList)
# burada ikisi arasındaki farkı görebiliyoruz. Filter, true olan değerleri verir.


# lambda fonksiyonu
# genelde tek satırlık anonim fonksiyonlar oluşturur.
# def carpım(x):
#    return x*3
# BU FONKSİYON KULLANIMI YERİNE AŞAĞIDAKİ GİBİ BİR SATIR YAZILABİLİR.

proces = lambda x : x*x
print(proces(4))




