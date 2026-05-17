# Python Advanced Concepts

A quick reference guide for important Python concepts.

---

## 1. Iterators

An **iterator** is an object that can be iterated one value at a time using `next()`.

### Example

```python
nums = [1, 2, 3]

iterator = iter(nums)

print(next(iterator))  # 1
print(next(iterator))  # 2
```

### Key Points

- Uses `__iter__()` and `__next__()`
- Saves memory
- Used internally in loops

---

## 2. Generators

Generators are a simpler way to create iterators using `yield`.

### Example

```python
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

for num in count_up_to(3):
    print(num)
```

### Why Use Generators?

- Memory efficient
- Lazy evaluation
- Great for large datasets

---

## 3. Decorators

Decorators modify the behavior of functions without changing their code.

### Example

```python
def logger(func):
    def wrapper():
        print("Function started")
        func()
        print("Function ended")
    return wrapper

@logger
def greet():
    print("Hello!")

greet()
```

### Common Use Cases

- Logging
- Authentication
- Performance timing
- Caching

---

## 4. Async IO

Async IO enables concurrent execution using `async` and `await`.

### Example

```python
import asyncio

async def say_hello():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

asyncio.run(say_hello())
```

### Benefits

- Non-blocking operations
- Faster network/file handling
- Useful for APIs and web scraping

---

## Summary

| Concept | Purpose |
|---|---|
| Iterators | Sequential access to data |
| Generators | Lazy iterator creation |
| Decorators | Modify function behavior |
| Async IO | Concurrent asynchronous tasks |

---

## Resources

- Python Official Docs
- asyncio Documentation
- Real Python Tutorials
```
