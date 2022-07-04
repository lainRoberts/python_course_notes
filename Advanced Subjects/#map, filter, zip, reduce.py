#map, filter, zip, reduce

from functools import reduce

my_list = [1,2,3]
your_list = [10, 20, 30]
their_list = (5,4,3)

def multiply_by2(item):
    return item*2

def only_off(item):
    item % 2 !=0

def accumulator(acc, item):
    print(acc, item)
    return acc + item



print(list(filter(only_off, my_list))) #FILTER ONLY GETS WHAT IS RETURNED FROM FUNCTION
print (list(zip(my_list,your_list, their_list))) # ZIP LIST CREATES A LIST WITH TUPLES OF EACH ITERABLE'S VALUES

print(list(map(multiply_by2, my_list))) #MAP IS USEEFUL ANYTIME WE HAVE SOMETHING TO ITTERATE THROUGH

print((reduce(accumulator,my_list, 0))) 


print(my_list) #PURE FUNCTIONS DONT AFFECT ANYTHING OUTSIDE THEM, THUS my_list REMAINS THE SAME

# reduce() = apply a function to an iterable and reduce it to a single cumulative value.
#            performs function on first two elements and repeats process until 1 value remains
#
# reduce(function, iterable)

import functools

letters = ["H","E","L","L","O"]
word = functools.reduce(lambda x, y,:x + y,letters)
print(word)

# factorial = [5,4,3,2,1]
# result = functools.reduce(lambda x, y,:x * y,factorial)
# print(result)