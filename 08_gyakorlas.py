#   majd kiszámolja és kiírja annak osztóit! Az osztók egy sorban, pontosvesszővel elválasztva jelenjenek meg!A program várt működése pl. a következő:
#       Írj be egy pozitív egész számot: 15
#           15 osztói:
#           1; 3; 5; 15

#
# while True:
#     try:
#         szaam = int(input("Kérek egy pozitív egész számot: "))
#     except ValueError:
#         print("Nem számot adtál meg!")
#     else:
#         for osztok in range(1, szaam):
#             if szaam % osztok==0:
#                 print(osztok , end='; ')
# print()
#
#
#
#
#
#
#
#
#

#
#
#
# print()
#
#
#
#
#
#
#
#
#
# print()
# #range(1, kerdes)
# # for kerdes in range(1, kerdes):
# #       if kerdes % 1 or 2 or 3== 0:
# #             print(kerdes, end=' ;')
#
#
# # kerdes =int(input("Kérek egy pozitív egész számot: "))
# # osztok=[1,2,3,4,5,6,7,8,9,10]
# #
# #
# # for i in osztok:
# #     print()
# #
#
#
#
# import math
#
# a=float(input("Kérem a három szög oldalát: "))
# b=float(input("Kérem a három szög oldalát: "))
# c=float(input("Kérem a három szög oldalát: "))
#
# s= (a+b+c)/2
# t= (s*(s-a)*(s-b)*(s-c))
# # T= ((t**t)*t)
# # T= (t**t)
# T= math.sqrt(t)
#
# print(T)
#
# if a + b < c:
#     print(f"nem lehet")
# else:
#     if a + c < b:
#         print("nem lehet")
#     else:
#         if b + c < a:
#             print("nem lehet")
#         else:
#             print(f"A háromszög Kerülete = {a + b + c} egység!")
#             print(f"A háromszög Területe = {T} egység!")
#
#


print("3.feladat! ")
# b=0
# a=0
# c=0
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
#             c = b + a
#             a = b + c
#             b = a + c
#         if b or a or c == szam**2:
#             print()




















