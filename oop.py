class fruits:
    def __init__(self, type, price, color):
        self.type = type
        self.price = price
        self.color = color
    def onyesha(self):
        print(f"I like eating {self.type} and it costs {self.price}, its color is {self.color} ")
myobj=fruits("Banana","20 Kshs","Yellow")
myobj2=fruits("Mango","30 Ksh","Red")

myobj.onyesha()
myobj2.onyesha()