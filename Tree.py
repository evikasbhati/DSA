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

def LevelOrderTraversel(root):
    if root==None :
        return;

    q=deque();
    q.append(root)   
    
    while len(q)>0:
        temp=q.pop();
        print(temp.value, end=" ");

        if temp.left is not None:
            q.append(temp.left)
        if temp.right is not None:
            q.append(temp.right)

root=CreateTree();
# 25 12 6 3 -1 -1 55 -1 -1  33 -1 -1 -1
LevelOrderTraversel(root)
# Inorder(root)
# print("\n")
# PreOrder(root)
# print("\n")
# PostOrder(root)


 # if root==None:
    #     return ;
    # else:
    #     print(root.value);
    #     if root.left or root.right:
    #         print(end="\n")
    #     if root.left:
    #         print(root.left.value,end=" ")
    #     if root.right:
    #         print(root.right.value)
    #     if root.left.left!=None:
    #         LevelOrderTraversel(root.left.left)
    #     if root.right.right!=None:
    #         LevelOrderTraversel(root.right.right)
