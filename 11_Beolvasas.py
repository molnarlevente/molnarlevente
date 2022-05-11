# Beolvasás:

# alapok!!!!!!!                     with open("fáj neve", encoding="utf8") as f:
#read ==> kiiratás
with open("nevek_sima.txt", encoding="utf8") as fajl:       # kiiratás (encoding="utf8" ==> ékezeteseket is kitudja írni) !!!!!!!
    sor = fajl.read()                                       # ez a "fajl" változó bármi lehet, álltalában f"f"-nek használják !!
print(sor)
print(type(sor))

print("_"*100)


with open("nevek_sima.txt", encoding="utf8") as f:          # beolvasás
    sorok = f.read()
    listaa = sorok.split()                                  # listát hoz lérte és (split) fel darabolja a szöveget az enterek mentén vagy a szoközök mentén
                                                            # ÉS EGY LISTÁBA HELYEZI EL!
print(listaa)
print(type(listaa))

print("_"*100)

for elem in enumerate(listaa):                              # indexele külön sorokba írja ki
    print(elem)

print("_"*100)
# soronkénti beolvasás azaz csak bizonyos sorok beolvasása

with open("nevek_sima.txt", encoding="utf8") as f:
    sor1 = f.readline().strip().split()
    sor2 = f.readline().strip().split()
    sor3 = f.readline().strip().split()
print(sor1)
print(sor3)

print("_"*100)
lista2 = []                                             # üres lista készítése
with open("nevek_sima.txt", encoding="UTF-8") as f:     # fájl meg nyitása
    elso_sor = f.readline()                             # elsősor kiszedése
    for elem in f:                                      # fájl bejárása
        sor = elem.split()                              # sor változóba darabol
        lista2.append(sor)                              # hozzáadás a listához

print(elso_sor)
print(lista2)

print("_"*100)

for nev in lista2:
    print(nev)

print("_"*100)

# csak a vezeték nevek kiiratása!!!!!!!!!!!!!!!!!!!!!!!!!444

for nev in lista2:                      # vezetéknevek kiiratása    0. indexen lévőt
    vnev = nev[0]
    print(vnev)

print("_"*100)

for nev in lista2:                      # keresztnevek kiiratása    1. indexen lévőt
    knev = nev[1]
    print(knev)

print("_"*100)
print("_"*100)









