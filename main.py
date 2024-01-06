# Żółwik - rysowanie kwiatu
import turtle

turtle.speed(2)

# Rysowanie pojedynczego płatka
turtle.color("red")
turtle.begin_fill()
turtle.circle(50, 60)
turtle.left(120)
turtle.circle(50, 60)
turtle.end_fill()

# Rysowanie całego kwiatu
for _ in range(6):
    turtle.color("red")
    turtle.begin_fill()
    turtle.circle(50, 60)
    turtle.left(120)
    turtle.circle(50, 60)
    turtle.end_fill()
    turtle.left(60)
