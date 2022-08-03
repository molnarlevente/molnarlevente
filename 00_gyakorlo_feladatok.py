# while True:
#     try:
#         szam = int(input("Kérek egy pozitív egész számot: "))
#     except ValueError:
#         print("Nem számot adtál meg!")
#     else:
#         for i in a:
#             a = 0
#             b = 1
#             c = a + b
#             a = b + c
#             b = a + c
#
#         if b or a or c == szam:
#             print()


#fibonaci

#valasz=int(input("Kérek egy számot: "))
# valasz=15

# elsoelem = 0
# masodikelem = 1
# harmadikelem = 0
# fibonacci = [0,1]
#
# for elem in range(valasz):
#     harmadikelem=elsoelem+masodikelem
#     fibonacci.append(harmadikelem)
#     elsoelem = masodikelem
#     masodikelem = harmadikelem
#
# print(fibonacci)

        #       vagy !!!!!!!!!!!!!!

#valasz=int(input("Kérek egy számot: "))
valassz=15
fibonaci=[0,1]

for elem in range(valassz):
    harmadikelem2 = fibonaci[0+elem]+fibonaci[1+elem]
    fibonaci.append(harmadikelem2)
print(fibonaci)

##################### 6- os github