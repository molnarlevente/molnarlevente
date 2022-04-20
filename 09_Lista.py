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
# for elemek in szamok:
#     print(elemek)
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
# #keresés a listában
# db = 0
#
# print(32 in szamok)
#
# if 32 in szamok:
#     print(f"van találat")           # for-al    VIZSGÁLAT
#     db+=1
# else:
#     print(f"nincs")
#

# lista műveletek :

osszeadas= szamok + szoveg
print(osszeadas)
print(*osszeadas)

# szorzás         *
szorzas=szamok*2
print(szorzas)

# szeletelés  [ x : y ]
print(szamok[1:4])
print(szamok[:4])
print(szamok[4:])

# elemek módosítása
print(*szoveg)
szoveg[2]="egésznap"
print(*szoveg)

szoveg[1:1]="FaliÓra"
print(szoveg)

#elem törlése
print(szamok)
del szamok[2]
print(szamok)

#szövegben tólig kitörlés

print(szoveg)
del szoveg[1:8]
print(szoveg)


