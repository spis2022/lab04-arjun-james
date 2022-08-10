import turtle

turtle.left(90)

def tree(trunk_length, height):
    if (height == 0):
        turtle.fd(trunk_length)
        turtle.fd(-trunk_length)
        return
    turtle.fd(trunk_length)
    turtle.left(45)
    tree(trunk_length/2, height - 1)
    turtle.left(-90)
    tree(trunk_length/2, height - 1)
    turtle.left(45)
    turtle.fd(-trunk_length)

tree(100, 5)

turtle.done()