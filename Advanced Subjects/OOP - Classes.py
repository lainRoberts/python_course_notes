#OOP
class PlayerCharacter:
    membership = True #<-This is a Class Object Attribute, it applies to whole class
    def __init__(self, name, age=57):
        if (self.membership):
            self.name = name                     #SELF REFERS THE THE INSTANCE OF THE CLASSE THAT WAS CALLED, FOR EXAMPLE PLAYER1, OR PLAYER2, ETC...
            self.age = age
        
    def run (self):
        print('run')
        self.membership = False #THIS DOES NOTHING SINCE MEMBERSHIP IS ALREADY CALLED AS CLASS OBJECT ATTRIBUTE
        return('done')

player1 = PlayerCharacter('Cindy')
player2 = PlayerCharacter('Tom')

print(player1.age)
print(player1.run)
print(player1.membership)

