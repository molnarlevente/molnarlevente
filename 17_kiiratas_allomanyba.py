        #           kiírás fájlba!
with open("kiiratasok/elsokiiras.txt", "w", encoding="UTF-8") as f:
    f.writelines("Szia Levi!")          #soronként ír ki állomány

        #           változó értékének kiiratása
szoveg =    "Szia Levi!     Most már változóból! "
with open("kiiratasok/masodikkiiras.txt", "w", encoding="UTF-8") as f:
    f.writelines(szoveg)

        #           bekérés
valasz = input("MI legyen a fájl neve?: ")
with open(f"kiiratasok/{valasz}.txt", "w", encoding="UTF-8") as f:
    f.writelines("felhasználó álltal megadott fájlnév!")
