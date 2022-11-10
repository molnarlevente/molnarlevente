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


# print("7. feladat")
# rendszam=input("Rendszámot: ")
# lista=[]
# with open(f"kiiratasok/{rendszam}_menetlevel.txt", "w", encoding="UTF-8") as f:
#     for elem in lista:
#         f.writelines(f"{str(elem)} ")
#
# print(rendszam)
# print("Menetlevél kész.")
#

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
#
# print("2. Feladat")
# print(f"Foglalkozások száma: {len(megbeszeles)}")
#
# print("3. Feladat")
#
# nev = input("Adjon meg egy nevet: ")
# db=0
# for megbeszelesek in megbeszeles:
#     if megbeszelesek[1] == nev:
#         db += 1
# if db == 0:
#     print(" A megadott néven nincs időpontfohlalás.")
# else:
#     print(f"{nev} néven {db} időpontfoglalás van.")
#
# print("4. feladat")
# idopontt = input("Adjon meg egy érvényes időpontot (pl. 17:10): ")
# tanarok=[]
# for megbeszelesek in megbeszeles:
#     if megbeszelesek[2] == idopontt:
#         tanarok.append(megbeszeles[2])
# tanarok.sort()
#
# fajl_nev = idopontt[:2] + idopontt[3:] + '.txt'
#
# with open (fajl_nev, "w", encoding="UTF-8") as k:
#     for tanar in tanarok:
#         print(tanar)
#         print(tanar, file=k)
#
# print("5. feladat")
#
# min_idopont = megbeszeles[0]["f_datum"] + "-" + megbeszeles[0]["f_datum"]
# min_index = 0
# for index, megbeszelesek in enumerate(megbeszeles):
#     if megbeszelesek[0]["f_datum"] + "-" + megbeszelesek[0]["f_datum"] < min_idopont:
#         min_idopont = megbeszelesek ["f_datum"] + "-" + megbeszelesek[0]["f_datum"]
#         min_index = index
# print(f"tanar neve: {megbeszeles[min_index][tanar]}")
# print(f"Folalt időpont: {megbeszeles[min_index][idopontt]}")
# print(f"Foglalás ideje: {min_idopont}")
#
# print("6. feladat")
# idoo=[]
# for o in range(6,8):
#     for p in range(0,6):
#         ip = '1' + str(o) + ':' + str(p) + '0'
#         ido[ip]=False
# for megbeszelesek in megbeszeles:
#     if megbeszelesek[0:1] == "Barna Eszter":
#         ido[megbeszelesek[2]] = True
#
#for ta

# kiszűröm a foglalt időpontokat!

#
# from datetime import datetime, timedelta
#
# fogadooralista = []
#
# with open("TXT_allomanyok/fogado.txt", encoding="utf8") as f:
#     for adat in f:
#         sor = adat.strip().split(" ")
#         tanar = sor[0]+" "+sor[1]
#         foglaltido = sor[2]
#         foglalasdatuma = sor[3]
#         fogadooralista.append([tanar,foglaltido,foglalasdatuma])
#
# # for tanar,foglaltido,foglalasdatuma in fogadooralista:
# #     print(foglaltido)
#
# #2. feladat:
# print(f"2. feladat\nFoglalások száma: {len(fogadooralista)}")
#
# #3. feladat:
# #valasztanar = input("3. feladat\nAdjon meg egy nevet: ")
# valasztanar = "Nagy Ferenc"
# #valasztanar = "Farkas Attila"
# db = 0
# for tanar,foglaltido,foglalasdatuma in fogadooralista:
#     if tanar == valasztanar:
#         db += 1
#
# if db > 0 :
#     print(f"{valasztanar} néven {db} időpontfoglalás van.")
# else:
#     print("A megadott néven nincs időpontfoglalás.")
#
# #4. feldat:
# #valaszido = input("4. feladat\nAdjon meg egy érvényes időpontot (pl. 17:10): ")
# valaszido ="17:40"
# tanaroklista = []
# for tanar,foglaltido,foglalasdatuma in fogadooralista:
#     if foglaltido == valaszido:
#         tanaroklista.append(tanar)
#
# tanaroklista = sorted(tanaroklista)
# #tanaroklista.sort(reverse=True) #fordított sorrend
# #tanaroklista.sort()
# #fajlnev = valaszido[:2]+valaszido[3:]+".txt"
#
# for elem in tanaroklista:
#     print(elem)
# with open(f"Kiiratasok/{valaszido.replace(':','')}.txt", "w" , encoding="utf8") as f:
#     for elem in tanaroklista:
#         f.write(f"{elem}\n")
#
# #5. feladat:
# legkisebbdatum = datetime.max
# #print(legkisebbdatum)
# for tanar,foglaltido,foglalasdatuma in fogadooralista:
#     idopont = datetime.strptime(foglalasdatuma, "%Y.%m.%d-%H:%M")
#     #print(idopont)
#     if idopont < legkisebbdatum:
#         legkisebbdatum = idopont
#         adaotttanar = tanar
#         adottidopont = foglaltido
#
#
# #print(legkisebbdatum)
# print(f"\n5. feladat:\nTanár neve: {adaotttanar}\nFoglalt időpont: {adottidopont}\nFoglalás ideje: {legkisebbdatum:%Y.%m.%d-%H:%M}")
#
#
# print("-"*50)
# #6.feladat:
# #kiválogatom a foglalt időpontokat
# foglaltidopontoklista = []
# for tanar,foglaltido,foglalasdatuma in fogadooralista:
#     if tanar == "Barna Eszter":
#         foglaltidopontoklista.append(foglaltido)
#
# foglaltidopontoklista = sorted(foglaltidopontoklista)
# #print(idopontoklista[-1])
# hazamehet = datetime.strptime(foglaltidopontoklista[-1], "%H:%M")
# #print(hazamehet)
# print(f"Barna Eszter legkorábban távozhat: {hazamehet + timedelta(minutes=10):%H:%M}")
#
# idopontoklista = []
# for tanar,foglaltido,foglalasdatuma in fogadooralista:
#     if foglaltido not in idopontoklista:
#         idopontoklista.append(foglaltido)
#
# #print(sorted(idopontoklista))
# idopontoklista = sorted(idopontoklista)
#
# for idok in foglaltidopontoklista:
#     for elem in idopontoklista:
#         if idok == elem:
#             idopontoklista.remove(elem)
#
# for elem in idopontoklista:
#     print(elem)


