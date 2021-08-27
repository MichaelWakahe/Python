def square(num):
    return num * num


square_lambda = lambda num: num * num

assert square(4) == square_lambda(4)

# velocity calculator (physics): v=u+at
velocity = lambda u, a, t: u + a * t

assert velocity(3, 2, 10) == 23
