from collections import deque

class Graph:
    def __init__(self, vertex):
        self.mat = [[0]* vertex for x in range(vertex) ] 
        self.size = vertex

    def add_edge(self, src, dest):
        if 0 <= src < self.size and 0 <= dest < self.size:
            self.mat[src][dest] = 1
            self.mat[dest][src] = 1
        else: 
            print("Invalid Edge")

    def print(self):
        for row in self.mat:
            print(" ".join(map(str, row)))

    def BFS(self, src):
        visited = [False] * self.size
        queue = deque([src])
        visited[src] = True

        while queue:
            v = queue.popleft()
            print(v, end = " ")

            for i in range(self.size):
                if self.mat[v][i] == 1 and visited[i] == False:
                    visited[i] = True
                    queue.append(i)


    
g = Graph(6)
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(2,3)
g.add_edge(2,4)
g.add_edge(3,5)
g.add_edge(4,5)

g.BFS(0)

# 0 1 1 0 0 0
# 1 0 0 0 0 0
# 1 0 0 1 1 0
# 0 0 1 0 0 1
# 0 0 1 0 0 1
# 0 0 0 1 1 0

# visited = [T, F, F, F, F, F]
# src = 0
# queue = [0]

# v = 0