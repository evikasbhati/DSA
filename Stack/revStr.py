class Stack:
    def __init__(self):
        self.array=[]
        self.size=0
    
    def view(self):
        for i in self.arr:
            print(i)

    def push(self,element):
        self.array.append(element)
        self.size+=1

    def pop(self):
        rem=self.array.pop()
        return rem
        self.size-=1

lstr="something"
obj=Stack()
for i in lstr:
    obj.push(i)
    
rstr=""
for i in range(len(lstr)):
    rstr+=obj.pop()
    print(i)

print(rstr)
