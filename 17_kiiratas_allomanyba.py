        #           kiírás fájlba!
with open("kiiratasok/elsokiiras.txt", "w", encoding="UTF-8") as f:
    f.writelines("Szia Levi!")          #soronként ír ki állomány

        #           változó értékének kiiratása
szoveg =    "Szia Levi!     Most már változóból! "
with open("kiiratasok/masodikkiiras.txt", "w", encoding="UTF-8") as f:
    f.writelines(szoveg)

        #           bekérés
# valasz = input("MI legyen a fájl neve?: ")
valasz = "Teszt_1"
with open(f"kiiratasok/{valasz}.txt", "w", encoding="UTF-8") as f:
    f.writelines("felhasználó álltal megadott fájlnév!")

        #           feladat

#_______hozz létre egy 100 elemből álló listát és töltsd fel véletlen számokkal! (0 és 100 közöttivel)

import random
lista = [random.randrange(0,101,1) for elem in range(100)]
for elem in lista:
    print(elem, end=" ")

print(f"\n A lista {len(lista)} db elemet tartalmaz! ")

#_______rendezzük növekvőbe         ------>        sorted !!!!!!!!!

for elem in sorted(lista):
    print(elem, end=" ")

#_______írjuk ki a listát egy féjlba
with open("kiiratasok/lista.txt", "w", encoding="UTF-8") as f:
    f.writelines(str(lista))

#_______csak az elemek kiiratása egy féjlba

kiiratas = ""
for elem in lista:
    kiiratas += f"{str(elem)} "

with open("kiiratasok/kiirataas.txt", "w", encoding="UTF-8") as f:
    f.writelines(kiiratas)



