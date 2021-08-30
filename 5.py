x = [3, 5, 6, 7, 8, 9, 12, 15, 20]
print(x)

print((3 + 5 + 6 + 7 + 8 + 9 + 12 + 15 + 20) / 9)

print((x[0] + x[1] + x[2] + x[3] + x[4] + x[5] + x[6] + x[7] + x[8]) / 9)

x = [3, 5, 6, 7, 8, 9, 12, 15, 20]
adet = 0
toplam = 0
for i in x:
    adet += 1
    toplam += i
    ortalama = toplam / adet
print(ortalama)

def tebrikler():
    print("Tebrikler, ilk fonksiyon.")

tebrikler()

def bes_kati(x):
    y = 5 * x
    print(y)

bes_kati(12)

def bes_kati(x):
    y = 5 * x
    return y
k = bes_kati(12)
print(k)

def ortalama(liste):
    adet = 0
    toplam = 0

    for i in liste:
        adet += 1
        toplam += i
    
    ortalama_1 = toplam / adet
    return ortalama_1

print(ortalama(x))

liste = [1, 4, 6, 7, 12, -5]
x = max(liste)
y = min(liste)

def kare_al(x):
    return x ** 2

print(kare_al(12))

def us_alma(x, y):
    return x ** y

print(us_alma(x = 4, y = 3))
print(us_alma(4, 3))

def us_alma(x, y = 2):
    return x ** y

print(us_alma(13))
print(us_alma(3, 3))

def carpim(*args):
    sonuc = 1
    for sayi in args:
        sonuc = sonuc * sayi
    print(sonuc)

carpim(2, 3, 4)
carpim(2, 3, 4, 5, 6)

def birlestir(*args):
    sonuc = ""
    for kelime in args:
        sonuc = sonuc + kelime
    return sonuc

print(birlestir("Millet ", "Meclisi"))
print(birlestir("Büyük ","Millet ", "Meclisi"))
print(birlestir("Türkiye ","Büyük ","Millet ", "Meclisi"))

def yaz(ilk, *args):
    print("Ilk Arguman: " + ilk)
    for kelime in args:
        print("Esnek Argüman: " + kelime)

yaz("Ilker")
yaz("Ilker", "Eren")
yaz("Ilker", "Huseyin", "Eren")

def not_yazdir(**kwargs):
    for key, value in kwargs.items():
        print(key + " : " + value)

not_yazdir(Name = "Michael", Surname = "Kelly")
not_yazdir(Name = "Michelle", Surname = "Arnold", Job = "Investment Banker")

def us_alma(x, a, b):
    us_1 = x ** a
    us_2 = x ** b
    sonuc = (us_1, us_2)
    return(sonuc)

print(us_alma(3, 2, 4))
t, k = us_alma(3, 2, 4)
print(t, k)
sonuc = (t, k) = us_alma(3, 2, 4)
print(sonuc)

# Celsius = Kelvin + 273.15
# Fahrenheit = 1.8 * Celsius + 32

def kelvin_fahrenheit(derece):
    
    def kelvin_celsius(kelvin_derece):
        celsius_derece = kelvin_derece + 273.15
        return celsius_derece
    
    fahrenheit = 1.8 * kelvin_celsius(derece) + 32
    return(fahrenheit)

print(kelvin_fahrenheit(-273.15))

def us_al(n):

    def ussu(x):
        sonuc = x ** n
        return sonuc
    
    return ussu

kare = us_al(2)
kup = us_al(3)
print(kare(5))
print(kup(5))