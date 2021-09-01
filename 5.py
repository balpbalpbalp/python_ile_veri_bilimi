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

kare = lambda x: x ** 2
print(kare(5))

us = lambda x, y: x ** y
print(us(4, 3))

fahrenheit_cevir = lambda C: 1.8 * C + 32
print(fahrenheit_cevir(35))

tekrarla = lambda kelime, adet: kelime * adet
print(tekrarla("Python ", 3))

def kare(x):
    return x ** 2

sayi = [2, 3, 4, 5]

sonuc = map(kare, sayi)
sonuc_listesi = list(sonuc)
print(sonuc_listesi)

sayilar = [2, 3, 4, 5]
sonuc = list(map(lambda x: x ** 2, sayilar))
print(sonuc)

def tek_sayi(x):

    if x % 2 == 0:
        return False
    else:
        return True

sayilar = [3, 7, 12, 17, 43, 16, 29, 81, 64, 42]
tekler = list(filter(tek_sayi, sayilar))
print(tekler)

sayilar = [3, 7, 12, 17, 43, 16, 29, 81, 64, 42]
sonuc = list(filter(lambda x: x % 2 == 1, sayilar))
print(sonuc)

liste = ['Adiyaman', 'Ankara', 'Balikesir', 'Kahramanmaras', 'Igdir']
iller = list(filter(lambda x: len(x) > 7, liste))
print(iller)

from functools import reduce

ekip = ['Ayten', 'Ali', 'Mehmet', 'Yagiz', 'Baran', 'Özlem']
butun_ekip = reduce(lambda ekip_1, ekip_2: ekip_1 + " " + ekip_2, ekip)
print(butun_ekip)

sayilar = [5, 7, 8, 3, 5]
carpim = reduce(lambda x1, x2: x1 * x2, sayilar)
print(carpim)

def us_alma(x, y):
    sonuc = x ** y
    return sonuc

# print(sonuc) won't work. It is under the local scope of the program.

sonuc = 50
def us_alma(x, y):
    sonuc = x ** y
    return sonuc
print(us_alma(5, 3))
print(sonuc)

us = 3
def us_alma(x):
    sonuc = x ** us
    return sonuc
print(us_alma(5))

us = 3
def us_alma(x):
    global us
    us = us + 1
    sonuc = x ** us
    return sonuc
print(us_alma(5))
print(us)

import builtins
print(dir(builtins))

metin = "python ile programlama ogreniyorum"
print(metin.upper())
liste = [3, 7, 13, 17, 21]
liste.append(37)
print(liste)

liste = [4, 6, 2, 12, 11, 7]
liste_kup = [i ** 3 for i in liste]
print(liste_kup)

liste_kup = (i ** 3 for i in liste)
print(liste_kup)

for x in liste_kup:
    print(x)

liste = [4, 6, 2, 12, 11, 7]
liste_kup = (i ** 3 for i in liste)
print(next(liste_kup))
print(next(liste_kup))
print(next(liste_kup))

# 1

def odd_even_question():

    x = int(input("Enter an integer: "))

    if x % 2 == 0:
        print(f"{x} is an even number.")
    
    else:
        print(f"{x} is an odd number.")
    
# 2 

def word_reverser():

    x = input("Enter a word: ")
    x_letters = []
    index = 0

    while index < len(x):
        x_letters.append(x[index])
        index += 1
    
    x_letters.reverse()
    print(x_letters)

# 3

def word_combiner_capital():

    x = input("Enter the first word: ")
    y = input("Enter the second word: ")
    x_y = x.upper() + y.upper()
    print(x_y)

# 4

numbers_list = list(range(0, 101))
numbers_list_even_numbers = (i % 2 == 0 for i in numbers_list)
print(next(numbers_list_even_numbers))
print(next(numbers_list_even_numbers))
print(next(numbers_list_even_numbers))

# 5

def multiplier_3():

    input_1 = float(input("Enter the first number: "))
    input_2 = float(input("Enter the second number: "))
    input_3 = float(input("Enter the third number: "))

    result = input_1 * input_2 * input_3
    return result

# 6

def fibonacci():

    n_0 = 0
    n_1 = 1
    n_terms = int(input("The number of the terms should be: "))
    n_counter = 0

    while n_counter < n_terms:
        fibo_value = n_0 + n_1
        n_0 = n_1
        n_1 = fibo_value
        n_counter += 1
    
    return fibo_value

print(fibonacci())

# 8

def sort_numbers_list():

    list_numbers = []
    desired_amount_of_entries = int(input("How many numbers would you like to rank? "))
    index = 0

    while index < desired_amount_of_entries:
        list_numbers.append(float(input("Enter a number: ")))
        index += 1
    
    list_numbers.sort(reverse = False)
    print(list_numbers)