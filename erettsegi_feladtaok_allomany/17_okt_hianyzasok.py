hianyzasoklista=[]

with open ("info_feladat/2017_okt/naplo-2.txt", encoding="UTF-8") as f:
    for adat in f:
        sor = adat.strip().split(" ")
        if sor[0]=="#":
            honap = int(sor[1])
            nap = int(sor[2])
            #hianyzasoklista.append([honap, nap])
        else:
            nev = sor[0] + " " + sor[1]
            #knev = sor[1]
            hianyzas = sor[2]
            hianyzasoklista.append([honap, nap, nev, hianyzas])

print(f"2.feladat\nA naplóban {len(hianyzas)} bejegyzés van")

print(f"3.fealdat")

igazolatlan = 0
igazolt = 0

for honap, nap, nev, hianyzas in hianyzasoklista:
    for elem in hianyzas:
        if elem == "X":
            igazolt += 1

        if elem == "I":
            igazolatlan += 1

print(igazolt, igazolatlan)
