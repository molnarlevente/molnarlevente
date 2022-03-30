list = [5, 47, 8, 54, 6, 2, 15, 4, 1, 25, 10, 65, 17, 321]

# irassuk ki a 20-nál kisebbeket:
# for listaelem in list:
#     if listaelem <= 20:
#         print(listaelem, end=' ,')
# print()
#
# # irjuk ki a 20 és a 10 közötti számot
for i in list:
    if i >10 and i <20:
        print(i, end=',')
#
# # irjuk ki a 10-nél kissebb és a 20-nál nagyobb számokat
# print()
#
# for f in list:
#     if f < 10 or f > 20:
#         print(f, end="," )
#
#irjuk ki a lista elemeit ameddig nem találok 10-et
# print()
#
# for g in list:
#     print(g, end=',')u
#     if g == 10:
#         break

#                                   HÁZI FELADAT:

    #       1
print()

n=int(input("1.feladat: Kérek egy számot: "))
m=int(input("           Kérek még egy számot: "))
v=int(input("           Kérek és még egy számot: "))

if n < m and n < v:
    print(f"a/az {n} a legkisebb!")
else:
    if m < n and m < v:
        print(f" a/az {m} a legkisebb!")
    else:
        print(f" a/az {v} a legkisebb!")

print("vagy így is meg lehet oldani, de nem elegáns")

        #vagy így
import sys
                        # vagy (szam = 9999999999999999999999999)
szam = sys.maxsize

for i in range(3):
    valasz = int(input("Kérek egy számot: "))
    if valasz < szam:
        szam = valasz
else:
    print(szam)


    #       2
print()

a= int(input("2.feldat: adj meg egy számot:"))
b= int(input("          adj meg még egy számot:"))
c= int(input("          adj meg még egy számot:"))

if a > b and a > c:
    print(f"a/az {a} a legnagyobb")
else:
    if b > c and b > a:
        print(f"a/az {b} a legnagyobb")
    else:
        print(f"a/az {c} a legnagyobb")

        #       3
print()

jegy= float(input("3.feladat: Kérem írd be a dolgozat pontszámát, a fél pontot is oda írhatod!: "))

if jegy < 50.0:
    print(f"a dolgozatod 1-es lett!")
else:
    if 50.0 <= jegy < 60.0:
        print(f"a dolgozatod 2-es lett!")
    else:
        if 60.0 <= jegy < 70.0:
            print(f"a dolgozatod 3-as lett!")
        else:
            if 70.0 <= jegy < 85.0:
                print(f"a dolgozatod 4-es lett!")
            else:
                print(f"Gratulálok, a dolgozatod 5-ös lett!")

     #        4
print()

negyes= int(input("4.feladat: Kérlek írj be egy egész számot: "))

if negyes %3==0 or negyes %5==0:
    print(f"igen, a/az {negyes} szám osztható 3 vagy 5-el!")
else:
    print(f"nem, a/az {negyes} szám nem osztható 3 vagy 5-el!")

    #       5
print()

x = int(input("5.feladat: Kérek egy számot"))
y = int(input("           Kérek még egy számot"))
z = int(input("           És kérek még egy számot"))

if x + y == z:
    print(f"Ha össze adjuk a/az {x} és {y} számot, {z}-t kapunk!")
else:
    if x + z == y:
        print(f"Ha össze adjuk a/az {x} és {z} számot, {y}-t kapunk!")
    else:
        if y + z ==x:
            print(f"Ha össze adjuk a/az {y} és {z} számot, {x}-t kapunk!")
        else:
            print(f"Nem egyenlő két szám összege a harmadikkal!")

    #      6
print()

a= int(input("6. feladat: Kérek egy számot: "))
b= int(input("            Kérek még egy számot: "))
c= int(input("            És kérek még egy számot: "))

if a%2==0 and b%2==0 and c%2==0:
    print(f"Mind a három szám, {a}, {b}, {c} páros!")
else:
    if a%2==0 and b%2==0:
        print(f"Kettő szám, {a}, {b} páros!")
    else:
        if a%2==0 and c%2==0:
            print(f"Kettő szám, {a}, {c} páros")
        else:
            if b%2==0 and c%2==0:
                print(f"Kettő szám, {b}, {c} páros")
            else:
                print(f"Nincs kettő páros szám!")


      #                          #     GYAKORLÁS
print()
print("GYAKORLÁS")
print("     1.")
print()


t= float(input("Kéredés:    Hány foktól fagy a víz?: "))

if t == 0:
    print(f"Helyes válasz!")
else:
    if t < 0:
        print(f"{t}-nál/nél nagyobb hőmérsékleten már megfagy!")
    else:
        if t > 0:
            print(f"{t}-nál/nél kisebb mőmérsékleten fagy meg!")
        else:
            print()



print()
print("ételek")
print("     2.")
print()

for i in ["spagetti, gyümölcstorta, hatlapos"]:
    print(i, end=" ,")
print()
v= str(input("  Kérlek válaszd ki az egyik ételt és írd be ide, hogy megtudd milyen alapanyagra lesz szükséged: "))

if v == "spagetti":
    print(f"Vegyél tésztát, húst, szószt!")
else:
    if v == "gyümölcstorta":
        print(f"Vegyél banánt, barackot, epret, pudingot és tésztát!")
    else:
        if v== "hatlapos":
            print(f"Vegyél csoki pudingot, tésztát és cukrot!")
        else:
            print(f"Biztos jól írtad be?")

print()
k=str(input("Mennyibe fog kerülni az adott alapanyag: "))

