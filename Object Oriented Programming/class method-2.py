class Vehicle(): #name of the class
    pay_rate = 0.8 #class attribute, the variables that belongs to class
    all = []
    def __init__(self, quantity :float , value : float, name : str ): #method, __init__ special method
        
        assert quantity>= 0 ,f'The quantity {quantity} is not greater then 0'
    
        assert value>= 0 ,f'The value {value} is not greater then 0'
        self.q = quantity #self.q is instance variable, quantuty = attribute
        self.a = value
        self.n = name
        Vehicle.all.append(self)
    def calculate(self):
        return print(self.q*self.a*self.pay_rate)
item1 = Vehicle(10, 1000, 'car') #instance of a class , known as an 'Object'
item2 = Vehicle(20, 500, 'bike')
item1.calculate()
print(Vehicle.all)
for inst in Vehicle.all:
    print(inst.n)
'''for inst in Vehicle.all:
    print(self(self.n,self.q, self.a))'''
random = str('4')