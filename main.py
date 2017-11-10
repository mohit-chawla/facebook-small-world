"""
Facebook small world experiment-1
Number of different ways in which two people are connected

Author: Mohit Chawla (www.mohitchawla.in)
"""
import random as rand

INFINITY = float("Inf")

#flag to enable trace
trace_enabled = True
def trace(string):
    """ Enable to print trace statements 
        set trace_enabled flag
    """
    if trace_enabled:
        print(string)


class Graph: 
    """ This class represents a directed graph using adjacency matrix representation"""
    def __init__(self,graph):
        self.graph = graph
        self.ROWS = len(graph)
        self.COLS = len(graph[0])

    def BFS(self,s,t,parent):
        """ Returns true if there is a path from source 's' to sink 't', 
            fills the parent[] to store the path """
        #mark all vertices as not visited
        visited = [False]*(self.ROWS);
        # initialize a queue
        queue = []
        # add source to q and mark it visited
        queue.append(s)
        visited[s] = True
        #Breadth-first-search
        while queue:
            n = queue.pop(0)
            for index,val in enumerate(self.graph[n]):
                if visited[index] == False and val>0:
                    queue.append(index)
                    visited[index] = True
                    parent[index] = n
        #return True if sink was visted
        if visited[t]:
            return True
        else:
            return False
    
    def maxFlow(self,source,sink):
        """ Ford Fulkerson algorithm """
        """Returns max flow in a graph from source to sink"""
        parent = [-1]*(self.ROWS)
        max_flow = 0
        
        #augment, while there is a path from source to sink
        while self.BFS(source,sink,parent):
            #find min residual capacity
            path_flow = INFINITY
            s = sink
            while(s !=  source):
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]
            #add to max flow
            max_flow += path_flow
            # update residual capacities of the edges and reverse edges along the path
            v = sink
            while(v !=  source):
                u = parent[v]
                self.graph[u][v] -= path_flow #decrease flow from edge
                self.graph[v][u] += path_flow #add reverse edge with capacity flow
                v = parent[v] #recurse
            
        return max_flow


#maximum flow for figure 5.1 lecture notes
fig_5_1 = [[0,1,0,3],[0,0,1,2],[0,0,0,0],[0,0,1,0]]
source = 0; sink = 2
g_5_1 = Graph(fig_5_1)
#print("Maximum flow for figure 5.1 is %d"%g_5_1.maxFlow(source,sink))            

#maximum flow for figure 5.3 lecture notes
fig_5_3 = [[0,1,1,1,1,1,0,0,0,0,0,0],[0,0,0,0,0,0,0,INFINITY,0,0,0,0],[0,0,0,0,0,0,INFINITY,INFINITY,0,0,0,0],[0,0,0,0,0,0,INFINITY,0,0,0,0,0],[0,0,0,0,0,0,0,0,INFINITY,0,INFINITY,0],[0,0,0,0,0,0,0,0,INFINITY,INFINITY,0,0],[0,0,0,0,0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0,0,0,0,0]]
source = 0; sink = 11
g_5_3 = Graph(fig_5_3)
#print("Maximum flow for figure 5.3 is %d"%g_5_3.maxFlow(source,sink))            



fig_edge_disjoint = [[0,1,1,0],[1,0,1,1],[1,1,0,1],[0,1,1,0]]
source = 0; sink = 3
g_edge_disj = Graph(fig_edge_disjoint)
#print("Number of edge disjoint paths are %d"%g_edge_disj.maxFlow(source,sink))            

fig_edge_disjoint = [[0,1,1,0,1],[1,0,1,1,0],[1,1,0,1,0],[0,1,1,0,1],[1,0,0,1,0]]
source = 0; sink = 3
g_edge_disj = Graph(fig_edge_disjoint)
#print("Number of edge disjoint paths are %d"%g_edge_disj.maxFlow(source,sink))            

print("Reading facebook dataset")
NODES = 4039
input_file = open("facebook_combined.txt","r")
ITERATIONS = 101

fb_adjacency_matrix = [[0] * NODES for i in range(NODES)]

for line in input_file:
    node_a,node_b = line.split(" ") 
    fb_adjacency_matrix[int(node_a)][int(node_b)] = 1
    fb_adjacency_matrix[int(node_b)][int(node_a)] = 1

#print(fb_adjacency_matrix[0])
   
fb_graph = Graph(fb_adjacency_matrix)
avg_edge_disjoint_paths = 0
print("Started # of edge-disjoint paths experiment with total iterations %d"%(ITERATIONS))
for i in range(ITERATIONS):
    source = rand.randint(0,NODES-1)
    sink = rand.randint(0,NODES-1)
    print("Iteration %d randomly selected source:%d,sink:%d "%(i+1,source,sink))
    paths = fb_graph.maxFlow(source,sink)
    print("Number of edge disjoint paths are %d"%paths)            
    avg_edge_disjoint_paths += paths

avg_edge_disjoint_paths /=ITERATIONS
print("Average number of edge-disjoint paths that exist between two random nodes on the graph is:%d"%avg_edge_disjoint_paths )            

            
