# Algorithms

## Time Complexity

The time of execution.

### Calculate

Remove the constants.
- We dont care about constants because constants only matter at smaller inputs which are insignificant to our CPU.
- If you mapped n^2 and 2n on a graph, 2n would be higher than n^2 in terms of runtime (y) only for smaller input (x). Eventually they would intersect and n^2 will always be bigger

### O(1) 

Number of operations is constant relative to the input size.

USUALLY access is instant.

Not always fast, there could be 1000 operations and the time complexity could still be O(1).

### Amortized

Average time per operation
- Used to ensure the average performance is acceptable, even if some individual operations might take longer

## Space Complexity

*Not as relevant as time complexity* 

## Edge case checking

> Input = anything you are operating on to get output

**If you have input, you have to validate it.**
- Not empty
- Correct type
- Need to compare? Input needs > 1

**Never make any assumptions about your input**

## Sorting Algorithms

### Insertion sort

Best for when data is small

## Common Algorithms

### Shifting

Start at the beginning of the direction you are shifting
- Shifting everything to the left? Start at the left side
- Shifting everything to the right? Start at the right side

### In-place algorithm

Algorithm that doesnt require extra space proportional to the input size.

i.e. dont create another array for storing values, just edit the existing array

**How 2**:
1) Keep a Left pointer and a Right pointer
2) Update `R` w/ O(n) loop
   `for R in range(len(myList))`
3) Move the data at `R` to `L` when condition is met
   `if(myList[L] != myList[R])`
4) BE CAREFUL how you update `L`
   - Keep in mind if `L` starts at 0, +1 for the length of L elements 

### Get min

If data is sorted, getting min is O(1).

#### Static data

If the input is not changing, you can just get the minimum.

#### Dynamic data

However if the input is changing (added and removed from) and you need the minimum dynamically, then a minimum state stack should be used. 
This prevents having to find the minimum everytime the data is changed.

Keep track of the minimum state at every entry of input
- input stack
- minimum state stack

Need to keep both stacks in sync. So if you push/pop from input stack you push/pop to the minimum state stack.

### Combine Linked Lists

<mark> DONT THINK OF LINKED LIST AS ARRAY</mark>

Tips:
- **Once one list runs out** you dont have to keep looping through the other! 
  - Just `new.next = list2`
  - Where `list2` is pointing to a node in the remaining list that hasnt been added yet
- Useful to have beginning be dummy node, then at the end of combining them you set head to dummy.next (the true head of the list)
  - That way you have a dedicated entry into new list

### Factorial

> `5! = 5 * 4 * 3 * 2 * 1`

A useful way of thinking of factorial sequence is that `5! = 5 * 4!`
- do you see how recursion can be used here?

```python
def factorial(num: int) -> int:
    if num == 1:
        return 1
    return num * factorial(num-1)
```

### Fibonacci

Use recursion just like factorial