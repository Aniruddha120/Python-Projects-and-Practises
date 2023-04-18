class Vehicle():
    pay_rate = 0.8
    all = []
    def __init__(self, quantity :float , value : float, name : str ):
        
        assert quantity>= 0 ,f'The quantity {quantity} is not greater then 0'
    
        assert value>= 0 ,f'The value {value} is not greater then 0'
        self.q = quantity
        self.a = value
        self.n = name
        Vehicle.all.append(self)
    def calculate(self):
        return print(self.q*self.a*self.pay_rate)
item1 = Vehicle(10, 1000, 'car')
item2 = Vehicle(20, 500, 'bike')
item1.calculate()