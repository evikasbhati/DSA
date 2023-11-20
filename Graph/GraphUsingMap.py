
class Graph:
    def __init__(self):
        self.adjList={};

    def addVertex(self,src):
        self.adjList[src]=[];

    def addEdge(self,src,dest,direction=False):
        if src not in self.adjList:
            self.addVertex(src);
        self.adjList[src].append(dest);

        if not direction :
            if dest not in self.adjList:
                self.addVertex(dest);  
            self.adjList[dest].append(src);

    def printGraph(self):
        for key,values in self.adjList.items():
            print(key,"->",values);
            
graph=Graph();

edges=int(input("Enter number of edges\n"));

print("Enter vertex and single neighbour seprated by space");

for _ in range(edges):
    src,dest=map(int,input().split(" "))
    graph.addEdge(src, dest)

graph.printGraph()