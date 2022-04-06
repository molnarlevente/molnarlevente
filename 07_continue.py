
#    continue   =>      nem break, ez nem lép ki, hanem tovább megy a következőre!!!
#    continue   =>      vezérlés átadó utasítás

lista=[2,6,12,15,18,19,21,24,25,34,39,50]
for paros in lista:
    if paros % 2 == 0:
        print(paros, end=' ')

print()
# vagy

for i in lista:
    if i % 2 == 1:
        continue            #      ==>      vezérlés átadó utasítás
    print(i, end=' ')













