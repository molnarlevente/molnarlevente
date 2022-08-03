#
# print("8. Írj egy Python programot, amely bekér egy pozitív egész számot a felhasználótól és kiírja a képernyőre azokat "
#       "a pozitív hárommal osztható számokat, amelyek kisebbek az adott számnál!")
kerdes =int(input("Kérek egy pozitív egész számot : "))

for kerdes in range(1, kerdes):
      if kerdes % 3 == 0:
            print(kerdes, end=' ')
                                                #Kész
print()

# while egy > 100:
#       if egy % 3 ==0:
#             print(egy)
#       egy +=1



# print(egy<szam and egy%3)


print("9. Írj egy Python programot, amely bekér két pozitív egész számot a felhasználótól és kiírja a képernyőre azokat "
      "a páros számokat, amelyek a két adott érték közötti zárt intervallumban találhatóak!")

print()
# x=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
valasz1=int(input("Kérek egy pozitív egész számot: "))
valasz2=int(input("Kérek még egy pozitív egész számot: "))               #kész

for i in range(valasz1, valasz2):
      print(i, end=' ')





print("10. Írj egy Python programot, amely bekér egy 20-nál nem nagyobb pozitív egész számot a felhasználótól és kiírja "
      "a képernyőre a START szót úgy, hogy előtte annyi szóköz legyen amennyi a megadott szám értéke!")

valasz3 = int(input("Kérek egy 20-nál nem nagyobb pozitív egész számot: "))
kerek = valasz3 * " "                                                       #KÉSZ
print(f"{kerek} START")



#print("11. Írj egy Python programot, amely bekér egy pozitív egész számot a felhasználótól és kiírja a képernyőre azt a számot, "
     # "amely az ennél a számnál nem nagyobb pozitív egész számok összege!")

# lista11=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

valasz11=int(input("Kérek egy pozitív egész számot: "))
for i in range(0, valasz11):                          #kész
      print(i, end=' ')

print()




print("12. Írj egy Python programot, amely bekér egy szót (sztringet) a felhasználótól és kiírja a képernyőre "
      "a szó betűit, úgy, hogy minden betű egy új sorba kerüljön!")

valasz12=input("Kérek egy szót: ")
for i in valasz12:
      print(i)                                        #kész

print("Kész")

print("13. Írj egy Python programot, amely bekér egy pozitív egész számot a felhasználótól és kiírja a képernyőre "
      "felváltva a 0 és 1 számjegyeket úgy, hogy a számjegyek együttes darabszáma pontosan a megadott szám legyen!")

valasz13=int(input("Kérek egy számot: "))
kerek13= valasz13 * (1,2)                                   # kész
print(kerek13)

# print("14. Írj egy Python programot, amely először bekér egy kisebb majd egy nagyobb pozitív valós számot a felhasználótól")
#       # " és kiírja a képernyőre azokat az egész számokat, amelyek a megadott értékek között helyezkednek el!")
# valasz14a=int(input("Kérek egy kisebb számot: "))
# valasz14b=int(input("Kérek egy nagyobb számot: "))
#
# for i in range(valasz14a, valasz14b):
#       print(i, end=' ')
#                                           #kész
# print()
#
#

  #print("15. Írj egy Python eljárást, amely paraméterként kap 2 egész számot (N és M) és kiír a képernyőre a csillag (*) karaktereket"
      #" M darab sorban és N darab oszlopban (tehát NxM darab karaktert egy téglalap alakú képernyőrészre)! A programodban hívd is meg ezt az alprogramot!")

#egybeágyazott for ciklus

n=int(input("Kérlek írj be egy egész számot: "))
m=int(input("Kérlek írj be még egy egész számot: "))

# for i in n*"*":
#       print(i)
#       for f in m*"\n":
#             print (f and i)

# for i in n*"*" and m*"\n":
#       print(i)


# for sor in n*"*":
#       for oszlop in m*"\n":
#             print(sor, oszlop)

# for sor in n*"*":
#       print(sor, end=' ')
#       for oszlop in m*"\n":
#             print(oszlop)

