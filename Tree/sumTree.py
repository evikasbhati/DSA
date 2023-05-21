
class Node:
    def __init__(self,value):
        self.value=value;
        self.left=None;
        self.right=None;

def CreateTree(arr,index):

    if index>=len(arr):
        return;

    data=arr[index];
    root=Node(data);

    root.left=CreateTree(arr,2*index+1);
    root.right=CreateTree(arr, 2*index+2);

    return root;

def preOrder(root):
    if root==None:
        return;
    print(root.value);
    preOrder(root.left);
    preOrder(root.right);

# input
# 25 15 50 10 22 35 70 4 12 18 24 31 44 66 90

tree=CreateTree(arr, index)