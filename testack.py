class Stack:
    def __init__(self):
        self.array=[]
        self.size=0

    def view(self):
        for i in range(self.size):
            print(self.array[i])

    def push(self,element):
        self.array.append(element)
        self.size+=1
 
    def pop(self):
        rem=self.array.pop()
        self.size-=1
        return rem

    

obj=Stack()
obj.push(5)
obj.push(58)
obj.push(52)
obj.push(15)
obj.push(55)
obj.push(51)
stm=[]
while obj.size/2:
   stm.append(obj.pop())

print(obj.size)
# obj.view()
