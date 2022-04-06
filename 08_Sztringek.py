 # karakterlánc

# egységben kezelt str
# srt nem modosítható
# csak kis betű => upper  ,   csak nagy betű    ==>   lower    ,    swapcase  ==>  ellentétes
# split => darabolás


sztring= "Járványhelyzet"
#csak nagy betű    ==>   lower
print(sztring.lower())

# csak kis betű => upper
print(sztring.upper())

#swapcase  ==>  ellentétes
print(sztring.swapcase())

#nem módosul
print(sztring)

#részenként kezelve
print(sztring[1])                   # elem kiiratása# ===> 0-tól kell kell nézni az indexeket
print(len(sztring))                 # a sztring száma ami 1-től számol minden karaktert ami ""-n belül van
print(sztring[-1])                  # az utlsó kiiratása, visszafelé számol
print(list(enumerate(sztring)))     # kiiratni az indexeket str-ből int-be tehát az indexek mellé írja a megfelelő betűt is


hossz  = len(sztring)               # sztring hossza
utolso = sztring[hossz-1]           # az utolsó elem megkeresése index miatt a -1   =>   ha olyan indexre mutat amely nincs akkor túl csordul hibára fut.
print(hossz)
print(utolso)

#vagy egysorban

print(sztring[len(sztring) - 1])    # a kettő ugyan az

#sztring bejárása for ciklussal

for elem in sztring:
    print(elem, end=' ')


#vagy whlie-al

i=0
while i < len(sztring):
    print((i), sztring[i])
    i+=1

















