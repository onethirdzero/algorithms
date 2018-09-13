# Number of Ways to Reach nth Staircase Step

“Daily Coding Problem #12

This problem was asked by Amazon.

There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2
What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.“

## Prior Attempt

* Create decision tree
* DF traversal of the tree to count all leaves
* Return the number of leaves

* I want to say that creating a decision tree has `O(n)` time complexity, but I don’t know how to prove it
* DF traversal is `O(n)`

* We do construct an entire tree here, so space taken would be at least `n` (take only 1 step at a time), but I’m not sure how to generalize how many other nodes will exist

* I don’t know how to optimize the space for this
* The solution has options for optimization, so it’s probably a better route to go with

## Solution

* [Count ways to reach the n’th stair - GeeksforGeeks](https://www.geeksforgeeks.org/count-ways-reach-nth-stair/)
* We can reach the `n`th step from either the `n-1`th step or the `n-2`th step
* The solution immediately suggests that the recurrence relation is:
```
ways(n) = ways(n - 2) + ways(n - 1)
```
* To me, this is only obvious if you’ve seen the decision tree and understand the significance of its leaves

* Notice that the recurrence relation is similar to the one for the Fibonacci sequence:
```
fib(n) = fib(n - 1) + fib(n - 2)
```
* However, the values for `ways()` are shifted behind by `1`
```
ways(1) = 1 = fib(2)
ways(2) = 2 = fib(3)
ways(3) = 3 = fib(4)
```
* So we can call `ways(n) = fib(n + 1)` to return the answer to us

* We know that the naive implementation of the Fibonacci function runs in exponential time - `T(n) = T(n - 1) + T(n - 2)`
* If we consider the size of the call stack, then this algorithm runs with `O(n)` space
* We can optimize these the same way we optimize a Fibonacci function: [Program for Fibonacci numbers - GeeksforGeeks](https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/)
