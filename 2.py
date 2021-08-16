print(18 + 7)
print(81 -17)
print(12 * 6)
print(96 / 12)

a = 12
print(a)
print(a ** 2)

print("Python öğreniyorum.")

# + = Toplama
# - = Çıkarma
# / = Bölme
# * = Çarpma
# % = Mod Alma
# ** = Üs Alma
# // = Tam Sayı Bölme

print(7 ** 2)
print (12 == 12)
print(13.5 == 12.5)
print(2.78 <= 3.14)

print(3 ** 2 * 4)
print(3 ** (2 * 4))
print(5 + 4 / 2)
print((5 + 4) / 2)

print(5 / 2)
print(10 // 3)
print(23 // 3)

print(5 ** 2)# Üs Alma
print(13 % 3) # Mod Alma
# Tam Sayı Bölme
print(15 // 4)

""" Birden fazla satıra
yayılmış açıklama cümlesi mevcuttur.
Lütfen bir sayı girin.
"""
x = input("Karesi alınacak bir sayı girin: ")
print(float(x) ** 2)

isim = "Baran Alp Narinoğlu"
pi = 3.14
x = 18

a, b = 3.14, 2.78
print(a)
print(b)

[x, y, z] = [7, 8, 9]
print(x)
print(y)
print(z)

# int = Tam Sayı
# float = Gerçel Sayo
# string = Metin
# None = Boş
# bool = Doğru, Yanlış
# complex = Karmaşık

print(100) # Onluk
print(0b100) # İkilik
print(0o100) # Sekizlik
print(0x100) # On Altılık

print(int(-3.999))
print(int(4.2))
print(int(-2.78))
print(int(-7.99))

print(int('1807'))

print(int('1010', 2))
print(int('A0', 16))
print(int('100', 4))

print(type(17))

print((10).bit_length()) # Bit Boyutu
print((1000000000).bit_length())

print(3.14)
print(2.7818)

print(4e12) # Bilimsel Notasyon

print(float(11))
print(float('18.07'))

print(3 +4j)
print(2 - 3j)
print(type(1 + 1j))
print(5 + 3j + 3 - 2j)

print(complex(4, 3))
print(complex(2.7, 3.2))

x = None
print(x)

print(bool(0))
print(bool(-3))
print(bool(4.12))

print(bool(None))

print(True + True)
print(True + False)
print(True * False)

print("birinci " "ikinci " "üçüncü ")

il = "İzmir"
print(il[0])
print(il[1])
print(il[2])
print(il[3])
print(il[4])

print("Python " + "öğreniyorum" + "!")

x = 12345
print(type(x))
y = str(x)
print(y)
print(type(y))

print("""Python'da metinler
... birden fazla satıra
... yazılabilir.
""")
print("Python'da metinler\nbirden fazla satıra\nyazılabilir.")

metin = "Python \t ile \t Programla"
print(metin)

dir = r"C:\users\balp\Desktop" # r = Raw Text
print(dir)

name = "Guido "
surname = "Van Rossum"
name_surname = name + surname
print(name_surname)

dil = "Python"
dil_3 = dil * 3
print(dil_3)

isim = "baran alp narinoğlu"
isim = isim.title()
print(isim)

isim = isim.capitalize()
print(isim)

isim = isim.upper()
print(isim)

isim = isim.lower()
print(isim)

text = "    I am learning Python.   "
print(text)
text = text.rstrip()
print(text)
text = text.lstrip()
print(text)
text = text.strip()
print(text)

text = "I am learning Python."
text = text.split()
print(text)

metin = "Los Angeles Miami Dallas"
metin = metin.replace("Dallas", "Atlanta")
print(metin)

metin = "Los Angeles Miami Dallas Dallas"
metin = metin.replace("Dallas", "Atlanta", 1)
print(metin)

metin = "Los Angeles Miami Dallas Dallas"
print(metin.count("Dallas"))

kelime = "Türkiye"
print(kelime.startswith("T"))
print(kelime.endswith("a"))

kelime = "Programlama"
print(kelime.find("r"))
print(kelime.find("ml"))
print(kelime.find("f"))

x = "Baran"
print(x.islower())
print(x.istitle())
x = "234"
print(x.isnumeric())

print(b"bytesverisi")

text = b"Python Programming Language"
text = text.split()
print(text)

metin = "İ ı Ş ş Ğ ğ Ö ö Ç ç Ü ü"
print(metin)
bytel = metin.encode("utf-8")
print(bytel)
bytel_2 = bytel.decode("utf-8")
print(bytel_2)