# Merge K sorted lists of size N

* [How To Solve a Hard Programming Interview Question · Daily Coding Problem](https://www.dailycodingproblem.com/blog/how-to-solve-a-hard-programming-interview-question/)

## Algorithm

* Initialize the merged list
* Initialize the heap with the first element of the `K` sublists
    * Each element is a tuple containing the element value, the sublist index, and the element index within the sublist
* While heap is not empty
	* Pop an element off the heap
	* Append that element to the merged list
	* If the popped element was not the last one in its list
		* Append the next element in that list to the heap
* Return the merged list

## Complexity

* Time: `O(KN log K)`
	* Heap insert and pop are `O(log k)`, repeated for `KN` elements
	* Heapify is `O(k)`
* Space: `O(KN)` - size of the merged list
	* If we disregard the merged list, the size of the heap is never greater than `K`, since we always pop/insert `1` element into the heap at a time

## Comments

* Encoding `(val, list_ind, elem_ind)` in each heap element gives us the ability to easily switch which sublist we want to pick the next element from

* “Let’s say the smallest element is E. Once we get E, we know we’re interested in only the next element of the list that held E. Then we’d extract out the second smallest element and etc.”
* If the extracted element wasn’t the smallest among the `K` elements currently in the heap, the heap property still ensures that we get the smallest element when popping from it
* eg. `[[1,3],[2,2],[3,4]]` -> `[[3],[2],[4]]`
	* Heap: `[1, 2, 3]`
	* Popped element from heap: `1` - therefore, we would extract `3` from `[3]` to be inserted into the heap next
	* Heap: `[2, 3, 3]` - the heap would still give us `2` as the min
