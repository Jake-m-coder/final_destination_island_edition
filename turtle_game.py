from turtle import Turtle, Screen


def etch_e_sketch():
    """ The purpose of this function is to return a simple etch-e-sketch game for fun. The controls are listed below.
    controls:
    w or up arrow key to move forward,
    s or down arrow key to move backwards,
    a or left arrow key to move counter-clockwise,
    d or right arrow key to move clockwise,
    and c to clear the screen."""
    tim = Turtle()
    screen = Screen()
    screen.title("Etch-E-Sketch")
    screen.setup(width=400, height=400)

    def move_forward():
        tim.forward(10)

    def move_backward():
        tim.backward(10)

    def move_clockwise():
        tim.right(45)

    def move_counterclockwise():
        tim.left(45)

    def clear():
        tim.reset()

    screen.listen()
    screen.onkey(key="w", fun=move_forward)
    screen.onkey(move_forward, "Up")
    screen.onkey(key="s", fun=move_backward)
    screen.onkey(move_backward, "Down")
    screen.onkey(key="a", fun=move_counterclockwise)
    screen.onkey(move_counterclockwise, "Left")
    screen.onkey(key="d", fun=move_clockwise)
    screen.onkey(move_clockwise, "Right")
    screen.onkey(key="c", fun=clear)
    screen.exitonclick()

