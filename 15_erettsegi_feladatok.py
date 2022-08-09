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
# for elem in lista:
#     print(elem[0])
# print(adat)
#
# print("2.feladat")
#
# db=0
#
# for adatok in adat:
#     if "NI" not in adat[0]: #datum
#         db+=1
#
# print(f"A listában {db} db vetítési dátummal rendelkező epizód van.")
#
#
# print("3.feladat")
#
# szamlalo=0
#
# for adatok in adat:
#     if adatok[latta]==True:
#         szamlalo+=1
#
# szazalek_szam=szamlalo/len(adat) *100
# print(f"A listában lévő epizódok {szazalek_szam}%-át látta.")
#
# print("4.feladat")
# osszes_ido=0
#
# for adatok in adat:
#     if adatok[latta]==True:
#         osszes_ido += hossza
#
# nap=osszes_ido // (24 ** 60)
# ora=osszes_ido % (24 * 60) // 60
# perc=osszes_ido % 60
#
# print(f"Sorozatnézéssel {nap} napot {ora} órát és {perc} percet töltött.")
#
# print("5.feladat")
#
# datum=input(f"Adjon meg egy dátumot! Datum= ")
#
# for adatok in adat:
#     if adatok[latta] <= datum and latta==False:
#         print(resze  )                                      #!!!!!!
#
#
# print("6.feladat")
#

#while True !!!!!!!!!

print("ceges autok" and "*"*100)

                                                                    #_______________________________________________________________________
autok_lista = []
with open("erettsegi_feladtaok_allomany/info_feladat/2020_okt/autok.txt", encoding="UTF-8") as f:
    for adat in f:
        sor = adat.strip().split()

        nap=int(sor[0])
        ido=sor[1]
        rendszam=sor[2]
        azonosito=int(sor[3])
        km=int(sor[4])
        # if sor[5] == 0:
        #     ki = "ki"
        # else:
        #     be = "be"
        ki_be_hajtas=int(sor[5])
#
        adatok=[nap,ido,rendszam,azonosito,km,ki_be_hajtas]
        autok_lista.append(adatok)

# for elem in autok_lista:
#     print(rendszam)
#
# print("2. feladat")
#
# for elem in autok_lista:
#     if elem[5] == 0:
#         nap = elem[0]
#         rendszam = elem[2]   # az utolso marad benne amit eltárol !!!!
#
# print(f"{nap} nap rendszám: {rendszam}")
#
# print("3. feladat")
#
# #bekeret_nap=input("Nap: ")
# bekeret_nap = 4
# print(f"Forgalom a(z) {bekeret_nap} napon:")
# for elem in autok_lista:
#
#     # if elem[5] == 0:
#     #     ki = "ki"             # nem kell, felesleges
#     # else:
#     #     be = "be"
#
#
#     if elem[0] == bekeret_nap:
#         if elem[5] == 0:
#             print(f"{elem[1]} {elem[2]} {elem[3]} ki")
#         else:
#             print(f"{elem[1]} {elem[2]} {elem[3]} be")
#
#
# print("4. feladat")
# db=0
# db2=0
# for elem in autok_lista:
#     if ki_be_hajtas==0:
#         db+=1
#     else:
#         db2+=1
#
# print(f"A hónap végén {db-db2} autót nem hoztak vissza.")
#
# print("5. feladat")
# rendszamoklista=[]
# for elem in autok_lista:
#     if sor[2] not in rendszamoklista:
#         sor[2] += rendszamoklista
#
# rendszamoklista = sorted(rendszamoklista)                           ### sorted
# #print(rendszamoklista)
#
# for adat_rendszam in rendszamoklista:
#     megtett_km_ek = []
#     for elem in autok_lista:
#         if adat_rendszam == elem[2]:
#             megtett_km_ek.append(elem[4])
#
#     kezdo_km = megtett_km_ek[0]
#     utolso_km = megtett_km_ek[-1]
#     megtettkm= utolso_km - kezdo_km
#
#     print(f"{adat_rendszam} {megtettkm} km")
#
# print("6. feladat")
#
# leghoszabb_ut = 0
#
# for adat_rendszam in rendszamoklista:
#     for elem in autok_lista:
#         if adat_rendszam == elem[2]:
#             if elem[5] == 0:
#                 kezdo_km_allas = elem[4]
#             if elem[5] == 1:
#                 ut_hossza = elem[4] - kezdo_km_allas
#                 if leghoszabb_ut < ut_hossza:
#                     leghoszabb_ut = ut_hossza
#                     dolgozo_azonosito = elem[3]
#
# print(f"Leghosszabb út: {leghoszabb_ut} km, személy: {dolgozo_azonosito}")


print("7. feladat")                         # hf!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
rendszam=input("Rendszámot: ")
lista=[]
with open(f"kiiratasok/{rendszam}_menetlevel.txt", "w", encoding="UTF-8") as f:
    for elem in lista:
        f.writelines(f"{str(elem)} ")

print(rendszam)
print("Menetlevél kész.")










