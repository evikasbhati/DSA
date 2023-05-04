class twoStack:
    def __init__(self,size):
        self.array=[None for i in range(size)]
        self.size=size
        self.first=-1
        self.last=size

    def view(self):
        for i in range(self.size):
            if self.array[i]!=None:
                print(self.array[i])

    def push1(self,value):
        if self.last-self.first>1:
            self.first+=1
            self.array.insert(self.first,value)
        # raise OverflowError("can't insert more values")
    
    def push2(self,value):
        # print(self.first,"-",self.last,": ",self.last-self.first)
        if self.last-self.first>1:
            self.last-=1
            self.array[self.last]=value
        # raise OverflowError("can't insert more values")
    def pop1(self):
        if self.first>=0:
            rem= self.array[self.first]
            self.array[self.first]=None
            self.first-=1
            return rem
        else:
            print("no1")
        
    def pop2(self):
        if self.last<self.size:
            rem= self.array[self.last]
            self.array[self.last]=None
            self.last+=1
            return rem
        else:
            print("no2")

obj=twoStack(10)
obj.push1(5)
obj.push1(6)
obj.push1(8)
obj.push1(15)
obj.push1(25)
obj.push2(88)
obj.push2(68)
obj.push2(85)
obj.push2(98)
obj.push2(257)
obj.view()
print("pop1",obj.pop1())
print("pop2",obj.pop2())
print("pop1",obj.pop1())
print("pop2",obj.pop2())
print("pop1",obj.pop1())
print("pop2",obj.pop2())
print("pop1",obj.pop1())
print("pop2",obj.pop2())
print("pop1",obj.pop1())
print("pop2",obj.pop2())
print("pop1",obj.pop1())
print("pop2",obj.pop2())
obj.view()