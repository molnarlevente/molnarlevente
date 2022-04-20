# while True:
#     jelszo1 = input("Kérek egy jelszót: ")
#     jelszo2 = input("Kérek még egy jelszót: ")
#     if jelszo1 == jelszo2:
#         break
#     print(f"A két jelszó nem egyezik meg! {jelszo1} és {jelszo2} nem jó!!   Próbáld újra!"

#   VÁLTOZÓ = valasz !!!!!!!!!!!!!!!!!!!!!!

valasz = input("Kérek egy valamit: ")
print(f"Köszönöm! a valaszod a kérdésre: {valasz}!")

#kör sugarát bekérjük és a terület kiszámítása
  # pi => 3,14159
#        terület = r(2) x pi


sugar = float(input("Kérem írja be a kör sugarát: "))
terulet = sugar**2 * 3,14159
print(f"A kör területe: {terulet}!")

#vagy

sugar2 = float(input("Kérem írja be a kör sugarát2: "))
print(f"A kör területe: {sugar2**2 * 3.14159}!")

#vagy


print(print("A kör területe: ", float(input("Kérem írja be a kör sugarát3: "))**2 * 3.14159))


#a megadott érték ellenőrzése: !! try , expet !!

try :
    valasz_szam1 = int(input("Kérek egy egész számot: "))
except ValueError:
    print("Nem számot adtál meg!")

#addig ne engedje abba hagyni  amíg nem szam!

while True:
    try:
        valasz_szam2 = int(input("Kérek egy egész számot: "))
    except ValueError:
        print("Nem számot adtál meg!")
    else:
        print(f"Köszönöm a: {valasz_szam2} !!")
        break


#str-re

valasz_nev2 = input("Kérlek ird be a neved: ")                                #.isdigit() ==> bool típust kapok True/False, amit while-al már tudok vizsgálni!
print(valasz_nev2.isdigit())

valasz_nev3 = input("Kérlek ird be a neved: ")
while valasz_nev3.isdigit()==True or valasz_nev3 == " ":
    valasz_nev3= input("Nem adtad meg jól!!  kérem újra:\n add meg újra a nevedet: ")
print(f"Köszönöm a választ, a neved: {valasz_nev3}!")

valasz_nev4 = input("Kérek egy számot: ")
while valasz_nev4.isdigit() !=True or valasz_nev4 == " ":                       #(isdecimal() ==>)
    valasz_nev4= input("Nem adtad meg jól!! \n Add meg újra a számot: ")
print(f"Köszönöm a választ, a szám: {valasz_nev4}!")

# while True:
#     try:
#         valasz_nev = input("Kérlek ird be a neved: ")
#     except ValueError:
#         print("Biztos a nevedet adtad meg?")
#     else:
#         print(f"Köszönöm a {valasz_nev}-t!")
#         break1












