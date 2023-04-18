class Item():
    def __init__(self, name ,value,color):
        self.n = name
        self.v = value
        self.c = color
        
    
        print(f"I am created {name}, price {value}, {color}")

item1 =Item('android', 2000, 'black')
item1.n = 'hello'
item1.charger = 'black'
#item1.name = 'vodaphone'
item2 = Item('iphone', '2k', 'red')
#item3 = Item(name, value, color)

'''item1 = Item()
item1.name = "Phone"
item1.value = '2k
item1.

item2
print(item1.name)

item2.name'''
print(item1.n)
item1.c = 'yellow'
