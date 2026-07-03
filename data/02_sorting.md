# Sorting Algorithms

## Bubble sort
Repeatedly steps through the list, compares adjacent elements, and swaps them if they are out of order. After each full pass the largest unsorted element "bubbles" to its correct position at the end. Time complexity O(n^2) average and worst case, O(n) best case if the list is already sorted and a swap-flag early exit is used. Space O(1). It is simple but impractical for large inputs; mostly used for teaching.

## Selection sort
Divides the list into a sorted and unsorted region. Repeatedly finds the minimum element in the unsorted region and swaps it into the next sorted position. Time complexity O(n^2) in all cases because it always scans the remaining unsorted region. Space O(1). It makes the minimum number of swaps (O(n)) but the maximum number of comparisons.

## Insertion sort
Builds the sorted list one element at a time by taking the next element and inserting it into its correct position among the already-sorted elements, shifting larger elements right. Time complexity O(n^2) average and worst case, but O(n) on nearly-sorted data, which makes it excellent for small or almost-sorted inputs. Space O(1). It is stable and is often used as the base case inside faster sorts.

## Merge sort
A divide-and-conquer algorithm. It splits the array in half recursively until each piece has one element, then merges the sorted halves back together in linear time. Time complexity O(n log n) in all cases — the log n comes from the halving depth, the n from the merge at each level. Space O(n) for the temporary merge buffers. It is stable and has predictable performance, which makes it a good choice when worst-case guarantees matter.

## Quicksort
A divide-and-conquer algorithm that picks a pivot, partitions the array so smaller elements go left and larger go right, then recursively sorts each partition. Time complexity O(n log n) on average but O(n^2) in the worst case when the pivot consistently splits poorly (for example, always picking the first element of already-sorted data). Space O(log n) average for the recursion stack. It is usually faster in practice than merge sort due to good cache behavior and in-place partitioning, and randomized pivot selection makes the worst case unlikely.

## Heap sort
Builds a max-heap from the array, then repeatedly extracts the maximum and places it at the end. Time complexity O(n log n) in all cases. Space O(1) because it sorts in place. It is not stable. It guarantees O(n log n) worst case without the extra space of merge sort, but constant factors make it usually slower than quicksort in practice.

## Stability
A sort is stable if equal elements keep their original relative order. Merge sort and insertion sort are stable; quicksort and heap sort are not (in their standard forms). Stability matters when sorting records by one key while preserving an earlier ordering by another key.

## Choosing a sort
Use a library sort (Python's Timsort, a hybrid of merge and insertion sort, O(n log n)) in real code. Choose merge sort when you need stability and guaranteed worst case; quicksort when average speed and low memory matter; insertion sort for tiny or nearly-sorted inputs.
