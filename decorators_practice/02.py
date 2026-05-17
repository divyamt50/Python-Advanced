import time


def caching(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

@caching
def sum(num1, num2):
    time.sleep(4)
    return num1 + num2

print(sum(1,1))
print(sum(2,2))
print(sum(1,1))
print(sum(1,4))
print(sum(2,2))