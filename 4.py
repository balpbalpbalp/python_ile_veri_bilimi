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

