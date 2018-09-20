# Fewest Classrooms

“Daily Coding Challenge #21

This problem was asked by Snapchat.

Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.”

## Prior Attempt

### Algorithm

* Sort lectures in descending order of start time
* Take leftmost lecture until no lecture left
	* Go through each room and check for the latest end time
	* If latest scheduled end time < start time of current lecture
		* Schedule the current lecture in this room
	* Else
		* Add a new room and schedule the current lecture there
* Return room count

### Analysis

* Sorting takes `O(n log n)`
* Going through each room and checking for the latest end time (lookup) takes `O(k)` where `k` is the number of rooms so far
	* We could potentially have `n` rooms in the worst case, so lookup is `O(n)`
* This is done for `n` lectures we need to schedule, so that part of the algorithm runs in `O(n^2)` time

* `O(n)` space - storing every given lecture

## Solution

* [LeetCode – Meeting Rooms II (Java)](https://www.programcreek.com/2014/05/leetcode-meeting-rooms-ii-java/)

### Algorithm

* Sort lectures in descending order of start time
* Use a priority queue (min heap), `q` to track end times
	* Initialize with the first sorted lecture
* For each lecture
	* If current lecture’s start time overlaps with `q.front` end time
		* Increase rooms by 1
	* Else
		* `q.pop()`
	* Add current lecture’s end time to `q`
* Return room count

### Analysis

* We only care about the end times of the last scheduled lecture in each room
	* Unlike the previous approach, we discard all other lectures that came before
	* At each step, we’re discarding the previously scheduled lecture if the current class doesn’t overlap with it
	* If we don’t discard one on this iteration, we’ll discard the earliest end time between the 2 going forward
* Because of the ‘sorting’ of the priority queue, our lookup for latest end time is `O(1)`
* Sorting then becomes the longest running time - so the algorithm runs in `O(n log n)`

* Priority queue grows to `O(k)` size, where `k` is the number of overlaps
	* We add and remove from `q` on each iteration, but skip removing when an overlap happens
	* Because we can’t remove more than twice on each iteration, we can never bring down the number of items in `q`
* In the worst case, there is an overlap between every lecture, so this algorithm uses `O(n)` space
