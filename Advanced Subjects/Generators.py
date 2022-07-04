def generator_function(num):
    for i in range(num):
        yield i * 2  #yield pauses the function, takes less space than creating a list, we itterate through each value once so we only keep on in memory

g = generator_function(100)

next(g) #next resumes the function

print(next(g))
