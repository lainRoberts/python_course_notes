class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('run')

    def speak(self):
        print(f'My name is {self.name}, I am {self.age} years old')

player1 = PlayerCharacter('Matrakus', 137)
player1.speak()