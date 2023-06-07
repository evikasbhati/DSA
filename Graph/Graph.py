class Graph:
    def __init__(self):
        self.vertices=0;
        self.adjList={}

    def addEdge(self,src,dest,direction=False):
        self.adjList[src]=[];
        self.adjList[src].append(dest)

        if direction:
            self.adjList[dest].append(src)

        self.vertices+=1


    def printadjList(self):
        for node,values in self.adjList.items():
            print(node,"->",values)


# if __name__=="main":

g=Graph()
edges=int(input("Enter number of edges\n"));   
for _ in range(edges):
    src,dest=map(int,input().split(" "))
    g.addEdge(src, dest)

g.printadjList();       