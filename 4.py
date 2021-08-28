print(5 == 5)
print(6 == 5)
print(6 != 5)
print(4 < 7)
print(2.78 <= 3.14)

print(True & False)
print(True & True)
print((6 > 4) & (5 < 10))
print((5 == 4) | (3 != 4))
x = 45
print((x > 50) | (x % 3 == 0))

if 5 > 4:
    print("Koşul sağlanıyor.")

if 7 == 8:
    print('Koşul sağlanıyor.')

puan = 90
if puan > 85:
    print('Öğrenci geçti.')

if 100:
    print("A value is entered.")

if 0:
    print("A value is entered.")

if "herhangi bir metin":
    print("Herhangi bir metin olabilir.")


puan = 70
if puan > 85:
    print("Öğrenci geçti.")
else:
    print('Öğrenci kaldı.')

grade = 65
if grade > 85:
    letter_grade = "A"
else:
    if grade > 70:
        letter_grade = "B"
    else:
        if grade > 60:
            letter_grade = "C"
        else:
            if grade > 50:
                letter_grade = "D"
            else:
                letter_grade = "F"

print(letter_grade)

grade = 65
if grade > 85:
    letter_grade = "A"
elif grade > 70:
    letter_grade = "B"
elif grade > 60:
    letter_grade = "C"
elif grade > 50:
    letter_grade = "D"
else:
    letter_grade = "F"

print(letter_grade)

x = 1
while x < 10:
    print(x)
    x = x + 1

while True:
    cevap = input("Bir sayı girin (Çıkmak için 0 girin): ")
    print('Girdiğiniz Sayı: ' + cevap)
    if int(cevap) == 0:
        break

for i in range(1, 6):
    print (i ** 2)

list_students = ["Micheal", "Sarah", "Alex", "Baran", "Petros"]
for student in list_students:
    print(student)

list_students = ["Micheal", "Sarah", "Alex", "Baran", "Petros"]
for index, student in enumerate(list_students):
    print(str(index) + ": " + str(student))

countries = ['Greece', 'Turkey', 'Germany', 'Italy', 'France']
capital_cities = ['Athens', 'Ankara', 'Berlin', 'Rome', 'Paris']
countries_capital_cities = zip(countries, capital_cities)
for index, data in enumerate(countries_capital_cities):
    countries, capital_cities = data
    print(index, ": ", countries, capital_cities)

notlar = [['Eren', 100],
['Ilhan', 99],
['Ali', 98],
['Erman', 97],
['Mehmet', 96]
]

for i in notlar:
    print(str(i[0]) + ": " + str(i[1]))

siniflar = [["Ilhan", "Ali"]],
[["Yagiz", "Baran", "Tugce", "Mehmet"]],
[["Selin", "Umut", "Lara", "Ayten", "Murat"]]

for sinif, i in enumerate(siniflar):
    print("Sinif" + ":" + str(sinif + 1))
    for sira, ogrenci in enumerate(i):
        print(str(str(sira + 1) + " : " + str(ogrenci)))
    print("")

not_listesi = {
    'Ilhan' : 75,
    'Ali' : 98,
    'Mehmet' : 83,
    'Yagiz' : 99,
    'Baran' : 68,
    'Özlem' : 89,
    'Ayten' : 74
}

for ogrenci in not_listesi:
    print(ogrenci, not_listesi[ogrenci])

for anahtar, deger in not_listesi.items():
    print(anahtar + ":" + str(deger))

ogrenciler = [
    ('A', 'Ali', '0001'),
    ('A', 'Can', '0002'),
    ('A', 'Eren', '0003'),
    ('B', 'Ayse', '0004'),
    ('B', 'Ilhan', '0005'),
    ('B', 'Baran', '0006'),
    ('C', 'Mehmet', '0007'),
    ('C', 'Yagiz', '0008'),
    ('C', 'Ozlem', '0009'),
]

siniflar = {}

for sinif, ogrenci, numara in ogrenciler:
    if sinif not in siniflar:
        siniflar[sinif] = []
    siniflar[sinif].append((ogrenci, numara))

print(siniflar)

from collections import defaultdict
from typing import Literal

siniflar = defaultdict(list)

for sinif, ogrenci, numara in ogrenciler:
    siniflar[sinif].append((ogrenci, numara))

print(siniflar)

