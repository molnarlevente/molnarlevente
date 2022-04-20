#       while utasítás


# while felvézel
#         --       ciklustörzs


valasz = int(input("Kérek ide egy számot: "))
kezdo  = 0
osszeg = 0

while kezdo <= valasz:
    osszeg += kezdo
    kezdo  += 1
print(f"1.: {osszeg}" )


#
print()

osszeg2 = 0
for i in range(valasz+1):
    osszeg2 += i
print(f"2.: {osszeg2}" )

#       --       középen tesztelő ciklus:

print()
osszeg3=0
while True:                         #ism. a ciklust újra és újra == ameddig nem ==> True
    bemenet1 = input("Kérek egy számot: ")
    if bemenet1 == '':
        break
    osszeg3 += int(bemenet1)
print(f"itt az eredmény: {osszeg3}!")



       # --       hátul tesztelő ciklus:
print()

while True:
    jelszo1 = input("Kérek egy jelszót: ")
    jelszo2 = input("Kérek még egy jelszót: ")
    if jelszo1 == jelszo2:
        break
    print(f"A két jelszó nem egyezik meg! {jelszo1} és {jelszo2} nem jó!!   Próbáld újra!")
print(f"Helyes a két jelszó!")

      #
      # --
print()


while True:
    j1 = input("Kérek egy jelszót: ")
    j2 = input("Kérem újra a jelszót: ")
    if j1 == j2:
        break
    print(f"nem megeggyezik")
print(f"igen egyezik meg")

print()
osszeg3=0
while True:                         #ism. a ciklust újra és újra == ameddig nem ==> True
    bemenet1 = input("Kérek egy számot: ")
    if bemenet1 == '':
        break
    osszeg3 += int(bemenet1)
print(f"itt az eredmény: {osszeg3}!")

osszeg=0
while True:
    bemenet= input("Kérek egy számot: ")
    if bemenet == '':
        break
    osszeg += int(bemenet)
print(f"itt az eredmény: {osszeg}!")

print("köv:")
print()
#
# osszeg1=10
# while True:
#     bemenet1=input("Kérek egy számot: ")
#     if bemenet1 + osszeg1 == 30:
#         break
#     osszeg1 += int(bemenet1)
# print(f"10 a kezdő érték mennyit kell hozzá adni hogy 30 legyen?: ")










