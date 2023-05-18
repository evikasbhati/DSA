
class Node:
    def __init__(self, value):
        self.value =value
        self.left = None
        self.right = None

def CreateTree(arr,index):
    if index>=len(arr):
        return

    value=arr[index];
    root=Node(value);

    root.left=CreateTree(arr, 2*index+1)
    root.right=CreateTree(arr, 2*index+2)
    return root

def maxValue(arg1,arg2):
    print(arg1,arg2)
    return arg1 if arg1>arg2 else arg2;

def height(root):
    if root==None:
        return 0
    left=height(root.left)
    right=height(root.right)
    ht=maxValue(left,right)+1
    return ht

# Input
# 25 15 50 10 22 35 70 4 12 18 24 31 44 66 90

d=(input().split(" "))
data=[]
for i in d:
    data.append(int(i));
root= CreateTree(data,0)
ht=height(root)  
print("height of tree is:",ht) 

# With Test cases   
# tc=int(input())
# for i in range(tc):
#     # n=int(input()) # number of values
#     d=(input().split(" "))
#     data=[]
#     for i in d:
#         data.append(int(i));
#     root= CreateTree(data,0)
