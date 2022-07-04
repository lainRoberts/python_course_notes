#*args **kwargs

def super_func(name="lol", *args, i="hi", **kwargs):
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total

print(super_func(1,2,3,4,5, yo=137))


#PUT ARGS N STUFF IN THIS ORDER
# params, *args, default parameters, **kwargs