#                                                   Listaművelet importálása
# hozzunk látre egy 10 elemből álló listát véletlen számokkal töltsük fel
# a számok 0-100 között generálódjanak

# #modul importálása
import random
#
# lista = []
#
# for elemek in enumerate(range(10)):
#     r = random.randrange(0,101,1)  # a stop index már nincs benne
#     lista.append(r)
#
# print(lista)
# print(50*"_")
#     #   lista kiiratása
#
import random
#
# for elemek in lista:
#     print(elemek, end=", ")
print(50*"_")
    #   egy sorban
list = [random.randrange(0,101,1) for elemek in range(10)]
print(list, end=", ")

#   sorba rendezés és az eredeti lista nem módosul

# for (index, elemek) in enumerate(range(10)):
#     r = random.randrange(0,101,1)         # a stop index már nincs benne
#     print(index,r)

# házi gyakorlás
print()
    #   csak a páros kiiratása => listába tétele
    #   csak a páratlan kiiratása => listába tétele
    #

        # fibonacci!!!!!!!!!!   08_gykorlás végén  # nem sikerült!!
print("_"*50)

#
# lista = [1,2,3,4,5,6,7,8,9,10]
# print(lista for elem in range(0, 10, 2))
import random

lista = [random.randrange(0,100,2) for elem in range(10)]
print(lista, end=", ")

print()
print("_"*50)

listaa = [random.randrange(1,100,2) for elemk in range(10)]
print(listaa, end=", ")

print()
print("_"*50)


listaa = []

for elemek in enumerate(range(10)):
    r = random.randrange(0,100,2)
    listaa.append(r)





