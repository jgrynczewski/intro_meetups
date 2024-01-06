# Żółwik - Fraktal
import turtle


def draw_branch(branch_length, t):
    if branch_length > 5:
        # Rysowanie gałęzi
        t.forward(branch_length)
        t.right(20)
        draw_branch(branch_length - 15, t)

        # Powrót do poprzedniej pozycji
        t.left(40)
        draw_branch(branch_length - 15, t)

        # Powrót do korzenia
        t.right(20)
        t.backward(branch_length)


def main():
    screen = turtle.Screen()
    screen.bgcolor("black")

    t = turtle.Turtle()
    t.color("green")
    t.width(2)
    t.speed(0)

    # Ustawienie żółwia na górnej części ekranu
    t.left(90)
    t.up()
    t.backward(200)
    t.down()

    # Narysuj fraktal
    draw_branch(100, t)

    screen.exitonclick()


if __name__ == "__main__":
    main()

