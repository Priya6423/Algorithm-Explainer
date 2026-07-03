# Dynamic Programming

## What dynamic programming is
Dynamic programming (DP) solves problems by breaking them into overlapping subproblems and storing each subproblem's answer so it is computed only once. It applies when a problem has two properties: optimal substructure (the optimal solution is built from optimal solutions to subproblems) and overlapping subproblems (the same subproblems recur many times). Without overlap, plain divide-and-conquer is enough; the overlap is what DP exploits by caching.

## Memoization (top-down)
Write the natural recursion, then cache each result the first time it is computed and return the cached value on later calls. The recursion explores the problem top-down from the original input; the cache turns exponential repeated work into linear-or-polynomial work. In Python this is often a dictionary keyed by the subproblem parameters, or the functools.lru_cache decorator. The number of distinct cached states times the work per state gives the time complexity.

## Tabulation (bottom-up)
Fill a table iteratively starting from the base cases and building up to the final answer. There is no recursion and no call-stack overhead. You must determine the order in which subproblems depend on each other so each entry is ready before it is needed. Tabulation and memoization usually have the same time complexity; tabulation avoids stack depth limits and is often slightly faster.

## Identifying a DP problem
Signals include: the problem asks for an optimum (min, max, longest, fewest) or a count of ways; a greedy choice does not obviously work; and the same smaller computation appears repeatedly. Define the state (what parameters uniquely describe a subproblem), the recurrence (how a state's answer is built from smaller states), and the base cases.

## 1D DP
The state is described by a single index. Climbing stairs: ways(i) = ways(i-1) + ways(i-2), base cases ways(0) = ways(1) = 1, which is the Fibonacci recurrence, O(n) time and O(1) space if you keep only the last two values. House robber and maximum-subarray (Kadane's) are also 1D DP. Kadane's tracks the best subarray sum ending at each index: current = max(nums[i], current + nums[i]), and the answer is the maximum current seen, O(n) time O(1) space.

## 2D DP
The state needs two indices, often comparing two sequences or moving on a grid. Examples: longest common subsequence (compare prefixes of two strings), edit distance, unique paths in a grid, and 0/1 knapsack (item index and remaining capacity). The table is filled in an order respecting dependencies, usually O(n*m) time and space, with space sometimes reducible to one or two rows.

## Common DP pitfalls
Wrong state definition is the most common error — the state must capture everything that affects future decisions. Incorrect base cases corrupt the whole table. Iterating in the wrong order in tabulation uses entries before they are filled. For knapsack-style problems, the order of loops (items vs. capacity, and ascending vs. descending) determines whether items can be reused, so it must match the problem.
