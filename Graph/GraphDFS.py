from collections import deque;
class Graph:
    def __init__(self,vertices):
        self.adjList={};
        for v in range(vertices):
            self.adjList[v]=[];

    def addEdge(self,src,dst,direction=False):
        self.adjList[src].append(dst)

        if not direction:
            self.adjList[dst].append(src);


def DFS(graph):
    # isVistited={i:False for i in graph.adjList.keys()}

    isVisited={}
    stack=deque()
    for v in graph.adjList.keys():

        if  not isVisited.get(v): # .get() give None if key is not present. Used to neglect iteration for isVistited
            stack.append(v)
            while  len(stack)>0:
                first=stack.pop()
                print(first,end=" ")
                isVisited[first]=True 
                
                for i in graph.adjList[first]:
                    if not isVisited.get(i):
                        stack.append(i)
                        isVisited[i]=True


vertices=int(input("Enter number of vertices\n"));
edges=int(input("Enter number of edges\n"));

g=Graph(vertices);
for _ in range(edges):
    sr,ds=map(int,input().split(" "))
    g.addEdge(sr,ds)
DFS(g)

