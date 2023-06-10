from queue import Queue
class Graph:
    def __init__(self,veritces):
        self.adjList={};
        for v in range(veritces):
            self.adjList[v]=[];

    def addEdge(self,src,dst,direction=False):
        self.adjList[src].append(dst);

        if not direction :  
            self.adjList[dst].append(src);

  
def BFS(graph):
    isVisited={key:False for key in graph.adjList.keys()}

    for v in graph.adjList.keys():
        q=Queue()
        q.put(v)

        if not isVisited[v]:
            while(not q.empty()):
                first=q.get()
                isVisited[first]=True

                print(first,end=" ")

                for i in graph.adjList[first]:

                    if  not isVisited[i]:
                        q.put(i)
                        isVisited[i]=True


vertices=int(input("Enter vertices\n"));
edges=int(input("Enter edges\n"));

g=Graph(vertices)

for _ in range(edges):
    src,dst=map(int,input().split(" "))
    g.addEdge(src, dst)

BFS(g)