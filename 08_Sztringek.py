#  # karakterlánc
#
# # egységben kezelt str
# # srt nem modosítható
# # csak kis betű => upper  ,   csak nagy betű    ==>   lower    ,    swapcase  ==>  ellentétes
# # split => darabolás
#
#
# sztring= "Járványhelyzet"
# #csak nagy betű    ==>   lower
# print(sztring.lower())
#
# # csak kis betű => upper
# print(sztring.upper())
#
# #swapcase  ==>  ellentétes
# print(sztring.swapcase())
#
# #nem módosul
# print(sztring)
#
# #részenként kezelve
# print(sztring[1])                   # elem kiiratása# ===> 0-tól kell kell nézni az indexeket
# print(len(sztring))                 # a sztring száma ami 1-től számol minden karaktert ami ""-n belül van
# print(sztring[-1])                  # az utlsó kiiratása, visszafelé számol
# print(list(enumerate(sztring)))     # kiiratni az indexeket str-ből int-be tehát az indexek mellé írja a megfelelő betűt is
#
#
# hossz  = len(sztring)               # sztring hossza
# utolso = sztring[hossz-1]           # az utolsó elem megkeresése index miatt a -1   =>   ha olyan indexre mutat amely nincs akkor túl csordul hibára fut.
# print(hossz)
# print(utolso)
#
# #vagy egysorban
#
# print(sztring[len(sztring) - 1])    # a kettő ugyan az
#
# #sztring bejárása for ciklussal
#
# for elem in sztring:
#     print(elem, end=' ')
#
#
# # vagy whlie-al
#
# i=0
# while i < len(sztring):
#     print((i), sztring[i])
#     i+=1

# sztring szeletelés

gyumolcs= "szederfa"
#
# print(gyumolcs[0:3])        # az elejétől a harmadik indexen szerepelő betűig íratjuk ki
# print(gyumolcs[0:400])      # ez végig kiírja
#
# # in not in operátorok                      OPERÁTOROK HASZNÁLATA
#
# print('a' in gyumolcs)      # az 'A' megtalálható a gyümölcs változóban?
#
# if "a" in gyumolcs:
#     print(" igen szerepel benne az 'A'")
#
#
# print('a' not in gyumolcs)      # az 'A' NEM megtalálható a gyümölcs változóban?
#
# if "a" not in gyumolcs:
#     print(" NEM szerepel benne az 'A'")  # csak akkor lép bele a printbe ha igaz a feltétel
# else:
#     print(" IGEN szerepel benne az 'A'")


betu= input("Kérek egy betűt: ")
index=0

if betu not in gyumolcs:                    # megvizsgálom van-e benne
    print("Nem szerepel ilyen karakter!")
else:
    print("Igen van benne ilyen karakter!")
    index = 0
    for i in gyumolcs:                         # ha van benne akkor megnezem hanyadik
        if betu==i:
            print(f"ez a/az {betu} a {index+1} helyen szerepel!")
            #break      # ha csak az első találatot akarjuk kiírni
        index+=1





