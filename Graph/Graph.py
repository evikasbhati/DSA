# Created graph using ajacentList with n veritces and m edges

class Graph:
    def __init__(self):
        self.vertices=0;
        self.adjList={}

    def addEdge(self,src,dest,direction=False):
        if src in self.adjList:
            self.adjList[src].append(dest)
        else:
            self.adjList[src]=[]
            self.adjList[src].append(dest)

        self.vertices+=1


    def printadjList(self):
        for node,values in self.adjList.items():
            print(node,"->",values)


g=Graph()
edges=int(input("Enter number of edges\n")); 
  
for _ in range(edges):
    src,dest=map(int,input().split(" "))
    g.addEdge(src, dest)

g.printadjList();  
print(g.adjList)     