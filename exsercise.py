def decorator_func(function):
    def wrapper_function(*args, **kwargs):
        print(f"You called {function.__name__}({args})")
        result = function(args[0], args[1])
        print(f"It returned: {result}")

    return wrapper_function


@decorator_func
def sum_num(a, b):
     return a + b


sum_num(1, 2)
