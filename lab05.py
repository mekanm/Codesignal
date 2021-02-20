import turtle, random, math

# spiro problem

turtle.speed(1)
turtle.delay(0)

turtle.showturtle()

def filled_square(side):
    r = random.random()
    g = random.random()
    b = random.random()
    turtle.color(r,g,b)
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(side)
        turtle.left(90)
    turtle.end_fill()

def spiro(num, side):
    angle = 360 / num
    for i in range(num):
        filled_square(side)
        turtle.left(angle)

spiro(9, 50)





# challenge problem

n = 0

turtle.hideturtle()
turtle.speed(0)
turtle.delay(0)
turtle.penup()

amt_inside = 0
darts_thrown = 0

def in_circle(x_cor, y_cor):
    col = ''
    d = math.sqrt(math.pow(x_cor, 2) + math.pow(y_cor, 2))

    if d <= 1:
        col = 'green'
    elif d > 1:
        col = 'red'

    return col


while n < 5000:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    col = in_circle(x, y)
    darts_thrown += 1

    if col == 'green':
        amt_inside += 1

    turtle.setpos((x * 150), (y * 150))
    turtle.pendown()

    turtle.dot(5, col)
    turtle.penup()

    n += 1

prob = amt_inside / darts_thrown

est_val = prob * 4

print(est_val)


# route problem part one

turtle.speed(0)
turtle.delay(0)

n = 0
while n < 200:
    heading = random.randint(1, 4)

    if heading == 1:
        turtle.setheading(0)
    elif heading == 2:
        turtle.setheading(90)
    elif heading == 3:
        turtle.setheading(180)
    elif heading == 4:
        turtle.setheading(270)

    turtle.forward(20)

    n += 1


# route problem part two

turtle.speed(0)
turtle.delay(0)

n = 0
while n != -1:
    heading = random.randint(1, 4)

    if heading == 1:
        turtle.setheading(0)
    elif heading == 2:
        turtle.setheading(90)
    elif heading == 3:
        turtle.setheading(180)
    elif heading == 4:
        turtle.setheading(270)

    turtle.forward(20)

    if (turtle.xcor()) < -250 or (turtle.xcor()) > 250:
        turtle.write(n, font=("Arial", 20, "normal"))
        n = -1
    elif (turtle.ycor()) < -220 or (turtle.ycor()) > 220:
        turtle.write(n, font=("Arial", 20, "normal"))
        n = -1
    else:
        n += 1

