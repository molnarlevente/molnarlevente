# naplo={}
# with open("erettsegi_feladtaok_allomany/info_feladat/2017_okt/naplo-2.txt") as f:
#     for sor in f:
# #print(sor.strip().split())
#         if sor [0]  ==  "#":
#             datum_hesteg = sor.strip().split()
#             datum = datum_hesteg[1] + " " + datum_hesteg[2]
#             naplo[datum] = []
#         else:
#             bejegyzes = sor.strip().split()
#             naplo[datum].append([bejegyzes[0] + " " + bejegyzes[1], bejegyzes[2]])
#
# print(naplo)




print("-" * 65)

# megbeszeles=[]
#
# with open("erettsegi_feladtaok_allomany/info_feladat/2018_maj/fogado.txt") as f:
#     for sor in f:
#         adatok = sor.strip().split()
#         tanar = adatok[0] + " " + adatok[1]
#         idopont = adatok[2]
#         foglalas_datuma = adatok[3]
#         foglalas_idopontja = adatok[4]
#
#         adat=(tanar,idopont,foglalas_datuma,foglalas_idopontja)
#
#         megbeszeles.append(adat)
# print(megbeszeles)

print("-" * 65)
#
# autok_lista = []
# with open("erettsegi_feladtaok_allomany/autok.txt", encoding="UTF-8") as f:
#     for adat in f:
#         sor = adat.strip().split()
#
#         nap=int(sor[0])
#         ido=sor[1]
#         rendszam=sor[2]
#         azonosito=int(sor[3])
#         km=int(sor[4])
#         # if sor[5] == 0:
#         #     ki = "ki"
#         # else:
#         #     be = "be"
#         ki_be_hajtas=int(sor[5])
# #
#         adatok=[nap,ido,rendszam,azonosito,km,ki_be_hajtas]
#         autok_lista.append(adatok)

print("-" * 65)
# megoldas=[]
# with open("erettsegi_feladtaok_allomany/info_feladat/2019_maj/beosztas.txt", encoding="UTF-8") as f:
#     for adat in f:
#         sor = adat.strip().split)()
#
#         tanar = sor[0]
#         tantargy = sor[1]
#         osztaly = sor[2]
#         oraszam = sor[3]
#
#         adatok=[tanar, tantargy, osztaly, oraszam]
#         megoldas.append(adatok)
#
# print(megoldas)

print("-" * 65)
# mego_=[]
# with open("erettsegi_feladtaok_allomany/info_feladat/2020_maj/tavirathu13.txt", encoding="UTF-8") as f:
#     for adat in f:
#         sor= adat.strip().split()
#
#         telepules= sor[0]
#         ido=int(sor[1])
#         szelirany_es_erosseg= int(sor[2])
#         homerseglet= int(sor[3])
#
#         adatok=[telepules, ido, szelirany_es_erosseg, homerseglet]
#        mego_.append(adatok)
# print=mego_

print("-" * 65)
# lista=[]
# with open("erettsegi_feladtaok_allomany/lista-1.txt", encoding="UTF8") as f:
#     for sor in f:
#         adat = sor.strip().split()
#         if len(adat) == 5:
#             datum=adat[0]
#             sorozat=adat[1]
#             resze=adat[2]
#             hossza=adat[3]
#             latta = adat[4]
#             adatok=[datum,sorozat,resze,hossza,latta]
#             lista.append(adatok)
#
# print(adat)
print("-" * 65)
kesz=[]
with open("erettsegi_feladtaok_allomany/info_feladat/2019_okt/utasadat.txt", encoding="UTF=8") as f:
    for adat in f:
        sor = adat.strip().split()

        megallo_sorszama= sor[0]
        datum= sor[1]
        azonosito= sor[2]
        tipus= sor[3]
        if tipus == "FEB":
            print("Felnőtt bérlet")
        else:
            if tipus == "TAB":
                print("Tanulóbérlet (kedvezményes) ")
            else:
                if tipus == "NYB":
                    print("Nyugdíjas bérlet (kedvezményes) ")
                else:
                    if tipus == "NYP":
                        print("65 év feletti bérlet (ingyenes) ")
                    else:
                        if tipus == "RVS":
                            print("Rokkant, vak, siket vagy kísérő bérlet (ingyenes)")
                        else:
                            if tipus == "GYK":
                                print("Iskolakezdés előtti gyerekbérlet (ingyenes)")
                            else:
                                if tipus == "JGY":
                                    print("jegy")
        ervenyes= sor[4]

        adatok=[megallo_sorszama, datum, azonosito, tipus, ervenyes]
        kesz.append(adatok)

print(kesz)

print("-" * 65)

