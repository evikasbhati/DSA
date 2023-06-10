# Created graph using AdjacencyList with n veritces and m edges

class Graph:
    def __init__(self,vertices):
        self.adjList={};
        for v in range(vertices):
            self.adjList[v]=[];

    def addEdge(self,src,dst,direction=False):
        self.adjList[src].append(dst);

        if not direction :  
            self.adjList[dst].append(src);


    def printadjList(self):
        for node,values in self.adjList.items():
            print(node,"->",values)


edges=int(input("Enter number of edges\n"));
vertices=int(input("Enter vertices\n"));

g=Graph(vertices)
  
for _ in range(edges):
    src,dest=map(int,input().split(" "))
    g.addEdge(src, dest)

g.printadjList();  