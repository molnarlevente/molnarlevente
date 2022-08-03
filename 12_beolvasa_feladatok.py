# lista=[]
# with open("TXT_allomanyok/autok.txt", encoding="UTF-8") as f:
#     for adat in f:
#         sor = adat.strip().split()
#
#         nap = int(sor[0])
#         ido = sor[1]
#         rendszam = sor[2]
#         azonosito = sor[3]
#         km = sor[4]
#         behajtas = sor[5]
#         adatok = [nap, ido, rendszam, azonosito, km, behajtas]              # a sorrendeket is meg tudjuk változtatni, mi hat.meg a sorrendet
#         lista.append(adatok)
# #
# print(lista)
#
# for elem in lista:                                  # kiiratjuk csak a rendszámokat, forciklussal !!!!!!!!!!!!
#     print(elem[2])
#
#
# print()
# print("-"*50)
# print()
#
#
# # hf int-be a számokat
# for elem in lista:
#     print(elem[int(2)])
# print("-"*80)
# listaa=[]
# with open("TXT_allomanyok/naplo.txt", encoding="UTF-8") as f:
#     for sor in f:
#         sor = sor.strip().replace('#', '')
#
#         # nap = sor[0].replace('#', '').strip().split()
#         # nev = sor[1].strip().split()
#         # rendszam = sor[2].strip().split()
#         listaa.append(sor)
#
# for nev in listaa:
#     print(nev)
# print("-"*80)
#
# print(50*("-"))
# lista=[]
# with open("TXT_allomanyok/nevek.txt", encoding="UTF-8") as f:
#     fejlec = f.readline()
#     for adat in f:
#         sor = adat.strip().split()
#         vnev = sor[0]
#         knev = sor[1]
#         if len(sor)>2:
#             kknev = sor[2]
#             nevek=[vnev, knev, kknev]
#             lista.append(nevek)
#         else:
#             nevek=[vnev,knev]
#             lista.append(nevek)
#
# for elem in lista:
#     print(elem[1])
#
# print(len(lista))
# print(50*("-"))
# for elem in lista:
#     if len(lista)>2:
#         print(f"{elem[0]} {elem[1]} {elem[2]}")

# db=0
# if sor[2] in lista:
#     print(f"igen van 2 keresztnév"+sor[2]+"!")
#     db+=1
# else:
#     print(f"nincs 2 keresztnév")
#
# print(f"A névsorban {len(adat.replace(' ' , ''))} név szerepel, amiben {adat.lower().count('n')} névben van n-betű!")
#
# if vnev == vnev:
#     print(f"Igen van! ")
# else:
#     print(f"Nincs! ")
#
# if knev == knev:
#     print(f"Igen van! ")
# else:
#     print(f"Nincs! ")


# hossz=len(vnev)
# for vnev in nevek:
#     len(vnev)
#     print(vnev[-1])
# print(knev[1:2])

# print("-"*80)
#
# lista=[]
# with open("TXT_allomanyok/negyedevesberek.txt", encoding="UTF-8") as f:
#     megye = f.readline().strip()
#     for adat in f:
#         sor = adat.strip().split()
#         #megye= f.readline()
#         lista.append(megye + adat)
#
# print(lista)

# lista=[]
# with open("TXT_allomanyok/playlist.csv", encoding="utf=8") as f:
#     for adat in f:
#         sor = adat.strip().split()
#
#         nap = int(sor[0])
#         ido = sor[1]
#         rendszam = sor[2]
#         azonosito = sor[3


#playlist!!!!!!!!

egy=[]
with open ("TXT_allomanyok/playlist.csv", encoding="UTF-8") as f:
    for adat in f:
        adat = adat.strip().split(";")
        eloado = adat[0]
        cim = adat[1]
        mufaj = adat[2]
        hossz = int(adat[3])
        egy.append(adat)
        # print(eloado, cim, mufaj, hossz)

for elem in egy:
    if elem[2]=="rock":
        print(f"{elem[0]} {elem[1]} {elem[2]} {elem[3]}")




        # eloado = adat[0]
        # cim= adat[1]
        # mufaj= adat[2]
        # hossz= len(adat[3])
        #
        # elso_feladat=[eloado,cim,mufaj,]
        # elso_feladat.append(egy)
# print(adat)

#2.
# print(len(egy))
#3.






