# facebook-small-world
The project analyzes facebook dataset to draw insights about the connection(s) between two people.

## Dataset Details
Source: [http://snap.stanford.edu/data/egonets-Facebook.html]
Other: 88,234 edges (undirected edges representing Facebook friendship) in a sampled 4,039-node network.

## Objective and methodologies used
The project tries to answer the following questions: 
### 1. How many different ways are two people connected on average ?
This can be answered by finding the average number of edge disjoint paths between two nodes.
By theorem, from >>.. :
Given any graph G, the number of edge-disjoint paths between a source s and a sink t equals the max-(s, t)-flow in (G, c) where c(e) = 1 for all edges e.
So, to find the max-(s, t)-flow, Ford Fulkerson algorithm was used.

Ford-Fulkerson Algorithm algorithm was implemented, which, given a directed graph, a source s, a sink t, and edge capacities over each edge in E, computes the maximum flow from s to t.

In order to run our algorithm on the undirected Facebook graph (Gu), we need to transform it into a directed graph(Gd). To achieve this, every undirected edge between nodes u and v can be replaced with two directed edges, u to v and v to u, both of weights 1. Can you think of why this won't be a problem ?


## Assumptions:
1. Commutativity in relationships between two people via undirected graph (If you are my friends, I am your friend with same magnitude.) 
2.  

## Execution trace snapshots:
The algorithm was run times 101 times on the Facebook data, selecting two random nodes each time, to produce a rough average of the number of edge-disjoint paths that exist between two random nodes on the graph.
The average of the number of edge-disjoint paths = 15

![alt text](https://github.com/mohit-chawla/facebook-small-world/output/run_1_1.png "")
![alt text](https://github.com/mohit-chawla/facebook-small-world/output/run_1_2.png "")
![alt text](https://github.com/mohit-chawla/facebook-small-world/output/run_1_3.png "")
![alt text](https://github.com/mohit-chawla/facebook-small-world/output/run_1_4.png "")
## Relevant Resources: 
1. [Ford Fulkerson algorithm](https://en.wikipedia.org/wiki/Ford–Fulkerson_algorithm) 
2. [Small World Experiment](https://en.wikipedia.org/wiki/Small-world_experiment)
 
