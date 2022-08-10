import turtle

def snowflake_side(side_length, levels):
    if (levels == 0):
        turtle.fd(side_length)
        return
    snowflake_side(side_length/3, levels - 1)
    turtle.left(60)
    snowflake_side(side_length/3, levels - 1)
    turtle.left(-120)
    snowflake_side(side_length/3, levels - 1)
    turtle.left(60)
    snowflake_side(side_length/3, levels - 1)

    

def snowflake(side_length, levels):
    for i in range(3):
        snowflake_side(side_length, levels)
        turtle.left(-120)

snowflake(140, 4)

turtle.done()