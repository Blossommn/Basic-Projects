###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
# import colorgram

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.r
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import turtle as t
import random
tim = t.Turtle()

tim.speed("fastest")
t.colormode(255)

color_list = [(245, 245, 238), (246, 246, 244), (202, 202, 110), (240, 240, 241), (236, 236, 243), (149, 149, 50), (222, 222, 136), (53, 53, 123), (170, 170, 41), (138, 138, 20), (134, 134, 184), (197, 197, 73), (47, 47, 86), (73, 73, 35), (145, 145, 149), (14, 14, 70), (232, 232, 165), (160, 160, 158), (54, 54, 50), (101, 101, 77), (183, 183, 171), (36, 36, 74), (19, 19, 89), (82, 82, 129), (147, 147, 19), (27, 27, 102), (12, 12, 64), (107, 107, 153), (176, 176, 208), (168, 168, 102)]

tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.fd(300)
tim.setheading(0)
num_of_dots = 100

for dot_count in range(1, num_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.fd(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.fd(50)
        tim.setheading(180)
        tim.fd(500)
        tim.setheading(0)


screen = t.Screen()
screen.exitonclick()