def val_checker(checker_func):
    def Val_checker(func):
        def wrapper(x):
            if checker_func(x):
                return func(x)
            else:
                raise ValueError(x)
        return wrapper
    return Val_checker

@val_checker(lambda x: x > 0)
def calc_cube(args):
    return args ** 3

print(calc_cube(5))
print(calc_cube(-5))