if k == "tészta":
    print(f"400 Ft")
else:
    if k=="hús":
        print(f"1000 Ft")
    else:
        if k=="szósz":
            print(f"750 Ft")
        else:
            if k=="banán":
                print(f"350 Ft")
            else:
                if k=="barack":
                    print(f"200 Ft")
                else:
                    if k=="eper":
                        print(f"350 Ft")
                    else:
                        if k=="puding":
                            print(f"270 Ft")
                        else:
                            if k=="cukor":
                                print(f"120 Ft")
                            else:
                                print(f"Volt {k} a listán? Én nem emléksem! Nézd meg újra :)")


print()
print("gyakorlás       utazás")
print("     3.")
print()

# legyenek utazási lehetőségek, legyen mivel utazni, legyenek időpontok és legyen ajánlás ha valamivel nem tud utazni

print("Szia! Ez egy utazási lehetőségeknek a hírdetése. Megnézheted hova, mikor, mivel tudsz eljutni és ez mennyibe kerül.")
print(" Lehetőséged van Debrecenbe, Budapestre, Pécsre menni.")
a=str(input("     Kérlek írd be a választott várost: "))

print(" Busszal vagy vonattal szeretnél menni?")
b=str(input("     Kérlek írd be a választott utazási eszközt: "))

print( "  Mikor szeretne utazni?"
       "  13.15 vagy 15.15- kor?")
k=float(input("     Kérlek írd be ide az időpontot amikor szeretnél idnulni: "))

if a== "Debrecen" and b=="vonat" and k==13.15:
    print(f"Debrecenbe vonattal az út 2500 Ft")
else:
    if a== "Debrecen" and b=="busz" and k==13.15:
        print(f"Debrecenbe busszal az út 5000 Ft")
    else:
        if a == "Debrecen" and b == "vonat" and k == 15.15:
            print(f"Debrecenbe vonattal az út 2500 Ft")
        else:
            if a == "Debrecen" and b == "busz" and k == 15.15:
                print(f"Debrecenbe busszal az út 5000 Ft")
            else:
                if a == "Budapest" and b == "vonat" and k==13.15:
                    print(f"Budapestre vonattal az út 2300 Ft")
                else:
                    if a == "Budapest" and b == "busz" and k==13.15:
                        print(f"Budapestre busszal az út 4000 Ft")
                    else:
                        if a == "Budapest" and b == "vonat" and k == 15.15:
                            print(f"Budapestre vonattal az út 2300 Ft")
                        else:
                            if a == "Budapest" and b == "busz" and k == 13.15:
                                print(f"Budapestre busszal az út 4000 Ft")
                            else:
                                if a == "Pécs" and b == "vonat" and k == 13.15:
                                    print(f"Pécsre vonattal az út 2300 Ft")
                                else:
                                    if a == "Pécs" and b == "busz" and k == 13.15:
                                        print(f"Pécsre busszal az út 2500 Ft")
                                    else:
                                        if a == "Pécs" and b == "vonat" and k == 15.15:
                                            print(f"Pécsre vonattal az út 2300 Ft")
                                        else:
                                            if a == "Pécs" and b == "busz" and k == 15.15:
                                                print(f"Pécsre busszal az út 2500 Ft")


print()
print("Vásárlás")
print("     4.")
print()

# ha vegetáriánus vagy, vagy szóját eszel vagy halat, nem húst.
# bekérni, mit eszel, ha vegetáriánus vagy akkor szóját vayg halat, nem húst

print()
print("         következő")
print()

print("Szia, hivatalos vagy egy bálra, ahova most ki kell választanod mibe fogsz menni"
      "   hawaii ing, farmer sort, kisestéi, melegítő vagy elegáns kosztüm ")

a=str(input("   Kérem írd be melyik ruhádban szeretnél menni: "))

print("Melyik cipődet választod a ruhádhoz? Balerina cipő, fehér sport cipő, fehér szandál vagy egy elegáns ruha cipő?")

b=str(input("   Nos, melyik cipődet választod? Írd ide: "))

print("Melyik órát veszed fel hozzá? Wellington, Gucci vagy Apple Watch?")

c=str(input("   Milyen órára gondoltál?"))

l=print("Egyébként el szeretnél menni, vagy szeretnél inkább egy kifogást keresni?")

d=str(input("   keressünk vagy nem kell?"))

if a == "hawaii ing" or "farmer sort" or "melegítő" or b == "Balerina cipő" or "fehér szandál":
    print(f"Bocsi de ilyen ruhába nem nagyon kéne megjelenni")
    print(l ,"\n", d)
    if d== "keressünk":
        print(f"   Mond, hogy megy a hasad :(")
    else:
        if d == "nem kell":
            print(f"  Akkor öltözz :D")
else:
    if a== "kisestéi" and b == "elegáns ruha cipő" and c == "Wellington" or "Gucci" or "Apple Watch":
        print(f"  Ez egy jó döntés!")
    else:
        if a== "elegáns kosztüm" and b == "elegáns ruha cipő" and c == "Wellington" or "Gucci" or "Apple Watch":
            print(f"  Ez jól fog kinézni!")
        else:
            if a== "melegítő" and b == "fehér sport cipő" and c == "Wellington" or "Gucci" or "Apple Watch":
                print(f"  Ez jó szett de nem ide illik")
            else:
                if a=="hawaii ing" and "fehér sport cipő" or "fehér szandál":
                    print(f"  Hát ez egy jó kis NYÁRI szett!")
                else:
                    print()

print()



