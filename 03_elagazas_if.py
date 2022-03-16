# booleam típusok
#>>> type(True)                      <class 'bool'>
#>>> type(False)                     #<class 'bool'>

# összehasonlító operátorok:
    # gyenlő                 a == b
    # Nem egyenlő            a != b (!!negátolás!! = tagadod)
    # kisebb mint:           a < b
    # nagyobb mint:          a > b
    # kisebb vagy egyenlő:   a <= b
    # nagyobb vagy egyenlő:  b >= b

# logikai operátorok:
    # És =>       and
    # vagy =>     or
    # tagadás =>  not

#>>> n = 9
#>>> n%2==0 or n%3==0
#True
#>>> n = 9
#xx>>> n%2==0 and n%3==0
#False
#>>> not(x<n)
#False

# feltételes végrehajtás (if használatával)
a=25
b=33
if a<b:
    print(f'a/az {a} kisebb mint a/az {b} ')

# kérek egy számot a felhasználótol és döntsük el róla hogy páros vagy páratlan
    # csak a páros
valasz = int(input("Kérek egy számot:"))
if valasz%2==0:
    print(f'a/z {valasz} páros')

# most javitjuk a programunkat és megnézzük mnd a kettő ágat
    # igaz vagy hamis

valasz2 = int(input("Kérek egy számot:"))
if valasz2%2==0:
    print(f'a megadott szám {valasz2} páros')        # igaz/True ág (vagy ez fut le)
else:
    print(f'a megadott szám {valasz2} páratlan')     # hamis/False ág (vagy ez fut le)

# kérjünk be

pozitiv = int(input("kérek egy számot (lehet ez negatív és pozitív is):"))
if pozitiv > 0:
    print(f'a megadott szám {pozitiv} pozitív')
else:
    print(f'a megadott szám {pozitiv} negatív')

# LÁNCOLT feltételes utasítás:
    #szerinted melyik a helyes válasz?      pl: a vagy b vagy c

valasztasok = input('Szerinted melyik a helyes válasz? "a" vagy "b" vagy "c": ')

if valasztasok == 'a':
    print('az "a" választ írtad be')
elif valasztasok == 'b':
    print('az "b" választ írtad be')
elif valasztasok == 'c':
    print('az "c" választ írtad be')
else:
    print('rossz választ adtál meg')

# BEÁGYAZOTT feltételes utasítás:
    #vizsgáljuk a + vagy - vagy 0!!!

valasz3 = int(input('Kérek egy számot:'))
if valasz3 > 0:
    print(f'a megadott szám {valasz3} ami pozitív')
else:
    if valasz3 < 0:
        print(f'a megadott szám {valasz3} ami negatív')
    else:
        print(f'a megadott szám {valasz3}, se nem pozitív se nem negatív')

## hf

print("Házi")
 # kérjünk be egy számot, 0-10 közé vagy annál nagyobb két féle képpen!!!

# BEÁGYAZOTT feltételes utasítás:
hazi = int(input("Kérek egy számot:"))
if hazi >=0 and hazi < 10:
    print(f"Azt adott {hazi} 0 és 10 közé esik")
else:
    if hazi <0:
        print(f"Azt adott {hazi} kisebb mint 0")
    else:
        print(f"Azt adott {hazi} nagyobb mint 9 ")

# LÁNCOLT feltételes utasítás:
print("Házi2")


hazi2= int(input("Kérek egy számot:"))
if hazi2 >=0 and hazi < 10:
    print(f"Azt adott {hazi} 0 és 10 közé esik")
elif hazi >0:
    print(f"Azt adott {hazi} > 0 ")
else :
    print(f"nem tartozik a {hazi} szám nagyobb mint 9")



hazi = int(input("Kérek egy számot:"))
if hazi >=0 and hazi < 10:
    print(f"Azt adott {hazi} 0 és 10 közé esik")
else:
    if hazi <0:
        print(f"Azt adott {hazi} kisebb mint 0")
    else:
        print(f"Azt adott {hazi} nagyobb mint 9 ")

# feladat
a= int(input("adj meg egy számot:"))
b= int(input("adj meg még egy számot:"))
c= int(input("adj meg még egy számot:"))

for i in [a, b, c]:
    if a > b and c:
        print(f"a/az {a} a legnagyobb")
        if b > a and b:
            print(f"a/az {b} a legnagyobb")
        else:
            print(f"a/az {c} a legnagyobb")

if a > b and a > c:
    print(f"a/az {a} a legnagyobb")
else:
    if b > c and b > a:
        print(f"a/az {b} a legnagyobb")
    else:
        print(f"a/az {c} a legnagyobb")







# if bekeres1 > bekeres2 and bekeres3:
#     print(f"a/az {bekeres1}  a legnagyobb")
# else:
#     if bekeres2 > bekeres1 and bekeres3:
#         print(f"a/az {bekeres2}  a legnagyobb")
#         if bekeres3 > bekeres1 and bekeres2:
#             print(f"a/az {bekeres3}  a legnagyobb")
#     else:
#         print()























