# Lista létrehozása

szamok=[5,87,6,32,145,6]
szoveg=["alma","virág","kutya","ember"]
vegyes=[ 5, "barack", 3,["helo", 4]]
ures=[]
listaalistaban=[1,3,4,[szamok]]

# print(szamok,szoveg,vegyes,ures, listaalistaban)
#
# print(szamok[3])        # indexelés ezért az eredmény 32
# print(szamok[-1])       # utolsó kiiratása
#
# print(szamok[1-3])      # számolás is lehet benne
#
# #minden elem kiratáse
# #ciklussal:
#
for elemek in szamok:
    print(elemek)
#
# print(listaalistaban[4])        # a beslo lista a 4.index
#     # ROSSZ      print(listaalistaban[12321312]) # ez nem szeletelés, nem lehet kiiratni a nem létező indexet, a program hibára fut
# #lista hossza len-nel
#
# print(len(szamok))      # nem indexet kapok vissza, hanem db-számot
#
#
#
#
#keresés a listában
db = 0

print(32 in szamok)

if 32 in szamok:
    print(f"van találat")           # for-al    VIZSGÁLAT
    db+=1
else:
    print(f"nincs")

#
# #lista műveletek :
#
# osszeadas= szamok + szamok
# print(osszeadas)
# print(*osszeadas)
#
# # szorzás         *
# szorzas=szamok*2
# print(szorzas)
#
# # szeletelés  [ x : y ]
# print(szamok[1:4])
# print(szamok[:4])
# print(szamok[4:])
#
# # elemek módosítása
# print(*szoveg)
# szoveg[2]="egésznap"
# print(*szoveg)
#
# szoveg[1:1]="FaliÓra"
# print(szoveg)
#
# #elem törlése
# print(szamok)
# del szamok[2]
# print(szamok)
#
# #szövegben tólig kitörlés
#
# print(szoveg)
# del szoveg[1:8]
# print(szoveg)
#
# #hozzá fűz az utolsó lista elem után
# szoveg.append("valami")
# print(szoveg)

# objektumok és hivatkozások
    # sztring esetén: ugyan arra az objektumra mutat az alábbi módon bizonyítjuk
a = "valami"
b = "valami"

print(a == b)

print(a in b)
print(50*"!")
#viszont a lista esetében ugyan KÜLÖN objektumra mutat az alábbi módon bizonyítjuk
list1 = [1,2,3,4,]
list2 = [1,2,3,4,]

print(list1==list2)     #==> true

print(list1 in list2)   #==> false

                                                                        #tk 150.oldal (fedőnevek)

 # klónozás
a = ["egy","kettő"]
b = a[:]

print(*b)

a.append("három")

print(*a)
print(*b)


# lista és for-ciklus használata

#kész. egy listát majd az elemeket szorozzuk meg kettővel

szorzat= [1,2,3,4,5,6]

for i in szorzat:
    print(f"az eredeti szám {i} majd ezt megszorzom 2-vel és ezt fogom kapni {i*2}")

for (i, ertek) in enumerate(szorzat):                                                        # indexelve írjuk ki   enumerate !!!!!!!!!!!!!!!!!
    print(f"a sorozat indexe:{i}, az indexen a {ertek*2} szám *2 értéke szerepel ")

    #   sztringbe
    print("-"*50)
szoveg= ["alma", "virág", "eper","kutya","ember"]

for (i, ertek) in enumerate(szoveg):
    print(i, ertek)

    print("_" * 50)
                #       lista metódusok  (beép.függvények)

mlista = []
print(mlista)

mlista.append(85)
mlista.append(65)
mlista.append(4)
mlista.append(418)          # mindeig az utolsó poz.-ra
mlista.append(12)
print(mlista)

mlista.insert(2, 45)        # beszúrás az adott helyre de nem cseréli ki, erébb rólja, !!!!!!!pozicíóra!!!!!!!
print(mlista)

print(50*"-")
sorbaredezve= sorted(mlista)
print(sorbaredezve)         # növ.sorrend az eredeti lista nem módosul!!!!!!!!!!
print(mlista)
print(50*"-")

mlista.reverse()            # elemek megfordítás, de az eredeti lista módosul!!!!!!!!!!
print(mlista)

    #   rendezzükk a listát növekvő sorrendbe

mlista.sort()               # sorba rendez, de az eredeti lista módosul!!!!!!!!!!
print(mlista)

    #   csökk. sorrend, de az eredeti lista nem módosul!!!!!!!!!!
print(50*"-")
print(sorted(mlista, reverse=True))
print(50*"-")
