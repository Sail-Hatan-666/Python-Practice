from turtle import Turtle, Screen

timmy = Turtle()

print(timmy)
timmy.shape("turtle")
timmy.color("DarkSlateGray1")
timmy.forward(100)
timmy.left(100)
timmy.fd(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()