
amazon_cart = [
    'notebooks', 
    'sunglasses'
    'toys',
    'grapes'
    ]

amazon_cart[0] = 'laptop'
print(amazon_cart[0::2])

new_cart = amazon_cart[:] # <----- TAKES THE VALUE FROM INSIDE VARIABLE AND COPIES IT OVER IN NEW_CART
new_cart = amazon_cart    # <----- INSTEAD, THIS JUST POINTS TO THE EMPLACEMENT OF AMAZON_CART AND MODIFICATIONS TO NEW_CART WILL ALSO AFFECT AMAZON_CART
new_cart[0] = 'gum'

print(amazon_cart)

print(new_cart)