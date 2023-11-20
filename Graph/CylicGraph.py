from queue import Queue;

class Graph:
    def __init__(self,vertices):
        self.adjList={};
        for v in vertices:
            self.adjList[v]=[]

    def addEdge(self,src,dst,direction=False):
        self.adjList[src].append(dst);
        if not direction:
            self.adjList[dst].append(dst)

def detectCyclicGraph(graph):
    isCyclic=False;
    parent={}
    isVisited={}
    q=Queue()

    for v in graph.adjList.keys():
        q.append(v);
        parent[v]=-1;

        if not isVisited.get(v):
            while not q.empty():
                first=q.get();
                isVisited[first]=True;
                parent

                for i in graph.adjList[first]:
                    if not isVisited.get(i):
                        q.put(i)
                    

                

