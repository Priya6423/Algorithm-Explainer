# Time and Space Complexity (Big-O)

## What Big-O notation means
Big-O describes how the running time or memory of an algorithm grows as the input size n grows. It captures the dominant term and ignores constants and lower-order terms, because those stop mattering as n gets large. O(2n + 5) is written O(n); O(3n^2 + n) is written O(n^2). Big-O is an upper bound on growth — the worst-case rate at which cost increases.

## Common time complexities, fastest to slowest
- O(1) constant: the work does not depend on input size. Array index access, hash map lookup, arithmetic.
- O(log n) logarithmic: the input is halved each step. Binary search, balanced BST operations.
- O(n) linear: the work is proportional to input size. A single pass over an array.
- O(n log n): a linear amount of work done log n times. Efficient comparison sorts (merge sort, heap sort), and many divide-and-conquer algorithms.
- O(n^2) quadratic: nested loops over the same input. Bubble sort, comparing every pair of elements.
- O(2^n) exponential: the work doubles with each added element. Naive recursion over all subsets, brute-force subset enumeration.
- O(n!) factorial: enumerating all permutations. Brute-force traveling salesman, generating all orderings.

## How to reason about time complexity
Count how many times the innermost operation runs as a function of n. A single loop from 0 to n is O(n). Two nested loops each running n times is O(n^2). A loop that halves the range each iteration is O(log n). Sequential (non-nested) loops add: O(n) + O(n) = O(n). Nested loops multiply: an outer O(n) loop containing an inner O(n) loop is O(n^2).

## Space complexity
Space complexity measures the extra memory an algorithm uses beyond the input itself. An in-place algorithm that uses a few variables is O(1) auxiliary space. An algorithm that builds a new array of size n is O(n). Recursion adds space for the call stack: a recursion that goes n levels deep before returning uses O(n) stack space even if it allocates nothing else. This is why recursion depth matters — deep recursion can overflow the stack.

## Best, average, and worst case
The same algorithm can have different complexities depending on the input. Quicksort is O(n log n) on average but O(n^2) in the worst case (already-sorted input with a poor pivot). Hash map lookup is O(1) average but O(n) worst case (all keys collide). Big-O without qualification usually refers to the worst case, but it is worth stating which case you mean.

## Amortized complexity
Amortized analysis averages the cost of an operation over a sequence of operations. A dynamic array (Python list) append is O(1) amortized: most appends are O(1), but occasionally the array doubles and copies all n elements (O(n)). Spread across many appends, the average per-append cost is O(1).
