#ird ki  a számokat 1-10-ig
print(1,2,3,4,5,6,7,8,9,10)
#vagy
print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)
print(8)
print(9)
print(10)

#for ciklus segítségével:
for i in [1,2,3,4,5,6,7,8,9,10]:                    #lista létrehozása      #pass -> ne fusson hibára
    print(i)                                        #lokális változó csak itt találom meg


#irjuk ki hogy Szeretek programozni
print()
for i in [1,2,3,4]:
    print("szeretek programozni")

#lista kiszervezése változóba:
print()
lista = [1,2,3,4,5,6,7,8,9,10]
for i in lista:
    print(i, end=', ')                              #egy soros kiiratás

# a range használata
#ird ki  a számokat 1-10-ig
print()
for i in range(10):                                 #range (10) => 1-9-ig irja ki számokat (indexelés= 0-tól indul)
    print(i, end=', ')

#ird ki  a számokat 1-10-ig
print()
for i in range(1,11):
    print(i, end=', ')

#ird ki a számokat 5-10-ig
print()
for i in range(5, 11):
    print(i, end=', ')

#irassuk ki csak a páros számokat 1-10-ig
print()
for i in range(2,11,2):
    print(i, end=', ')

#irassuk ki csak a páratlan számokat 1-10-ig
print()
for i in range(1,11,2):
    print(i, end=', ')

print()
print(*range(1,11))     #egy sorban van a számok kiiratása

#írjuk ki a számokat
print()
for i in range(1,11):
    print(i, end=', ')
else:                                   #utánna kiirja egyszer
    print("Vége a ciklusnak")

#szövegkezelés forciklussal
print()
for i in "szöveg":
    print(i)
gyumolcsok = ["alma", "körte", "banán", "szilva", "narancs", "kivi"]
for i in gyumolcsok:
    print(i, end=', ')

#irassuk ki a lsita hosszát, hány elem van a listában!
print()
print(f'A listában szereplő elemek száma: {len(gyumolcsok)} db')

#2 db  lista: tulajdonságok és gyümölcsök:
#írjuk ki az egyes tulajdonsághoz és gyümölcsök2-t

tulajdonsag= ["érett", "nagy", "édes"]
gyumolcsok2= ["alma", "körte", "banán", "szilva", "narancs", "kivi"]

for i in gyumolcsok2:
    for j in tulajdonsag:
        print(i, j)

print()                     # megfordítjuk

for i in tulajdonsag:
    for j in gyumolcsok2:
        print(i, j)











