import turtle

def spiral(initial_length, angle, multiplier):
    if (initial_length < 1 or initial_length > 200):
        return
    turtle.left(angle)
    turtle.fd(initial_length)
    spiral(initial_length*multiplier, angle, multiplier)

#spiral(100, 90, 0.9)
spiral(1, -45, 1.1)

turtle.done()