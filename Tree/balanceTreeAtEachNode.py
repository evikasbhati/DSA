
def maxValue(arg1,arg2):
    return arg1 if arg1>arg2 else arg2;

class Solution:

    def balanceCheck(self,root):
        self.isBalanced=False;

        def height(root):
            if root is None:
                return 0;
            left=height(root.left)
            right=height(root.right)
            ht=maxValue(left, right)+1
            self.isBalanced=abs(left-right)<=1

            return ht
        height(root)
        return self.isBalanced

class Node:
    def __init__(self,value):
        self.value=value;
        self.left=None;
        self.right=None;

# def CreateTree(arr,index):
#     if index>=len(arr):
#         return;

#     data=arr[index];
#     root=Node(data)
#     root.left=CreateTree(arr, 2* index+1)
#     root.right=CreateTree(arr, 2* index+2)

#     return root

# input
# 25 15 50 10 22 35 70 4 12 18 24 31 44 66 90

ar=[25,15,50,10,22,35,70,4,12,18,24,31,44,66,90]

#Tree creation one node at a time
def CreateTree(root=None):
    data=int(input("Enter data\n"));
    if data==-1 :
        return ;
    else:
        root=Node(data)
        print(f"enter data for left of {root.value}")
        root.left=CreateTree(root.left)
        print(f"enter data for right of {root.value}")
        root.right=CreateTree(root.right)

        return root


# root=CreateTree(ar, 0)
root=CreateTree()
sol=Solution()
bal=sol.balanceCheck(root)
print(bal)
