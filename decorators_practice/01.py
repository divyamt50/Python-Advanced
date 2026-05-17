def outer(func):
    def wrapper(*args, **kwargs):
        args_val = ', '.join(str(arg) for arg in args)
        kwargs_val = ', '.join(f"{k}={v}" for k,v in kwargs.items())
        print(f"function name {func.__name__}")
        print(f"args = {args_val}")
        print(f"kwargs = {kwargs_val}")
        return func(*args, **kwargs)
    return wrapper


@outer
def sum(num1, num2):
    return num1 + num2


@outer
def greet(wish, name="Lance"):
    print(f"{wish} {name}")

sum(10,20)
greet("hi",name="Kyle")