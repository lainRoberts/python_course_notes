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


print(list(map(lambda item: item * 2, my_list))) #lambda var_name: return this action, on this item

print(reduce(lambda acc, item: acc + item, my_list)) #reduce with lambda

