#bruh
basket = ["Banana", 
["Apples", 
["Oranges"],
 "Blueberries"]]

print(basket[1][1])
print(basket[1][1][0])

bob = [1,2,3,4,5]

#adding
bob.append(100)
new_list = bob[:]
print(new_list)

#insert
bob.insert(4, 137)
print(bob)

#extend
basket.extend(["lol"])
print(basket)

#poping and removing
basket.pop() #TO REMOVE LAST INDEX
print(basket)

basket.pop(0) #TO REMOVE INDICATED INDEX
print(basket)

print(basket)
basket[0].remove("Apples") #TO REMOVE A SPECIFIC VALUE
print(basket)

#clearing
basket.clear()
print(f'Basket content : {basket}')