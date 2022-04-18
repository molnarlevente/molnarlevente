# kerdes1=int(input("Kérek egy pozitív egész számot: "))
# lista=1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 or 10
# # if kerdes1%2==0:
# #     print("2")
# # else:
# #     if kerdes1%3==0:
# #         print("3")
# #     else:
# #         if kerdes1 % 4 == 0:
# #             print("4")
#
# if kerdes1%lista:
#     print(f"A/az {kerdes1} osztható:")
print()
#range(1, kerdes)
# for kerdes in range(1, kerdes):
#       if kerdes % 1 or 2 or 3== 0:
#             print(kerdes, end=' ;')


# kerdes =int(input("Kérek egy pozitív egész számot: "))
# osztok=[1,2,3,4,5,6,7,8,9,10]
#
#
# for i in osztok:
#     print()
#




a=float(input("Kérem a három szög oldalát: "))
b=float(input("Kérem a három szög oldalát: "))
c=float(input("Kérem a három szög oldalát: "))

s= (a+b+c)/2
t= (s*(s-a)*(s-b)*(s-c))
T= t//t

if a + b < c:
    print(f"nem lehet")
else:
    if a + c < b:
        print("nem lehet")
    else:
        if b + c < a:
            print("nem lehet")
        else:
            print(f"A háromszög Kerülete = {a + b + c} mivel a {a}+{b}+{c} = {a + b + c} egység!")
            print(f"A háromszög Területe = {T} mivel a")

