# Intersection of Two Linked Lists

“Daily Coding Problem #20

This problem was asked by Google.

Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

In this example, assume nodes with the same value are the exact same node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.”

## Brute Force Approaches

### Algorithm
* For each node in list A
	* For each node in list B
		* If `a == b`, return that node

### Analysis
* `O(mn)` running time, `O(1)` space

### Algorithm
* Traverse each node in list A, storing each in an array
* Traverse each node in list B and do a lookup on the array to compare values
* Return the node with the matching value

### Analysis
* `O(m+mn)` running time, `O(m)` space
* We could speed up the `O(m)` look up by using a hash table, which would bring the running time down to `O(m+n)`

## Solution

* [Write a function to get the intersection point of two Linked Lists. - GeeksforGeeks](https://www.geeksforgeeks.org/write-a-function-to-get-the-intersection-point-of-two-linked-lists/)

### Algorithm
* Traverse A and calculate the length
* Traverse B and calculate the length
* Calculate the difference in length, `d`
* Traverse the longer list up to the `d`th node
* Compare `a` and `b` - if they match, return the intersecting node

### Analysis

* `O(m+n)` running time, `O(1)` space

* I had seen a variation of this problem before, where all we wanted was to determine if the lists intersected or not
* We could do this by traversing to the end of both lists and recording the last node’s address/value - if they matched, that meant the lists intersected
