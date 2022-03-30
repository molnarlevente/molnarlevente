
print("8. Írj egy Python programot, amely bekér egy pozitív egész számot a felhasználótól és kiírja a képernyőre azokat "
      "a pozitív hárommal osztható számokat, amelyek kisebbek az adott számnál!")
print()

egy=int(input("Kérek egy pozitív egész számot: "))
while egy%3:
      print(f"igen")
      break
print(f"Következő")


# def osszeg_eddig (egy):
#     alap = 0
#     e = 1
#     while e <= egy:
#         alap = alap + e
#         e = e%3
#     return alap
# print(f"")


print("9. Írj egy Python programot, amely bekér két pozitív egész számot a felhasználótól és kiírja a képernyőre azokat "
      "a páros számokat, amelyek a két adott érték közötti zárt intervallumban találhatóak!")

print()

# elso=int(input("Kérek egy pozitív egész számot: "))
# masodik=int(input("Kérek még egy pozitív egész számot: "))
# lista1=int(0,1,2,3,4,5,6,7,8,9,10)
#
# while True:
#       if elso<lista1<masodik:
#             print(lista1)
#       else:
#             if elso > lista1 > masodik:
#                   print(lista1)


print("10. Írj egy Python programot, amely bekér egy 20-nál nem nagyobb pozitív egész számot a felhasználótól és kiírja "
      "a képernyőre a START szót úgy, hogy előtte annyi szóköz legyen amennyi a megadott szám értéke!")
print()
lista = int(input("Kérek egy 20-nál nem nagyobb pozitív egész számot: "))
a= len(lista)

# szamlalo=int(input("Kérek egy 20-nál nem nagyobb pozitív egész számot: "))
# def szamjegy_szam (n):
#       szamlalo = 0
#       while n != 0:
#             szamlalo = szamlalo
#           n = n


print("11. Írj egy Python programot, amely bekér egy pozitív egész számot a felhasználótól és kiírja a képernyőre azt a számot, "
      "amely az ennél a számnál nem nagyobb pozitív egész számok összege!")
# lista=[1,2,3,4,5,6,7,8,9,10]
# szam= int(input("Kérek egy pozitív egész számot 1 - 10 között: "))
# for i in szam:
#     if szam == lista:
#         print()


print("12. Írj egy Python programot, amely bekér egy szót (sztringet) a felhasználótól és kiírja a képernyőre "
      "a szó betűit, úgy, hogy minden betű egy új sorba kerüljön!")

valasz12=input("Kérek egy szót: ")
for i in valasz12:
      print(i)

print("Kész")

print("13. Írj egy Python programot, amely bekér egy pozitív egész számot a felhasználótól és kiírja a képernyőre "
      "felváltva a 0 és 1 számjegyeket úgy, hogy a számjegyek együttes darabszáma pontosan a megadott szám legyen!")
lista = [0,1]
valasz13=int(input("Kérek egy szót: "))



print("14. Írj egy Python programot, amely először bekér egy kisebb majd egy nagyobb pozitív valós számot a felhasználótól"
      " és kiírja a képernyőre azokat az egész számokat, amelyek a megadott értékek között helyezkednek el!")
a=int(input("Kérek egy számot: "))
b=int(input("Kérek egy nagyobb számot: "))
c= a + b

for i in lista:
      print(i, end=', ')


print("15. Írj egy Python eljárást, amely paraméterként kap 2 egész számot (N és M) és kiír a képernyőre a csillag (*) karaktereket"
      " M darab sorban és N darab oszlopban (tehát NxM darab karaktert egy téglalap alakú képernyőrészre)! A programodban hívd is meg ezt az alprogramot!")


