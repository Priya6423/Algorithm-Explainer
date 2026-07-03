# Graphs

## Graph basics
A graph is a set of vertices (nodes) connected by edges. Edges can be directed (one-way) or undirected (two-way), and weighted (carrying a cost) or unweighted. Graphs model networks, dependencies, maps, and relationships. Two common representations: an adjacency list (each vertex stores a list of its neighbors, space O(V + E), efficient for sparse graphs) and an adjacency matrix (a V-by-V grid marking edges, space O(V^2), efficient for dense graphs and O(1) edge lookups).

## Breadth-first search (BFS)
BFS explores a graph level by level from a source, visiting all neighbors before moving outward, using a queue and a visited set. It finds the shortest path in terms of number of edges in an unweighted graph, because it reaches every node by the fewest hops. Time O(V + E), space O(V). The visited set must be marked when a node is enqueued (not when dequeued) to avoid adding the same node multiple times.

## Depth-first search (DFS)
DFS explores as far as possible along each branch before backtracking, using recursion or an explicit stack and a visited set. It is used for connectivity, cycle detection, topological sorting, and exploring all paths. Time O(V + E), space O(V) for the visited set plus recursion depth. On a grid, DFS or BFS from each unvisited land cell solves number-of-islands and connected-component counting.

## Grid as a graph
Many matrix problems are graph problems in disguise: each cell is a vertex and adjacent cells (up, down, left, right) are edges. Number of islands counts connected components of land cells; flood fill spreads from a start cell; rotting oranges is a multi-source BFS where all initially rotten cells start in the queue together. The bounds check (staying inside the grid) and marking visited cells are the usual sources of bugs.

## Cycle detection
In an undirected graph, a cycle exists if DFS reaches an already-visited node that is not the parent of the current node, so you must track the parent to ignore the edge you just came from. In a directed graph, a cycle exists if DFS reaches a node currently on the recursion stack (the "gray" set in three-color marking); a node fully explored ("black") does not indicate a cycle. Directed-cycle detection is the basis of detecting whether a dependency ordering is possible.

## Topological sort
A topological sort orders the vertices of a directed acyclic graph so every edge points forward — every prerequisite comes before what depends on it. Kahn's algorithm repeatedly removes nodes with in-degree zero and decrements their neighbors' in-degrees; if not all nodes are removed, the graph has a cycle and no valid ordering exists. This solves course-schedule and build-order problems. Time O(V + E).

## Shortest paths
In an unweighted graph, BFS gives shortest paths. In a weighted graph with non-negative weights, Dijkstra's algorithm uses a priority queue to always expand the closest unsettled node, O((V + E) log V). With negative weights, Bellman-Ford handles them and detects negative cycles in O(V*E). Choosing the right algorithm depends on whether edges are weighted and whether weights can be negative.

## Hashing and hash maps
A hash map stores key-value pairs and supports average O(1) insertion, lookup, and deletion by mapping keys to array indices through a hash function. Collisions (different keys hashing to the same index) are resolved by chaining (a list per bucket) or open addressing (probing for the next free slot). Worst case degrades to O(n) when many keys collide. Hash maps power frequency counting, deduplication, two-sum in one pass, and memoization caches.
