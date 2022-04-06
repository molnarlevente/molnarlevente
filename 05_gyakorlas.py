
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


# osszeg9 = 0
# for i in x:
#     osszeg9=valasz1<x>valasz2
# print(f"2.: {osszeg9}" )

# if valasz1 < valasz2 and valasz1 < valasz2:
#     print(f"a/az {n} a legkisebb!")
# else:
#     if valasz2 < valasz1 and valasz2 < valasz1:
#         print(f" a/az {m} a legkisebb!")
#     else:
#         print(f" a/az {v} a legkisebb!")
# if valasz1<x and valasz2<x:                                           #Félig kész
# print(f"Az adott szémok, amelyek a/az {valasz1} és a/az {valasz2} nem más mint a  ")


print("10. Írj egy Python programot, amely bekér egy 20-nál nem nagyobb pozitív egész számot a felhasználótól és kiírja "
      "a képernyőre a START szót úgy, hogy előtte annyi szóköz legyen amennyi a megadott szám értéke!")

valasz3 = int(input("Kérek egy 20-nál nem nagyobb pozitív egész számot: "))
kerek = valasz3 * " "                                                       #KÉSZ
print(f"{kerek} START")



#print("11. Írj egy Python programot, amely bekér egy pozitív egész számot a felhasználótól és kiírja a képernyőre azt a számot, "
     # "amely az ennél a számnál nem nagyobb pozitív egész számok összege!")

# lista11=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

valasz11=int(input("Kérek egy pozitív egész számot: "))
for i in range(0, valasz11):                          #
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

print("14. Írj egy Python programot, amely először bekér egy kisebb majd egy nagyobb pozitív valós számot a felhasználótól")
      # " és kiírja a képernyőre azokat az egész számokat, amelyek a megadott értékek között helyezkednek el!")
valasz14a=int(input("Kérek egy kisebb számot: "))
valasz14b=int(input("Kérek egy nagyobb számot: "))

for i in range(valasz14a, valasz14b):
      print(i, end=' ')
                                          #kész
print()



  #print("15. Írj egy Python eljárást, amely paraméterként kap 2 egész számot (N és M) és kiír a képernyőre a csillag (*) karaktereket"
      #" M darab sorban és N darab oszlopban (tehát NxM darab karaktert egy téglalap alakú képernyőrészre)! A programodban hívd is meg ezt az alprogramot!")

#egybeágyazott for ciklus
