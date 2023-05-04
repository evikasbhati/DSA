class Node:
    def __init__(self,data):
        self.data=data;
        self.next=None;

class Linked_List:
    count=0
    def __init__(self):
        self.start=None

    def viewList(self):
        if self.start is None:
            print("list is empty")
        else:
            temp=self.start
            while temp is not None:
             print(temp.data, end=" -> ")
             temp=temp.next
        print(f"\n Number of nodes are: {Linked_List.count}")

    def insertEnd(self,value):
        newNode=Node(value);
        if self.start==None:
            self.start=newNode;
        else:
             temp=self.start;
             while temp.next:
                 temp=temp.next;
             temp.next=newNode
        Linked_List.count+=1

    def insertStart(self,value):
        newNode=Node(value);
        if self.start==None:
            self.start=newNode
        else:
            newNode.next=self.start
            self.start=newNode
        Linked_List.count+=1

    def insert_at_Position(self,value,postion):
        if postion==1:
            Linked_List.insertStart(self, value)
        elif postion>Linked_List.count:
            Linked_List.insertEnd(self, value)
        else:
            newNode=Node(value)
            if self.start is None:
                self.start=newNode
            else:
                index=1
                temp=self.start
                while index<postion-1:
                    temp=temp.next
                    index+=1
                newNode.next=temp.next
                temp.next=newNode
            Linked_List.count+=1

    def deleteStart(self):
        self.start=self.start.next
        Linked_List.count-=1

    def deleteEnd(self):
        temp=self.start
        for i in range(1,Linked_List.count-1):
            temp=temp.next
        temp.next=None
        Linked_List.count-=1

    def delete_at_postion(self,position):
        if position==1:
            Linked_List.deleteStart(self)
            print("first")
        elif position>=Linked_List.count:
            Linked_List.deleteEnd(self)
            print("last")
        else:
            print("postion")
            temp=self.start
            for i in range(1,position-1):
                temp=temp.next
            temp.next=temp.next.next
            Linked_List.count-=1


ll1=Linked_List()
ll1.insertEnd(25)
ll1.insertEnd(5)
ll1.insertEnd(15)
ll1.insertEnd(35)
ll1.insertStart(36)
ll1.insertEnd(45)
ll1.insertStart(50)
ll1.insert_at_Position(111,20)
ll1.viewList()
ll1.delete_at_postion(7)
ll1.viewList()
# ll1.insertEnd(15)
# ll1.insertEnd(2)

