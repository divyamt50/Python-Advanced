#iterators and iterables and generators
#first what are iterables, a list is an example of iterable

nums = [1,2,3,4,5]
#just like this a string, tuple, set is also an iterable
#now lets understand what are iterators
#simple example
# for num in nums:
#     print(num)
#num here is an iterator
#but there is more to this


num = nums.__iter__()
print(num.__next__)
print(num.__next__)

num = iter(nums)
print("num is ", num)
print(num.__next__())
print(num.__next__())

#we can also write it like this
i_num = iter(nums)
print(next(i_num))
print(next(i_num))

# making our own iterable and iterator
class MyRange:
    def __init__(self,start,end):
        self.value = start
        self.end = end
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current

lt = MyRange(5,10)
print(next(lt))
print(next(lt))

# now generators can make this all very easy

def gen_example(start, end):
    current = start
    while current < end:
        yield current
        current += 1

new_nums = gen_example(50,55)

print("\n")
for num in new_nums:
    print(num)

print("\n")
new_nums = gen_example(50,55)


print(next(new_nums))
print(next(new_nums))