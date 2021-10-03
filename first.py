# Make A Class of cricketers and to count there scores as they hit a six or 4 only;
class India():
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def __add__(self, other):
        x = self.first + other.first
        y = self.second + other.second
        z = India(x, y)
        print(z)
    def th(self):
        print((self.first + self.second)//2)
    def single(self, singles):
        a = self.first + self.second + singles
        print(a)

obj1 = India(20 , 40)
obj2 = India(20, 40)
obj1.th()
obj1.single(16)
(obj1 + obj2)