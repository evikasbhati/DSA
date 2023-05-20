
class Node:

    def __init__ (self,value):
        self.value=value;
        self.left=None;
        self.right=None;

# def CreateTree(root=None):
#     data=int(input("Enter data\n"));

#     if data==-1:
#         return;
    
#     root=Node(data);
#     print(f"Enter data to left of {root.value}");
#     root.left=CreateTree(root.left)
#     print(f"Enter data to right of {root.value}");
#     root.right=CreateTree(root.right)

#     return root

def CreateTree(arr,index):
    if index>=len(arr):
        return

    data=arr[index];
    root=Node(data)
    root.left=CreateTree(arr, 2*index+1)
    root.right=CreateTree(arr, 2*index+2)
    return root

def post(root):
    if root==None:
        return;
    post(root.left)
    post(root.right)
    print(root.value,end=" ")

class Solution:

    def isIdentical(self,root1,root2):
        self.isId=True

        def inOrder(root1,root2):
            if root1==None and root2==None:
                return
            if root1 is None and root2 is not None or root1 is not None and root2 is None:
                self.isId=False;
                return
            if root1.value!=root2.value:
                self.isId=False;
                return
            
            inOrder(root1.left, root2.left)
            inOrder(root1.right, root2.right)
        
        inOrder(root1, root2)
        return self.isId

# input
# 25 15 50 10 22 35 70 4 12 18 24 31 44 66 90

ar1=[25,15,50,10,22,35,70,4,12,18,24,31,44,66,90]
ar2=[25,15,50,10,22,35,70,4,12,18,24,31,44,66,90]

tree1=CreateTree(ar1,0);
print("New tree");
tree2=CreateTree(ar2,0)
# post(tree)
sol=Solution()
output=sol.isIdentical(tree1, tree2)
print(output)