# Spiral Matrix

* [Spiral Matrix - LeetCode](https://leetcode.com/problems/spiral-matrix/description/)

## Prior Attempt

### Algorithm

* Move horizontally until we hit the end of the row
* Start moving vertically until we hit the end of the column
* At each stage, the range we use will be shrunk by an offset

### Comments

* It was hard to figure out how to manage the offset on each iteration
* Figuring out how to switch directions was tough too

## Simulation Approach

* [Spiral Matrix - LeetCode](https://leetcode.com/problems/spiral-matrix/solution/)
* Simulate the path of the spiral

### Algorithm

* Keep track of indices we’ve seen before in an auxiliary matrix
* For each element while traversing the spiral
	* Record the current element
	* If the candidate element is not out of bounds or not seen before
		* Move the cursor to that element
	* Else
		* Switch directions
* Return the recorded elements

```py
if not matrix: return []
R, C = len(matrix), len(matrix[0])
seen = [[False] * C for _ in matrix]
ans = []

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
r = c = di = 0

for _ in range(R * C):
    ans.append(matrix[r][c])
    seen[r][c] = True

    cr, cc = r + dr[di], c + dc[di]
    if 0 <= cr < R and 0 <= cc < C and not seen[cr][cc]:
        # If candidate indices are not out of bounds
        # and we haven't seen them before.
        r, c = cr, cc
    else:
        # Change directions.
        di = (di + 1) % 4
        r, c = r + dr[di], c + dc[di]

return ans
```

### Analysis

* Each element is visited once, so running time is `O(mn)` -> `O(n)`
* Uses `O(mn)` space to store the auxiliary matrix

* The most useful pattern here is using `dr` and `dc` to encode which directions to move in, and `di` to select which encoding to use

* The `seen` matrix is necessary once we get deeper into the spiral - without it, we would record elements we’ve already seen before
* In other words, we’d be going through the walls of the snake we’ve already drawn
