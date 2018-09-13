# Random Number From Stream with O(1) Space

“Daily Coding Problem #13

This problem was asked by Facebook.

Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.”

## Prior Attempt

* Fill up a file of fixed sized as the stream comes in and label it iteratively with a number
* At any time that we want a random number from the stream, generate a random number and use it open a stored file, then grab a random line from it as the return value

* This still uses storage memory, which will not hold an ever-growing input - misunderstood the question

## Solution

### Algorithm

[Select a random number from stream, with O(1) space - GeeksforGeeks](https://www.geeksforgeeks.org/select-a-random-number-from-stream-with-o1-space/)
* Initialize a global `count = 0`
* For each `x` from the stream
	* Increment `count`
	* If count is `1`, `result = x`
	* Else
		* Generate a random `i` in the range `[0, count - 1]`
		* If `i` is `count - 1`, `result = x`
	* Return `result`

### Analysis

* Important to note is that `result` is replaced every time `i == count - 1`

* We need to prove that every returned element was selected randomly ie. with a probability of `1/n`
* For every new item, we pick a random `i` in the range `[0, count - 1]`
* If `i` is `count - 1`, we return `x` - so `x` has a `1/n` chance of being picked

* Now to prove for the rest of the elements
* Consider the 2nd last element returned
* The probability that it replaces the previously stored element is `1/(n - 1)`
* When the `n`th stream element comes in, the probability of the 2nd last element being picked is `(n - 1)/n`
* So the total probability of the 2nd last element being picked on the `n`th iteration is: `1/(n - 1) * (n - 1)/n = 1/n`
	* This is because the 2nd last element can only be picked if it replaced the previously stored element on the `n-1`th iteration first
* We can argue similarly for the remaining elements

* Since we don’t use any extra memory as `n` grows, the algorithm runs in `O(1)` space
* Since the algorithm is called upon arrival of a new `n`, it runs in `O(1)` time
