class User():
    def __init__(self, email):
        self.email = email


class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(email)                   #SUPER CALLS ON THE CLASS ABOVE THE ONE WE CURRENTLY, THIS WAY WE CAN ADD THE EMAIL FUNCTION
        self.name = name
        self.power = power
    def attack(self):
        print(f'Volley of arrows falls down upon the enemy, dealing {self.power}')
     
class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows
    
    def attack(self):
        print(f'Volley of arrows falls down upon the enemy, dealing {self.num_arrows}')

wizard1 = Wizard('Merlin', 50, 'merlin@magicmail.com')
archer1 = Archer('Robin', 100)


#INTROSPECTION
print(dir(wizard1))