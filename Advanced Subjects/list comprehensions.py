#list, set , dict
simple_dict = {
    'a' : 1,
    'b' : 2
}
my_dict = {key : value **2 for key, value in simple_dict.items() if value %2 == 0}

my_dict2 = {key : key * 2 for key in [1,2,3]} #THAT MAKE SIT SO THE ITEM IS THE KEY AND IT MULTIPLIED BY 2 IS THE VALUE

print(my_dict)



my_list = [char for char in 'hello']       
my_list2 = [num*2 for num in range(10)]

my_list4 = [num**2 for num in range(10) if num % 2 == 0] #TAKES VALUE, EXPONANT 2, ITERATES THROUGH RANGE, THEN IF ITS AN EVEN NUMBER, ITS ADDED TO VAR

for char in 'hello':
    my_list.append(char)

print(my_list2)