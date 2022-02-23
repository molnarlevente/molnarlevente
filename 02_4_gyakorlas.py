#for n in ["1. ","2. ","3. ","4. "]:
    #szamolas = 'Szia ' + n + ' láttalak.'
    #print(szamolas)

print()

#for z in ["Zsuzsi", "Keke", "Anita"]:
    #meghivo = "Szia, " + z + "! Kérlek gyere el velem a moziba."
    #print(meghivo)


print()

#a = 12
#b = 20
#c = (a + b)
#for y in [c]:
    #eredmeny ='Az eredmény, 12 + 20 = ' + c + '.'
    #print(eredmeny)




import turtle
ablak = turtle.Screen()
ablak.bgcolor("lightgreen")
ablak.title("Blanka & Levi")

Blanka = turtle.Turtle()
Blanka.color("white")
Blanka.pensize(8)

Levi = turtle.Turtle()
Levi.color("black")
Levi.pensize(8)

for a in [0, 1, 2, 3]:
    Blanka.forward(200)
    Blanka.left(90)

for a in [0, 1, 2, 3]:
    Blanka.forward(200)
    Blanka.right(90)

for a in [0, 1, 2, 3]:
    Blanka.left(90)
    Blanka.forward(200)

for a in [0, 1, 2, 3]:
    Blanka.right(90)
    Blanka.forward(200)





