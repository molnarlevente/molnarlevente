
lista=[]
with open("TXT_allomanyok/negyedevesberek.txt", encoding="UTF-8") as f:
    while True:
        megye = f.readline().strip()
        if not megye:            # elágazás
            break
        elso_n = int(f.readline().strip().replace(" ",""))
        masodik_n = int(f.readline().strip().replace(" ",""))
        harmadik_n = int(f.readline().strip().replace(" ",""))
        negyedik_n = int(f.readline().strip().replace(" ",""))

        adatok= [megye,elso_n,masodik_n,harmadik_n,negyedik_n]
        lista.append(adatok)

for elem in lista:
    print(elem)


#hány elemet tartalmaz a fájlunk?:
print(50*"_")
print(len(lista))

db = 0
for elem in lista:
    if elem[0]:
        db += 1

print(db)

#írjuk ki megyénként az első negyedéves átlagot, egymás alá kerüljenek a karakterek:
print(50*"_")
for elem in lista:
    print(f"{elem[0]:25} {elem[1]} Ft")

#melyik megyében a legnagyob az átlegkereset az elsőnegyedévben és mennyi az:
print(50*"_")
                                                ###### replace()!!!!!!!!!!!!!!!!!!!!!!!
max1 = 0
max2 = 0
max3 = 0
for elem in lista:
    if elem[1] > max1:
        max1=elem[1]
for elem in lista:
    if max1 == elem[1]:
        print(f"{elem[0]} {max1:,}")


        # for elem in lista:
        #     if (elem[1] > max1) > (elem[2] > max2) > (elem[3] > max3) :
        #         max2 = elem[2]
        #         max3 = elem[3]
        # for elem in lista:
        #     if max2 == elem[2] and max3 == elem[3]:
        #         print(f"{elem[0]} {max2:,}")
        #         print(f"{elem[0]} {max3:,}")



#max2 max3 max4   HHHÁÁÁÁZIIIIIIIII!!!!!!!!!!!!!!!!!!!!!!!


# mennyi volt az országban az első negyedéves átlagbér? Az eredményt két tuizedes pontossággal irasd ki!

print("_"*50)

alap=0
for i in adatok[1]:                                             ######## befejezniiiii
    if i > 0:
        alap += i
    print(alap)


print("_"*50)
