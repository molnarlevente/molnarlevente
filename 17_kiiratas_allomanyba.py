        #           kiírás fájlba!




with open("kiiratasok/elsokiiras.txt", "w", encoding="UTF-8") as f:
    f.writelines("Szia Levi!")          #soronként ír ki állomány

szoveg =    "Szia Levi!     Most már változóból! "

with open("kiiratasok/masodikkiiras.txt", "w", encoding="UTF-8") as f:
    f.writelines(szoveg)