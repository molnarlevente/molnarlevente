naplo={}

with open("erettsegi_feladtaok_allomany/info_feladat/2017_okt/naplo-2.txt") as f:
    for sor in f:
#print(sor.strip().split())
        if sor [0]  ==  "#":
            datum_hesteg = sor.strip().split()
            datum = datum_hesteg[1] + " " + datum_hesteg[2]
            naplo[datum] = []
        else:
            bejegyzes = sor.strip().split()
            naplo[datum].append([bejegyzes[0] + " " + bejegyzes[1], bejegyzes[2]])


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



















