def typy_logger(func):
    def wrapper(*args):
        for arg in args:
            print(f'{func.__name__}({arg}:{type(arg)})')
            func(arg)

    return wrapper

@typy_logger
def calc_cube(*args):
        for arg in args:
            out = arg ** 3
            print(out)


calc_cube(5, 4)