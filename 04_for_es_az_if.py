list = [5, 47, 8, 54, 6, 2, 15, 4, 1, 25, 10, 65, 17, 321]

# irassuk ki a 20-nál kisebbeket:
for listaelem in list:
    if listaelem <= 20:
        print(listaelem, end=' ,')
print()

# irjuk ki a 20 és a 10 közötti számot
for i in list:
    if i >10 and i <20:
        print(i, end=',')

# irjuk ki a 10-nél kissebb és a 20-nál nagyobb számokat
print()

for f in list:
    if f < 10 or f > 20:
        print(f, end="," )

#irjuk ki a lista elemeit ameddig nem találok 10-et
print()

for g in list:
    print(g, end=',')
    if g == 10:
        break

print("Házi feladat 1 - 6 !!!")
print("+ órai befejezés")


















