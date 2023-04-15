#  hataları ele almak
# try & except & else & finally  
try:
    a=int(input("num -> "))
except:
    print("Geçerli bir numara giriniz!")
else: 
    print("Geçerli bir numara girildi, teşekkürler")
finally: # her durumda çalışır
    print("Finally worked")

