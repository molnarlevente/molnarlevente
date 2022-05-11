lista=[]
with open("TXT_allomanyok/autok.txt", encoding="UTF-8") as f:
    for adat in f:
        sor = adat.strip().split()

        nap = int(sor[0])
        ido = sor[1]
        rendszam = sor[2]
        azonosito = sor[3]
        km = sor[4]
        behajtas = sor[5]
        adatok = [nap, ido, rendszam, azonosito, km, behajtas]              # a sorrendeket is meg tudjuk változtatni, mi hat.meg a sorrendet
        lista.append(adatok)

print(lista)

# for elem in lista:                                  # kiiratjuk csak a rendszámokat, forciklussal !!!!!!!!!!!!
#     print(elem[2])
#



# hf int-be a számokat