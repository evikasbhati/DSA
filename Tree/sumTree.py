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


class Solution:
    def __init__(self):
        self.sumTree=True;
        
    def checkSum(self,root):

        def checkSumTree(root):
            
            if root==None:
                return 0;
            left=checkSumTree(root.left)
            right=checkSumTree(root.right)
    
            if root.left is None and root.right is None:
                return root.value;
    
            if root.value!=left+right:
                self.sumTree=False;
                # return self.sumTree
            return root.value+left+right
            
        checkSumTree(root)
        return self.sumTree

ar=[int(i) for i in input().split(" ")];
    
tree=CreateTree(ar, 0)
sol=Solution()
print(sol.checkSum(tree));