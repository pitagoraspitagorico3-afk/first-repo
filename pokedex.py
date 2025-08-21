class Pokemon:
    def __init__(self, number, name, type):
        self.name = name
        self.number = number
        self.type = type
    def __str__(self):
        return f'\n number: {self.number} \n name: {self.name} \n type: {self.type}'

bulbasaur= Pokemon('0001', 'Bulbasaur', 'grass')
ivysaur= Pokemon('0002', 'Ivysaur', 'grass/poison')

print(bulbasaur)
print(ivysaur)

