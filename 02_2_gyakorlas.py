print()             # ki iratás

a = 1 + 1           # 1
b = 1 - 1           # 0
c = 2 * 2           # 4
d = 2 ** 3          # 12
x = 2 / 2           # 1.0
y = 2 // 2          # 1        %- osztás maradékát mutatja meg
e = 'Molnár Levente'
len(e)

print(a, b, c, d, e, x, y)
print()
for f in [a, b, c, d, e, x, y]:
    print(f)
print()

knev = "Levente"
vnev = "Molnár"
print(knev+vnev)

print()

bicikli = "kerék-, kormány-, váz-, csengő-"
for g in 'bicikli':
    print("Keresek egy kerékpárt, azaz, "+ bicikli +"t")

# str   =   sztring ("szia", "17")        )
# float =   float   (17.0)                } ---> tipuskonverzek
# int   =   int     (17)                  )
# szimantika = program jelentése
# szimantika hiba =  a programozó által szánt jelentés elhibázása -> más lesz a jelentése
# print() = kiiratás
# len() =   karakter számolása
# szkript = fájlban tárolt program
# értékadás                 =
# egyenlőség vizsgálata     ==
# range ->
# pass -> ne fusson hibára
# for ciklus -->

print()

z=1
k=1
print(k==z)     # egyenlőség vizsgálata (==) false or true
print(a==x)

print()

m= len("Levi")
n= len("Dani")
print(m == n)


for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print(i, end=', ')
    print(i)

print()
for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print(i, end=', ')

print()
for i in range(1, 11, 2):
    print(i, end=' ,')
print()
for i in range(2, 11, 2):
    print(i, end=' ,')

print()