for i in range(m):
      print("*")                                   #kész
      for sor in n * "*":
            print(sor, end=" ")


print()
# gyakorlás az összes eddigiből:
# tk 2.14
print(1)
a="Lustaság"
b="fél"
c="egészség."
print(a+b+c)

print()

print(2)
print(6*(1-2))

print()

print(7)
#Jelenleg pontosan 14 óra van. Beállítunk egy ébreszt˝oórát úgy, hogy 51 órával kés˝obb csörögjön. Hány órakor fog az ébreszt˝oóra megszólalni?
jelenleg=14
kesobb=51
print((jelenleg+kesobb)%24)
print()

print(8)
# Írj egy Python programot az előző feladat általános megoldására. Kérd be a felhasználótól az aktuális id˝ot (csak
# az órákat) és azt, hogy hány órával kés˝obb szólaljon meg az ébreszt˝oóra, majd jelenítsd meg a képerny˝on, hogy
# hány órakor fog megszólalni az ébreszt˝oóra.

ido=int(input("Kérlek írd be az időt: "))
ebreszto=int(input("Hány óra múlva szeretnéd, hogy szóljon az éresztő órád: "))
if ido + ebreszto > 24:
    print(f" Az ébresztő órád {(ido + ebreszto)%24}-kor for szólni")
else:
    print(f" Az ébresztő órád {ido + ebreszto}-kor for szólni")
print()

print("     Sztringek")
print("3.feladat")
# A függvény adja vissza a karakter sztringbeli el˝ofordulásainak számát és betünként írja ki

gyumolcs=input("Kérelek írd be a kedvenc gyümölcsödet: ")

for betu in gyumolcs:
    print(betu, end= " - ")
print("\n", len(gyumolcs))


print()
print("5.feladat")

szoveg="A korban még igásállatok vontatják a hajókat a Dunán felfelé. Így halad előre a Szent Borbála is, dacolva a sötétséggel és a rettenetes viharral. A hajó személyzetét a kormányos, Fabula János; a hajóbiztos, Timár Mihály; a tisztító; a hajóteher (tízezer mérő búza) tulajdonosa, Trikalisz Euthym; valamint lánya, Timéa alkotja a legénységen kívül. Hirtelen szörnyű veszélybe kerülnek: a víz egy elszabadult malmot sodor feléjük..."

print(f"A szövegben {len(szoveg.replace(' ' , ''))} szó szerepel, amelyből {szoveg.lower().count('e')} tartalmaz e-betűt.")

print()
print(7)

elotag = "Törp"
utotagok_listaja = ["erős", "költő", "morgó", "öltő", "papa", "picur","szakáll"]

for utotag in utotagok_listaja:
    print(elotag+utotag.replace('Törppapa', 'Törpapa'))

sztring= "Megszencségteleníthetetlenkedéseitekért"

print(sztring[1])                     # elem kiiratása ===> 0-tól kell nézni az indexeket
print(sztring[-1])                    # az utlsó kiiratása, visszafelé számol
print(len(sztring))                   # a sztring száma ami 1-től számol minden karaktert ami ""-n belül van
print(sztring.lower())                # csak nagy betű
print(sztring.upper())                # csak kis betű
print(sztring.swapcase())             # ellentétes


print(list(enumerate(sztring)))             # kiiratni az indexeket str-ből int-be tehát az indexek mellé írja a megfelelő betűt is
print(len(szoveg.replace(' ' , '')))        # számlálás spacek nélkül
print(sztring.count("s"))                   # "E" betűk keresése

# Értékek és típusok  --->  str, int, float
# Változók  --->   változó lényegében egy név, amely egy értékre utal.
# utasítások  --->   while for if
# for  --->   ismétlés automatikusan végig megy      ---->       BEJÁRÁS
# while  --->   ha nem tudjuk a pontos értéket akkor ezt kell használni nem a for-t,
#            PL: egy alap értékhez adjuk hozzá mindig ameddig nem éri el a beírt összeget
# if  --->  láncolt, ha fügvény, else ág

