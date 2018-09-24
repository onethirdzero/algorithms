# Minimum Number of Steps Through a Maze

“Daily Coding Problem #23

This problem was asked by Google.

You are given an M by N matrix consisting of booleans that represents a board. Each True boolean represents a wall. Each False boolean represents a tile you can walk on.

Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps required to reach the end coordinate from the start. If there is no possible path, then return null. You can move up, left, down, and right. You cannot move through walls. You cannot wrap around the edges of the board.

For example, given the following board:

[[f, f, f, f],
[t, t, f, t],
[f, f, f, f],
[f, f, f, f]]
and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number of steps required to reach the end is 7, since we would need to go through (1, 2) because there is a wall everywhere else on the second row.”

## Prior Attempt

### Algorithm

* While not at destination
	* Record current
	* If next step is valid and not seen before
		* Determine if step has min steps
		* Return 1 + min steps
	* Else
		* Skip that next step

### Comments

* I couldn’t come up with an efficient way to check if the next step is valid - I would have brute forced it like this approach: [Daily Coding Problem: Problem #23 · GitHub](https://gist.github.com/folksilva/465f89b46db0d8c56eb788677349637d)
* I was trying to use techniques from the Spiral Matrix problem: a ‘seen’ matrix as well as checking the validity of candidate cells at each step - got lost in the implementation details

## Solution

* [Daily Coding Problem #23](https://galayko.rocks/posts/dcp/maze/)

### Algorithm

* For each cell in the matrix
	* Check if neighbour cells are valid
	* For each valid neighbour cell
		* Mark the number of steps from current cell to neighbour, `n+1`
* Return the marked value at the end coordinate

```py
def solution(maze, start, end):
	maze[start[0]][start[1]] = -1
	mark(maze, start, 0)
	return maze[end[0]][end[1]]

def mark(maze, coord, n):
	r, c = coord[0], coord[1]

	neighbours = {
		[r + 1, c]: False, # Down.
		[r - 1, c]: False, # Up.
		[r, c + 1]: False, # Right.
		[r, c - 1]: False # Left.
	}

	for k in neighbours.keys():
		# Check/mark if neighbours are valid.
		neighbours[k] = markP(maze, k[0], k[1], n + 1)

	for k, v in neighbours.items():
		if v:
			# If neighbour is valid.
			mark(maze, k, n + 1)

def markP(maze, r, c, n):
	if r > len(maze) or c > len(maze):
		return False
	if r < 0 or c < 0:
		return False
	if maze[r][c] != 0:
		# If True or an int not equal to 0.
		return False
	# At this point, maze[r][c] is a False.
	maze[r][c] = n
	return True
```

### Analysis

* Uses `O(k)` space, where `k` is the number of keys in the dictionary representing each neighbour
	* Since this is at most `4`, the dictionary uses `O(4)` space
* There’s the question of how much space the recursion takes on the stack, but to answer that, we’ll need to understand how to recursion progresses - I don’t know how to do this yet

* Time complexity also relies on understanding the recursion
* At this point, my guess is that the algorithm visits all `j` cells that are not walls - ie. the number of `False` cells
* Let this be `j` where `j <= n`  - in the worst case, it’s `O(n)`
* If so, space used on the call stack will also be `O(n)`

### Comments

* A useful technique here is using a dictionary to encode whether neighbours are valid, then letting the algorithm proceed based on that encoding

* From tracing a small example by hand, it seems that a single ‘recursion path’ (from the first time we recurse on a valid neighbour) will make its way to end first, before the other ‘pending’ calls (also from that first time) can proceed
* However, since the first ‘path’ already found the solution and marked many other cells along the way, the other paths will not get very far
* Regardless, they will be called anyway, since they were valid neighbours
