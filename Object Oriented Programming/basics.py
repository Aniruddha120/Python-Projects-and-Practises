class canine(self, tail, color):
    self.t = tail
    self.c = color
    print("I am canine")
class dog(canine):
    print("I am dog from canine")
    print(self.t)

a = dog()


    