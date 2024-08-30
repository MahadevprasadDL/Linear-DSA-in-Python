class stack:
    def __init__(self):
        self.values=[]
    def push (self , x):
        self.values = [x]+self.values
    def pop (self):
        return self.values.pop(0) 

s=stack()
s.push(100)
s.push(200)
s.push(300)
s.push(400)
print(s. values)       
