from collections import deque
class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

def CreateTree(root=None):

    data=int(input("Enter data\n"));
    if data==-1 :
        return None ;
    else:
        root=Node(data)
        print(f"enter data for left of {root.value}")
        root.left=CreateTree(root.left)
        print(f"enter data for right of {root.value}")
        root.right=CreateTree(root.right)

        return root


def Inorder(root):
    # LNR
    if root==None :
        return;
    else:
        Inorder(root.left)
        print(root.value, end=" ")
        Inorder(root.right)

def PreOrder(root):
    # NLR
    if root==None:
        return ;
    else:
        print(root.value, end=" ")
        PreOrder(root.left,)
        PreOrder(root.right)

def PostOrder(root):
    # LRN 
    if root==None:
        return;
    else:
        PostOrder(root.left);
        PostOrder(root.right);
        print(root.value,end=" ");
        
# LOT is also known as BFS (Breadth First Search)
def LevelOrderTraversel(root):
    if root==None :
        return;

    q=[];
    q.append(root)   
    
    while len(q)>0:
        print(q[0].value,end=" ");
        temp=q.pop(0);

        if temp.left is not None:
            q.append(temp.left)
        if temp.right is not None:
            q.append(temp.right)

root=CreateTree();

# Input
# 25 12 6 3 -1 -1 55 -1 -1  33 -1 -1 -1

# print("Inorder \n")
# Inorder(root)
# print("\n")
# print("Preorder \n")
# PreOrder(root)
# print("\n")
# print("PostOrder \n")
# PostOrder(root)
# print("\n")
# print("LevelOrder \n")
LevelOrderTraversel(root)

