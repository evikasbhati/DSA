## Find Leaf Nodes and its count in a Tree
class Node:
    def __init__(self,value):
        self.value=value;
        self.left=None;
        self.right=None;

def createTree(root=None):

    data=int(input("Enter data \n"))

    if data==-1:
        return ;
    else:
        root=Node(data);
        print(f"Enter data to left of {root.value}");
        root.left= createTree(root.left)
        print(f"Enter data to right of {root.value}");
        root.right= createTree(root.right)
        
        return root;

tree=createTree()
count=0;



def FindLeaf(root):
    global count
    if root is None:
        return None;
    else:
        FindLeaf(root.left);
        FindLeaf(root.right);
        if root.left is None and root.right is None:
            print(root.value)
            count+=1
    return count    
print(f"Leaf node count is {FindLeaf(tree)}")
