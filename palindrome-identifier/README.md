# Lab 1 Finding a Palindrome

## Task
Write a routine called find_palindrome(**pattern**: tuple)->tuple | None:
The returned tuple must be a palindrome which is results from removing just one element from the **pattern**
### Rules
- The Algorithm must run at O(n) time complexity
- Single element palindromes return **None**
- Throw no exceptions
- Only way to change a pattern is to remove a whole element
- You must remove one element for the output to be valid
### Examples
- ✅ (3,1,2,3)         -- remove  2  --> (3,1,3)
- ❌ ("ab","a","a")    -- remove "b" --> ("a","a","a")
- ✅ ("g","a","a","g") -- remove "a" --> ("g","a","g")

## Planning
### Ideas
- Palindromes by definition can be split in half, because the first half should always be the same as the second half we only need to check them with eachother. Find if there is ONE difference and remove it. If there is more than one difference then return None.
```
(1,2,2,3,1) -> (1,2) & (3,1) -> (1,2) & (1,3) -> (1,2,2,1)
     ^               ^                ^              ^
     |               |                |              |
   input           split             flip          result
in this case, remove the element that is not similar to middle element

(1,2,3,1) -> (1,2) & (3,1) -> (1,2) & (1,3) -> (1,2,2,1)
    ^              ^                ^              ^
    |              |                |              |
  input          split             flip          result
in this case, remove either of them it doesnt matter
```

### Example
1. Input: pattern: tuple
2. Check if tuple element count is greater than 2
3. Find the midpoint of the tuple, odd: split on either side of element, even: split in half evenly
4. Compare first half with second, if there is one difference remove it if its not the same as the middle number

# Solution

```
I'll be using the palindrome that I've been struggling with:
1,2,3,3,2,1,1
n=7
odd palindrome 

1. get center = int(7/2) = 3
2. seperate into 2 lists [1,2,3] [3,2,1,1]
3. flip the second list  [1,2,3] [1,1,2,3]
4. compare lists [1,2,3]
                 [1,1,2,3]
[0] is the same
[1] is different, now we check neighbors

A[1] will check A[2] = 3
B[1] will check B[2] = 2
If either of the neighbors are equal to the current position element we remove the one with the neighbor

A[1] = B[2] so we will remove B[1]

new palindrome:
1,2,3,3,2,1
```
1,1,1,2,1
[1,1] [1,2,1]

A[1,1]
B[1,2,1]

A[1] = 1
A[2] = NULL
B[1] = 2
B[2] = 1

A[1] = B[2]
remove B[1]
1,1,1,1


## Issues
(1, 2, 3, 4, 2, 1), currently its returning None due to the fact its an even palindrome and 3 & 4 dont have neighbors. So in the case of evens with the only difference being the center we can remove the center element.

