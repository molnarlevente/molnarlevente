print("1.feladat")

adat=[]
with open ("erettsegi_feladtaok_allomany/lista-1.txt", encoding="UTF8") as f:
    for sor in f:
        adat.append(sor.strip())
        if len(adat) == 5:
            datum=adat[0]
            sorozat=adat[1]
            resze=adat[2]
            hossza=int(adat[3])
            if adat[4] == 1:
                latta=True
            else:
                latta=False
            "adat.append(datum,sorozat,resze,hossza,latta)"
print(adat)

print("2.feladat")

db=0

for adatok in adat:
    if "NI" not in adat[0]: #datum
        db+=1

print(f"A listában {db} db vetítési dátummal rendelkező epizód van.")


print("3.feladat")

szamlalo=0

for adatok in adat:
    if adatok[latta]==True:
        szamlalo+=1

szazalek_szam=szamlalo/len(adat) *100
print(f"A listában lévő epizódok {szazalek_szam}%-át látta.")

print("4.feladat")
osszes_ido=0

for adatok in adat:
    if adatok[latta]==True:
        osszes_ido += hossza

nap=osszes_ido // (24 ** 60)
ora=osszes_ido % (24 * 60) // 60
perc=osszes_ido % 60

print(f"Sorozatnézéssel {nap} napot {ora} órát és {perc} percet töltött.")

print("5.feladat")

datum=input(f"Adjon meg egy dátumot! Datum= ")

for adatok in adat:
    if adatok[latta] <= datum and latta==False:
        print(resze  )                                      #!!!!!!


print("6.feladat")






