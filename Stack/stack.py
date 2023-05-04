class Stack:
    def __init__(self):
        self.arr=[];
        self.size=0;

    def view(self):
        for i in self.arr:
            print(i)

    def push(self,element):
        self.arr.append(element)
        self.size+=1

    def pop(self):
        rem=self.arr.pop()
        return rem
        self.size-=1
    
    def isEmpty(self):
        return self.size==0

    def peek(self):
        return self.arr[-1]
        

obj=Stack()
obj.push(5)
obj.push(15)
obj.push(25)
ll=obj.pop()
obj.push(35)
obj.view()
print(ll)