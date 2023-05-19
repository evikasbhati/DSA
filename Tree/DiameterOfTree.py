#  Diameter/width of tree longest path b/w any two nodes

class Node:
    def __init__(self,value):
        self.value=value;
        self.left=None;
        self.right=None;

# Tree created using LevelOrder with array as input
def CreateTree(arr,index):
    if index>=len(arr):
        return;
    data=arr[index];
    root=Node(data);

    root.left=CreateTree(arr, 2*index+1);
    root.right=CreateTree(arr,2* index+2);

    return root

# Tree creation one node at a time
# def CreateTree(root=None):
#     data=int(input("Enter data\n"));
#     if data==-1 :
#         return None ;
#     else:
#         root=Node(data)
#         print(f"enter data for left of {root.value}")
#         root.left=CreateTree(root.left)
#         print(f"enter data for right of {root.value}")
#         root.right=CreateTree(root.right)

#         return root

    

class Solution:

    def Diameter(self,root):
        self.diameter=0;

        def trav(root):
            if root==None:
                return 0;
            left=trav(root.left)
            right=trav(root.right)
            self.diameter=max(self.diameter,left+right)
            
            return max(left, right)+1
        
        trav(root)
        return self.diameter+1

# input
# 25 15 50 10 22 35 70 4 12 18 24 31 44 66 90

ar=[25,15,50,10,22,35,70,4,12,18,24,31,44,66,90]

root=CreateTree(ar, 0)
# root=CreateTree()
sol=Solution()
di=sol.Diameter(root)
print("dia",di)