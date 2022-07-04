class User():
    def sign_in(self):
        print('Logged in.')

class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'Freezing water falls from the sky, dealing {self.power}')
     
class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows
    
    def check_arrows(self):
        print(f'Volley of arrows falls down upon the enemy, dealing {self.num_arrows}')

    def run(self):
        print('ran really fast')


class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, num_arrows):
        Archer.__init__(self, name, num_arrows)
        Wizard.__init__(self, name, power)


hybrid_borg = HybridBorg('Borrgie', 50, 100)

print(hybrid_borg.sign_in())

print(hybrid_borg.attack())