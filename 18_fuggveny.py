#függvény írása
# def (függvényneve) () :
    # pass

def osszead():
    print(5+4)

#függvény meghívása
osszead()

#viszatérési érték -- return

#
#szorzás függvény paramétereivel:                   ----------------- PRAMÉTER

#def sorzas_fuggveny(a,b):       #paraméter létrehozása
#    return a*b                  # visszatérési érték

#print(sorzas_fuggveny(5,7))     # az 5 = x, b = y,
# meg kell adni az x és az y értékét!!!!!!!!!!!!

#hf messenger!!!!

print("1. feladat")
#x = int(input(" N darab sor:"))
#y = int(input(" M darab oszlop: "))
#
# def oszlop_sor(N,M):
#     for i in range(M):
#         print("*"*N)
#
#
# oszlop_sor(int(input(" N darab oszlop:")),int(input(" M darab sor: ")))
# #oszlop_sor(x,y)

print("2. feladat")
#bekeres=int(input("Kérek egy egész számot: "))

# while True:
#     bekeres=int(input("Kérek egy egész számot: "))
#     if bekeres%2==0 and bekeres%3==0:
#         break
#     print("Osztható mindkettővel!")
# print(f"Nem osztható! 2-vel és 3-al")


# bekeres1=int(input("Kérek egy egész számot: "))
# if bekeres1%2==0 and bekeres1%3==0:
#     print(True)
# else:
#     print(False)


def fedalat2(x):
    if x % 2 == 0 and x % 3 == 0:
    #     print("JO")
    # else:
    #     print("rossz")
        return True

if fedalat2(int(input("Kérek egy számot: "))) == True:
    print("Ostható")
else:
    print("Nem osztható")



def szorzas():
    a=4
    b=6
    return(a*b)
print(szorzas())

def osszeadas(c,d):
    return c*d
print(osszeadas(2,5))











