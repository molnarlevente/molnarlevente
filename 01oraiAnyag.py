# kiiratás:
print("Ez az első programom")       # vagyv
print()
print('Ez is szöveg')

# több soros megjelenítés

print("""ez a szöveg
több sorban
jelenik meg""")
#\n


# értéktípusok:
15          #int
"szöveg"    #str (string)
3.5         #float  (lebegő pontos)
3,5         #értékpár


# változók létrehozása és értékadás
print()
a = 'válozóba tárolt string'
print(a)

x = 15
y = 3.5
z = 'szöveg'

print(a,x,y,z)


# változó értékének a növelése
b = 1
print(b)
b = b + 1 # a b változóban tárolz adat értékének növelése eggyel
print(b)
b += 1 # a b változóban tárolt adar értékének növelése eggyel
print(b)
# b=+1 #ha ezt így írod akkor olyan mintha beállítanád neki a b = 1 azaz b értéke egy lesz

#változó tíusának a megváltoztatása
print()       #sortörés
ido = ' süt a nap' #str
print(ido)
ido= 'felhős'  #érték megváltoztatása
print(ido)
ido = 1990     # típus változtatása
print(ido)

#kiértékelés len beépített függvény használat
sajatnevem = 'Molnár Levente'
print(len(sajatnevem))

#összeadás
print()
d=10
c=5
e=c+d
print(e)                                   #változóba eltárolva
print(c+d)                                 #kiiratás közben

#szöveg hozzáadása a kiíratáshoz
print('\nA két szám összege: '+str(e))     #típuskonverzió str(e) (kasztolás)
#vagy
print('\nA két szám összege: ',e)          #int típusként való kiíratás

print(f'\nA két szám összege: {e}')         #sztring interpoláció (a szövegbe bele tudom illeszteni  aváltozómat akár
                                              # többet is!)

#típukonverziós függvény ami nem egyenlő a változó típusával!!!
#ezt a terminál ablakban futatom!!!
int(25)
25
float(25)
25.0
str(25)
'25'

o=c/3                   #maradékos osztás

print(o)
o=c//3

h=c**2                  #hatványozás
print(o)

o=c%d
print(o)                #osztás maradéka

# a zárójelekkel módosítható ez eredmény kiértékelése!!!!
# n=5
# n= 3*n+1 eredmény 16
# de ha zárójelezek:
# n=5
# n= 3*(n+1) eredmény 18

#szövegösszefűzés:
vnev = 'Molnár'
knev = 'Levi'
print(vnev + ' ' + knev)

#adat bekérés a felhasználótól
input('Kérek egy adatot: ')

#adat bekérés a felhasználótól és változóba tárolása
valasz=input('Kérek egy adatot: ')
print(f'A megoldot adat: {valasz}')

