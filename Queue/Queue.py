class Queue:
    def __init__(self):
        self.que=[]

    def view(self):
        for i in range(len(self.que)):
            print(self.que[i],end=" ")

    def size(self):
        print(len(self.que))

    def isEmpty(self):
        print(self.que==[])  

    def inqueue(self,element):
        self.que.append(element)

    def dequeue(self):
        if self.que==[]:
            print("can't remove element Queue is empty")
        else:
            self.que.pop(0)


q=Queue()
q.inqueue(5)
q.inqueue(15)
q.inqueue(25)
q.inqueue(35)
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.size()
q.isEmpty()
q.view()
