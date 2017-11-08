# facebook-small-world
The project analyzes facebook dataset to draw insights about the connection(s) between two people.

## Dataset Details
Source: [http://snap.stanford.edu/data/egonets-Facebook.html]
Other: 88,234 edges (undirected edges representing Facebook friendship) in a sampled 4,039-node network.

## Objectives and methodologies used
The project tries to answer the following questions: 
### 1. How many different ways are two people connected on average ?
This can be answered by finding the average number of edge disjoint paths between two nodes.
By theorem, from >>.. :
Given any graph G, the number of edge-disjoint paths between a source s and a sink t equals the max-(s, t)-flow in (G, c) where c(e) = 1 for all edges e.
So, to find the max-(s, t)-flow, Ford Fulkerson algorithm was used.

Ford-Fulkerson Algorithm algorithm was implemented, which, given a directed graph, a source s, a sink t, and edge capacities over each edge in E, computes the maximum flow from s to t.

2. 
3.
4.


## Assumptions:
1. Undirected graph (If you are my friends, I am your friend with same magnitude.) 

