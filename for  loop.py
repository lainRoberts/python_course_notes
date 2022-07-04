for variable_name in (1,2,3,4,5):
    for x in ['a', 'b', 'c']:
        print(variable_name, x)

for number in range(1,11):
    print(number)

for _ in range(10, 1, -2): #for when you just want to itterate through something, you can name var _ to indicate u dont care, 10, 1, -2 if you want to step back 2 from 10 
    print(list(range(10)))