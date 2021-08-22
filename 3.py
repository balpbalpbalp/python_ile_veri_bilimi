not_Eren = 100
not_Ilhan = 99
not_Ali = 98
not_Erman = 97
not_Mehmet = 96

notlar = (not_Eren, not_Ilhan, not_Ali, not_Erman, not_Mehmet)
notlar = {"Eren": 100, "Ilhan": 99, "Ali": 98, "Erman": 75, "Mehmet": 96}

# List

liste1 = [41, 42, 43, 44, 45]
print(liste1)

liste2 = ["abc", "def", "xyz", "ijk"]
print(liste2)

liste3 = [123, 456, "klm", "xyz"]
print(liste3)

notlar = ['Eren', 100, 'Ilhan', 99, 'Ali', 98, 'Erman', 97, 'Mehmet', 96]
notlar = [['Eren', 100], 
['Ilhan', 99], 
['Ali', 98], 
['Erman', 97], 
['Mehmet', 96]]
notlar = [['Eren', 'Ilhan', 'Ali', 'Erman', 'Mehmet'],
[100, 99, 98, 97, 96]]
print(notlar)

notlar = [not_Eren, not_Ilhan, not_Ali, not_Erman, not_Mehmet]
notlar = ['Eren', not_Eren, 'Ilhan', not_Ilhan, 'Ali', not_Ali, 'Erman', not_Erman, 'Mehmet', not_Mehmet]
print(notlar)

liste = []

print(type(notlar))

liste = [12, 33, 45, 76, 35, 43, 18, 6, 7]
print(len(liste))

print(liste3[0])
print(liste3[1])
print(liste3[2])
print(liste3[3])
print(type(liste3[0]))
print(type(liste3[2]))

liste = [4, 7, 9 , 12, 15, 19]
print(liste[-1])
print(liste[-2])
print(liste[-3])

print(liste[2:4])
print(liste[0:3])
print(liste[:3])
print(liste[3:])

liste = [4, 7, 9, 12, 15, 19, 3, 6, 8, 12, 13, 11, 2, 5, 9]
print(liste[3:12:2])

notlar = [['Eren', 100], 
['Ilhan', 99], 
['Ali', 98], 
['Erman', 97], 
['Mehmet', 96]]

print(notlar[1][0])
print(notlar[1][1])
(isim, puan) = (notlar[1][0], notlar[1][1])
print(isim)
print(puan)

liste = [1, 2, 3, 4]
liste[3] = 10
print(liste)
liste[0] = 'sayılar'
print(liste)

notlar = ['Eren', 100, 'Ilhan', 99, 'Ali', 98, 'Erman', 97, 'Mehmet', 96]
print(notlar.index('Ali'))
print(notlar.index(98))

liste = ['A', 'B', 'C', 'D', 'E']
print(liste)
sil = liste.pop(3)
print(sil)
print(liste)

olcum_degerleri = [1, 3, 6, 9, 3, 4, 4, 7, 8, 2, 4, 2, 1]
print(olcum_degerleri.count(4))

liste = [1, 2, 3, 10]
liste.append(12)
print(liste)
liste.append(15)
print(liste)

sayilar = [3, 7, 12, 15]
sayilar = sayilar + [19, 23]
print(sayilar)
notlar = notlar + ['Ilker', 76]
print(notlar)

liste1 = [1, 2, 3, 4]
liste2 = ["one", "two", "three", "four"]
liste1.extend(liste2)
print(liste1)

sayilar = [3, 7, 12, 15]
del(sayilar[3])
print(sayilar)

notlar = [100, 93, 86 ,78, 52 , 45, 95]
notlar.remove(100)
print(notlar)

liste = [3, 7, 2, 11, 3, 7, 9, 5, 18, 4]
print(sorted(liste))
print(sorted(liste, reverse = True))

print(notlar.reverse())

numaralar = sayilar + [15]
print(numaralar)

sayilar[0] = 5
print(sayilar)
print(numaralar)

numaralar = sayilar[:]
numaralar = list(sayilar)

print(sayilar[0])
print(numaralar[0])

tuple1 = (3.14, 2.78, 5.67, 2.18)
tuple2 = ('İstanbul', 'Ankara', 'İzmir', 'Bursa', 'Adana')
tuple3 = ('Fizik', 'Matematik', 'Kimya', 100, 99, 97)
print(tuple1[0])
print(tuple2[1:3])

tuple1 = (3.14, 2.78)
pi, e = tuple1
print(pi)
print(e)

zip()

alisveris_listesi  = ['ekmek', 'süt', 'yoğurt', 'pirinç', 'bal', 'meyve', 'ekmek', 'süt']
alisveris = set(alisveris_listesi)
print(alisveris)

alisveris.add('deterjan')
print(alisveris)

yeni_malzemeler = ['sebze', 'gazete', 'dergi']
alisveris.update(yeni_malzemeler)
print(alisveris)

alisveris.discard('ekmek')
print(alisveris)

alisveris.pop()
print(alisveris)
alisveris.pop()
print(alisveris)

alisveris1 = set(['ekmek', 'süt', 'yoğurt', 'peynir'])
alisveris2 = set(['bal', 'şeker', 'tuz', 'ekmek', 'süt'])
print(alisveris1.union(alisveris2))

print(alisveris1.intersection(alisveris2))

print(alisveris1.difference(alisveris2))

