# from collections import deque

# Tree created in levelOrder using Array as input
class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

def CreateTree(arr,index):
    if index>=len(arr):
        return
    
    data=arr[index];
    root=Node(data);

    root.left=CreateTree(arr,(index*2)+1)
    root.right=CreateTree(arr,(index*2) +2)

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
            
d=(input().split(" "))
data=[]
for i in d:
    data.append(int(i));
    
root= CreateTree(data,0)

# Input
# 25 15 50 10 22 35 70 4 12 18 24 31 44 66 90

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

