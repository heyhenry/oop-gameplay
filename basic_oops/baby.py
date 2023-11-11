# simple object creation

class Baby:

    # class attributes/variables
    action_1 = 'roll over'
    action_2 = 'crawl'

    # instance of attributes/variables
    def __init__(self, name):
        self.name = name

    def first_step(self):
        print('Baby ' + self.name + ' has just performed the skill: ' + self.action_1)

    def second_step(self):
        print('Baby ' + self.name + ' has just performed the skill: ' + self.action_2)
    
Ariel = Baby('Ariel')
Paing = Baby('Paing')

Ariel.first_step()
Paing.second_step()
