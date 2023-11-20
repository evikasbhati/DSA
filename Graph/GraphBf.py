from queue import Queue;

class Graph:
    def __init__(self):
        self.adjList={}

    def addVertex(self,src):
        self.adjList[src]=[];

    def addEdge(self,src,dest,direction=False):
        if src not in self.adjList:
            self.addVertex(src);
        self.adjList[src].append(dest);

        if not direction:
            if dest not in self.adjList:
                self.addVertex(dest);
            self.adjList[dest].append(src);

def BFS(graph):
    isVisited=[]
    # que=Queue();
    que=[];
    keys=graph.adjList.keys();

    for key in keys:
        if key not in isVisited:
            if key not in que:
                que.append(key)
            isVisited.append(key);
            values=graph.adjList[key];
            for i in values:
                if i not in que:
                    que.append(i);

    for i in que:
        print(i,end=" ");

gra=Graph();

edges=int(input("Enter number of vertices\n"));
for _  in range(edges):
    src,dst=map(int,input().split(" "));
    gra.addEdge(src,dst);

BFS(gra);