# [3, 4, 5, 6, 7], [10, 9, 8, 7, 6]
# [3, 4, 5, 6, 7] + 3

sehir = "Izmir"
yine = iter(sehir)
print(next(yine))
print(next(yine))
print(next(yine))
print(next(yine))
print(next(yine))
# print(next(yine))

sehir = "Izmir"
yine = iter(sehir)
print(*yine)

for i in range(5):
    print(i)

for i in range(4, 8):
    print(i)

sayilar = range(10, 20)
print(sayilar)

sayilar = range(10, 20)
sayi_listesi = list(sayilar)
print(sayi_listesi)

liste = ['A', 'B', 'C', 'D']
enum = enumerate(liste)
print(type(enum))

print(list(enum))

for indeks, deger in enumerate(liste):
    print(indeks, deger)

for indeks, deger in enumerate(liste, start = 2):
    print(indeks, deger)

countries = ['Turkey', 'Japan', 'Italy']
capitals = ['Ankara', 'Tokio', 'Rome']
countries_capitals = zip(countries, capitals)
print(*countries_capitals)

for country, capital in zip(countries_capitals):
    print(country, capital)

countries = ["Turkey", "Japan", "USA", "Spain", "Italy"]
capitals = ["Ankara", "Tokio", "Washington DC", "Madrid", "Rome"]
countries_capitals = zip(countries, capitals)
countries ,capitals = zip(*countries_capitals)
print(countries)
print(capitals)

kareler = []
for i in range(1, 11):
    kareler.append(i ** 2)
print(kareler)

liste1 = [3, 4, 5, 7, 10, 12]
liste2 = []

for i in liste1:
    liste2.append(i*2)
print(liste2)

kareler = [i ** 2 for i in range(0, 11)]
print(kareler)

liste1 = [3, 4, 5, 7, 10, 12]
liste2 = [i * 2 for i in liste1]
print(liste2)

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
months_shortened = [month[0:3] for month in months] 
print(months_shortened)

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
months_starting_with_M = [month[0:3] for month in months if month[0] == "M"]
print(months_starting_with_M)

cubes = [i ** 3 for i in range(0, 11) if i % 2 == 1]
print(cubes)

squares_cubes = [i ** 3 if i % 2 == 1 else i ** 2 for i in range(0, 11)]
print(squares_cubes)

cities = ["New York", "Los Angeles", "Liverpool", "Istanbul", "Islamabad"]
cities_dictionary = {city : len(city) for city in cities}
print(cities_dictionary)

#1

prg_dilleri = ['Python', 'R', 'Matlab', 'C++', 'C', 'Java', 'Javascript']
i = 0
while i < len(prg_dilleri):
    print(prg_dilleri[i])
    i += 1

list_prg_dilleri = iter(prg_dilleri)
print(*list_prg_dilleri)

#2

liste_1 = [0, 1, 2, 3, 4]
liste_2 = [[liste_1] for i in range(6)]
print(liste_2)

#3

ülkeler = ["Türkiye", "İspanya", 'Çin', 'Irak', 'İtalya', 'Çad']
ülkeler_büyüktür_5 = [ülke[:] for ülke in ülkeler if len(ülke) > 5]
print(ülkeler_büyüktür_5)

#4

# dersler = ["Matematik", "Fizik", "Kimya"]
# ogretmenler = ["Cahit Arf", "Mete Atatüre", "Aziz Sancar"]
# ders_ogretmen = zip(dersler, ogretmenler)

# for sira, cift in zip(ders_ogretmen):
#     print("Ders No: {}\nDers Adı: {}\nDers Öğretmeni: {}".format(list(range(0, 3)),dersler,ogretmenler))

# Yapamadım.

#5

def try_x():
    x = int(input("Enter a number: "))
    if x < 0:
        print(0)
    else:
        print(x)

try_x()

#6

def calculate_Wage():
    hourly_rate = float(input("Enter your hourly income: "))
    hours_amount_week = int(input("Enter the amount of hour you plan to work: "))
    if hours_amount_week < 40:
        print("Invalid entry")
    elif hours_amount_week == 40:
        print(hourly_rate * hours_amount_week * 4)
    else:
        print(hourly_rate * 1.5 * hours_amount_week * 4)

calculate_Wage()

#7

word = input("Enter a word: ")
count = 0
for i in word:
    if i.isupper():
        count += 1
print(count)