# listaa=[]
# with open("erettsegi_feladtaok_allomany/info_feladat/2017_maj/furdoadat.txt", encoding="UTF=8") as f:
#     for adat in f:
#         sor = adat.strip().split()
#
#         vendeg_azonosito= int(sor[0])
#         furdo_azonosito= int(sor[1])
#         ki_be_lepes = int(sor[2])
#         if ki_be_lepes == 0:
#             ki_be_lepes = "be"
#         else:
#             ki_be_lepes = "ki"                                          ########## ?????????????? intbe ora perc ms
#         idopontok= int(sor[3]), int(sor[4]), int(sor[5])
#
#         adatok=[vendeg_azonosito, furdo_azonosito, ki_be_lepes, idopontok]
#         listaa.append(adatok)
#
# print(listaa)


print("-" * 65)

# liszt=[]
# with open("erettsegi_feladtaok_allomany/info_feladat/2016_okt/hivas.txt", encoding="UTF=8") as f:
#     for adat in f:
#         sor = adat.strip().split()
#
#         idopont_egy= sor[0:3]
#         idopont_ketto= sor[3:6]
#
#         adatok=[idopont_egy, idopont_ketto]
#         liszt.append(adatok)
#
# print(liszt)

print("-" * 65)

# listta=[]
# with open("erettsegi_feladtaok_allomany/info_feladat/2016_maj/penztar.txt", encoding="UTF=8") as f:
#     for adat in f:
#         sor = adat.strip("F").split()
#         kosar = sor[0]                                               ####################   BEF   #####################
#
# print(listta)

import random

def dob():
    return "I" if random.randint(1, 2) == 1 else "F"

print("1. feladat")
print(f"Pénzfeldobás eredménye: {dob()}")

print("2. feladat")
tip=input("Tippeljen! (F/I) = ")
if tip == dob():
    print("Ön eltalálta.")
else:
    print("Ön nem találta el.")

print("3. feladat")

with open("erettsegi_feladtaok_allomany/info_feladat/2015_okt/kiserlet.txt", encoding="UTF=8") as f:
    szm = 0
    for adat in f:
        szm += 1
    print(f"A kísérlet {szm} dobásból állt.")

#
# print("-" * 65)
#
# lissta = []
# with open("erettsegi_feladtaok_allomany/info_feladat/2015_maj/veetel.txt", encoding="UTF=8") as f:
#      for adat in f:
#          sor = adat.strip().split()
#
# print("-" * 65)
#
# with open("erettsegi_feladtaok_allomany/info_feladat/2015_maj/veetel.txt", encoding="UTF=8") as f:
#     for adat in f:
#         sor = adat.strip().split()

# print("-" * 65)
#
# with open("erettsegi_feladtaok_allomany/info_feladat/2014_maj/ip.txt", encoding="UTF=8") as f:
#     for adat in f:
#         sor = adat.strip().split(":")
#         print(sor)
#
# print("-" * 65)
# adatoook=[]
# with open("erettsegi_feladtaok_allomany/info_feladat/2013_okt/jarmu-1.txt", encoding="UTF=8") as f:
#     for adat in f:
#         sor = adat.strip().split(":")
#         rendszam= adat[3]
#         ora= adat[0]
#         perc= adat[1]
#         msperc= adat[2]
#
#         adatok=[rendszam,ora,perc,msperc]
#         adatoook.append(adatok)
#
# print("-" * 65)
#
# liszzt=[]
# with open("erettsegi_feladtaok_allomany/info_feladat/2013_maj/szavazatok-1.txt", encoding="UTF=8") as f:
#     for adat in f:
#         sor=adat.strip().split()
#         sorszam= adat[0]
#         szavazat= adat[1]
#         vnev= adat[2]
#         knev= adat[3]
#         adata=adat[4]
#         adatok=[sorszam,szavazat,vnev,knev,adata]
#         liszzt.append(adatok)
#
# print("-" * 65)
#
# with open("erettsegi_feladtaok_allomany/info_feladat/2012_okt/kep.txt", encoding="UTF=8") as f:
#     for adat in f:
#         sor=adat.strip().split()
#
# print("-" * 65)
# llista=[]
# with open("erettsegi_feladtaok_allomany/info_feladat/2012_maj/tavok.txt", encoding="UTF=8") as f:
#     for adat in f:
#         sor=adat.strip().split()
#         nap_sorszam=adat[0]
#         fuvarszam= adat[1]
#         km= adat[2]
#         adatokook=[nap_sorszam,fuvarszam,km]
#         llista.append(adatokook)
#
# print("-" * 65)
#
# szo=input('1. feladat Adjon meg egy szót: ')
# with open("erettsegi_feladtaok_allomany/info_feladat/2011_maj/szoveg.txt", encoding="UTF=8") as f:
#     for adat in f:
#         if szo == adat:
#             if szo=="a" or "e" or "i" or "u" or "o":
#                 print("Van benne magánhangzó.")
#         else:
#             print("Nincs benne magánhangzó.")
#
# print("2. feladat")
#
#
#
# print("-" * 65)






