# Trees and Binary Trees

## Tree basics
A tree is a hierarchical structure of nodes where each node has a value and references to child nodes, with exactly one root and no cycles. A binary tree restricts each node to at most two children (left and right). The height of a tree is the number of edges on the longest root-to-leaf path; a balanced tree of n nodes has height O(log n), while a degenerate (linked-list-shaped) tree has height O(n). Height determines the cost of many operations.

## Tree traversals (DFS)
Depth-first traversals visit a whole subtree before moving on, usually implemented recursively. Preorder visits node, then left, then right (useful for copying a tree or producing prefix expressions). Inorder visits left, node, right (on a binary search tree this yields values in sorted order). Postorder visits left, right, then node (useful for deleting a tree or computing values that depend on children first). All three are O(n) time and O(h) space for the recursion stack, where h is the height.

## Level-order traversal (BFS)
Breadth-first traversal visits nodes level by level, top to bottom, left to right, using a queue. Start with the root in the queue; repeatedly remove a node, process it, and enqueue its children. To group output by level, record the queue size at the start of each level and process exactly that many nodes before moving to the next level. Time O(n), space O(n) for the queue in the worst case (a full bottom level).

## Two-channel / fusion pattern
Some tree problems need a recursion that returns one value to the parent while also updating a separate global answer. The diameter of a binary tree is the classic example: the recursion returns the height of each subtree to its parent, but along the way it updates a shared maximum with (left height + right height) at each node. In Python the shared variable is updated through a closure using the nonlocal keyword, or by wrapping it in a list/attribute. Confusing the returned value (height) with the tracked answer (diameter) is the common mistake here.

## Binary search tree (BST)
A binary search tree keeps, for every node, all left-subtree values less than the node and all right-subtree values greater. This invariant makes search, insertion, and deletion O(h): start at the root and go left or right by comparing the target to the current value. On a balanced BST h is O(log n); on an unbalanced one it degrades to O(n). Inorder traversal of a BST produces sorted output, which is a frequent way to validate a BST or find the kth smallest element.

## Balanced trees
Self-balancing trees (AVL, red-black) perform rotations on insertion and deletion to keep height O(log n), guaranteeing O(log n) operations even in the worst case. They trade extra bookkeeping for predictable performance and underlie ordered maps and sets in many standard libraries.

## Recursion on trees
Most tree algorithms are naturally recursive: solve the problem for the left and right subtrees, then combine their results for the current node. The base case is usually a null node returning a neutral value (0 for height, true for emptiness checks). Always handle the null-node base case first to avoid dereferencing a missing child.
