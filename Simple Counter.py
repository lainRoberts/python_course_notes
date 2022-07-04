#counter
my_list = [100,2,3,4,5,6,7,8,9,10]
tricky_counter = 0

for item in my_list:
    tricky_counter += item
    print(item)
print(f'Sum of values in list is : {tricky_counter}')