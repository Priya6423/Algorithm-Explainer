# Searching and Array Traversal Patterns

## Linear search
Scans every element until the target is found or the array ends. Time complexity O(n), space O(1). It works on unsorted data and is the fallback when no structure can be exploited.

## Binary search
Searches a sorted array by repeatedly halving the search range. It compares the target to the middle element and discards the half that cannot contain the target. Time complexity O(log n), space O(1) iterative. The array must be sorted. The classic bug is the loop boundary and the mid calculation; using low + (high - low) // 2 avoids overflow in languages with fixed-size integers, and the loop condition while low <= high with high = mid - 1 / low = mid + 1 updates is the standard correct form.

## Binary search on the answer
A powerful variant where you binary search over a range of possible answers rather than over array indices. You define a monotonic feasibility check — "can the task be done with capacity/speed/value x?" — and binary search for the smallest (or largest) x that satisfies it. The feasibility check is usually O(n), giving O(n log(range)) total. This pattern solves problems like minimum eating speed, splitting an array to minimize the largest sum, and capacity-to-ship-packages problems.

## Two-pointer pattern
Uses two indices that move toward each other or in the same direction to avoid a nested loop. On a sorted array, one pointer starts at the left and one at the right; you move them inward based on whether the current sum or condition is too small or too large. This turns an O(n^2) pair-search into O(n). It solves two-sum on a sorted array, valid palindrome checks, reversing in place, and container-with-most-water. The key requirement is usually that the data is sorted or that movement decisions are monotonic.

## Fast and slow pointers
A two-pointer variant where one pointer moves twice as fast as the other. It detects cycles (Floyd's cycle detection), finds the middle of a linked list in one pass, and finds the cycle entry point. If a cycle exists the fast pointer eventually laps the slow one and they meet.

## Sliding window
Maintains a contiguous window over an array or string and slides it to avoid recomputing overlapping work. A fixed-size window moves both ends together. A variable-size window expands the right edge to include elements and contracts the left edge when a constraint is violated. Time complexity O(n) because each element enters and leaves the window at most once. It solves longest-substring-without-repeating-characters, minimum-window-substring, and maximum-sum-subarray-of-size-k. The window state is usually tracked with a hash map of counts or a running sum.

## Prefix sums
Precompute a running total array where prefix[i] is the sum of the first i elements. Any subarray sum from i to j is then prefix[j+1] - prefix[i] in O(1). Building the prefix array is O(n), and it turns repeated range-sum queries from O(n) each into O(1) each. The same idea extends to prefix counts and 2D prefix sums for submatrix queries.