print()

###      egY ÚJ LISTÁHOZ HOZZÁ ADNI ÉS KIGYUJT AZ ELEMEKET   F.1   !!!!! nem fejeztem be

    # DB += ELEM!!! HOZZÁ ADNI EGY UJ LISTÁHOZ AZTÁN UGY KIIRATNI!  F.2     !!!!! nem ment
        #NEM REMOVE-VAL
                                # 45-60P!!!!!!!!  REGGEL!
    # 2019 MÁJUS IDEGENNYELV!!! UJ PROJECT MINDEN!!! FULL ERETTSEGI SZINTEN! F.3

#       DATETIME



#       HALMAZ MŰVELETEK?????
#           - A készletek rendezetlenek.
#           - A készletelemek egyediek. Az elemek ismétlődése nem megengedett.
#           - Maga a halmaz módosítható, de a halmazban lévő elemeknek változtathatatlan típusúaknak kell lenniük.
#           - Egy készlet kétféleképpen hozható létre. Először is definiálhatunk egy halmazt a beépített set() függvénnyel
#           - Ebben az esetben az <iter> argumentum egy iterálható – jelenleg is gondoljon lista vagy tuple –,
#               amely létrehozza a halmazba foglalandó objektumok listáját.

#
#           STR -> INT  CSAK HA VAN IDŐ!!!!!!

# lista1 = [1,2,3,4,5]
# lista2 = [4,5,6,7,8,9]
# #lista = set(lista1) & set(lista2)
# print(lista1)
# print(lista2)
# print(set(lista1) | set(lista2))
# print(set(lista1) ^ set(lista2))
# print(set(lista1) & set(lista2))
# print(set(lista1) - set(lista2))
# print(sorted(set(lista2) - set(lista1)))

megoldas=[]
with open("erettsegi_feladtaok_allomany/info_feladat/2019_maj/beosztas.txt", encoding="UTF-8") as f:
    for adat in f:                              ### while!!!!!!!!!!!!
        sor = adat.strip().split()
        if len(sor) == 4:
            tanar= sor[0]
            tantargy= sor[1]
            osztaly= sor[2]
            oraszam= int(sor[3])


            #adatok=[tanar,tantargy,osztaly,oraszam]
            megoldas.append([tanar,tantargy,osztaly,oraszam])
print(megoldas)
# for tanar,tantargy,osztaly,oraszam in megoldas:
#     print(tantargy)
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
print(f"2.feladat\nA fájlban {len(megoldas)} bejegyzés van!")



osz_oraszam = 0
for sor in megoldas:
    osz_oraszam += oraszam
print(f"3.feladat\nAz iskolában a heti összóraszám: {osz_oraszam}")


print(f"4.feladat")
#tanarr = input(f"Egy tanár neve= ")
tanarr = "Albatrosz Aladin"

szmlalo=0
for tanar in megoldas:
    if tanar == tanarr:
        szmlalo += oraszam
print(f" A nótanár heti óraszáma: {szmlalo}")



