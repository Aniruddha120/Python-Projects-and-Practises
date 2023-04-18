class Vehicle():
    def __init__(self, quantity :float , value : float, name : str ):
        assert quantity>= 0 ,f'The quantity {quantity} is not greater then 0'
    
        assert value>= 0 ,f'The value {value} is not greater then 0'
        self.q = quantity
        self.a = value
        self.n = name
    def calculate(self):
        return print(self.q*self.a)
item1 = Vehicle(10, 1000, 'car')
item1.calculate()
        