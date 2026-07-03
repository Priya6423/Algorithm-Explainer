# Recursion and Backtracking

## Recursion fundamentals
A recursive function solves a problem by calling itself on smaller inputs until it reaches a base case that can be answered directly. Every recursion needs two things: a base case that stops the recursion, and a recursive case that reduces the problem toward the base case. Missing or wrong base cases cause infinite recursion and stack overflow. The call stack stores each pending call, so recursion depth of d uses O(d) space even when no other memory is allocated.

## Returning values up the recursion
When a recursive call computes a result you need, you must capture its return value and use or re-return it at every level. A common bug is calling the recursion but discarding what it returns, so the answer never propagates back up. In tree problems especially, the value computed for a subtree must be returned to the parent call to be combined.

## Divide and conquer
A recursion pattern that splits the problem into independent subproblems, solves each recursively, and combines the results. Merge sort, quicksort, and binary search are divide-and-conquer. The complexity is often analyzed with the recurrence T(n) = a*T(n/b) + f(n); for merge sort that is T(n) = 2T(n/2) + O(n) = O(n log n).

## Backtracking
A systematic way to explore all candidate solutions by building them incrementally and abandoning a path ("backtracking") as soon as it cannot lead to a valid solution. The template is: choose an option, recurse to explore the consequences, then undo the choice before trying the next option. Backtracking solves permutations, combinations, subsets, N-Queens, Sudoku, and word search.

## Backtracking template
Maintain a partial solution (a path). At each step, loop over the available choices; for each choice, add it to the path, recurse, then remove it (the undo step). A base case appends a copy of the path to the results when the solution is complete. Forgetting to undo the choice corrupts later branches; appending the path without copying it stores a reference that later mutations will change.

## Avoiding duplicates in backtracking
When the input contains duplicates and you must not produce duplicate results, sort the input first, then skip a choice if it equals the previous choice at the same recursion level (a guard like: if i > start and nums[i] == nums[i-1]: continue). The sort groups equal values together so the skip works. This duplicate-skip logic appears in subsets-with-duplicates and combination-sum problems and is a frequent source of bugs.

## Complexity of backtracking
Backtracking typically explores an exponential search space: O(2^n) for subsets, O(n!) for permutations, multiplied by the work done at each node (often O(n) to copy the path). Pruning invalid branches early is what makes backtracking tractable in practice even though the worst case is exponential.
