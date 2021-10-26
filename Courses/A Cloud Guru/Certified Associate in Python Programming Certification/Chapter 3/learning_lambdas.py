def square(num):
    return num * num


square_lambda = lambda num: num * num

# According to Pep 8: E731, the above should be:
# def square_lambda(num): return num * num

assert square(4) == square_lambda(4)

# velocity calculator (physics): v=u+at
velocity = lambda u, a, t: u + a * t

assert velocity(3, 2, 10) == 23
