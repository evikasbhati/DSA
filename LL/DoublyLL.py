class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None

class DLL:
    count=0
    def __init__(self):
        self.start=None

    def viewList(self):
        if self.start==None:
            print("List is empty")
        else:
            temp=self.start
            while temp:
                print(temp.data,end=" -> ")
                temp=temp.next
        print(f"\nNo. of Nodes are: {self.count}")

    def ins_End(self,value):
        newNode=Node(value)
        if self.start==None:
            self.start=newNode
        else:
            temp=self.start
            while temp.next:
                temp=temp.next
            temp.next=newNode
            temp.next.prev=temp
        DLL.count+=1

    def ins_Start(self,value):
        newNode=Node(value)
        if self.start==None:
            self.start=newNode
        else:
            self.start.prev=newNode
            newNode.next=self.start
            self.start=newNode
        DLL.count+=1

    def insert_at_Position(self,value,position):
        newNode=Node(value);
        if position==1:
            self.ins_Start(value)
        elif position>=DLL.count:
            self.ins_End(value)
        else:
            temp=self.start
            for i in range(1,position-1):
                temp=temp.next
            newNode.next=temp.next
            temp.next=newNode
            newNode.next.prev=newNode
        self.count+=1

    def delete_start(self):
        self.start=self.start.next
        self.count-=1

    def delete_end(self):
        temp=self.start
        while temp.next:
            temp=temp.next
        temp.prev.next=None
        self.count-=1

    def delete_at_postion(self,position):
        if position==1:
            self.delete_start()
        elif position>=self.count:
            self.delete_end()
        else:
            temp=self.start
            for i in range(1,position-1):
                temp=temp.next
        temp.next.next.prev=temp.prev
        temp.next=temp.next.next
        self.count-=1    

ll=DLL()
ll.ins_End(5)
ll.ins_End(15)
ll.ins_End(25)
ll.ins_End(35)
ll.ins_End(45)
ll.ins_Start(111)
ll.ins_Start(511)
ll.insert_at_Position(20,1)
ll.insert_at_Position(120,5)
ll.delete_at_postion(5)
ll.viewList()
        