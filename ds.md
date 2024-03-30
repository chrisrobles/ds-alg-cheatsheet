# Data Structures

## RAM
Random Access Memory

![img.png](assets/img.png)

### Address
- Stores a byte value
- 4 bytes apart
  - Since one int is 4 bytes

### Bit
1's and 0's

### Byte
1 byte = 8 bits

### Hexadecimal
1 hex = 4 bits

2 hex = 8 bits = 1 byte

## Array
Ordered, contiguous group of elements.

Useful to:
- Access something with a known location instantly
- Add to the end of a ds(stack)

### Static Arrays
Cannot change size after initialization.

Default in *strictly typed languages*.
- Java
- C++
- C#

#### Reading - O(1)
```python
myArray = [1,3,6]
myArray[0]  # 1
```

#### Deleting
For static arrays, all array indices are filled with a default value denoting an empty array (0,null,-1).

##### From the end - O(1)
Simple as setting the end to a default empty value.

```python
arr[length-1] = 0
```
##### From the middle - O(n)
Cant set the value to a default value because it will break the contiguous order.

So we must shift everything after `i`, one index to the left.

Worst case would be deleting from the beginning, which would require n-1 shifts.

```python
def deleteMiddle(arr, i, length):
    for index in range(i, length-1):
        arr[index] = arr[index+1]
    arr[length-1] = 0
```
#### Inserting

##### At the end - O(1)
As long as the array has the capacity, can just insert at length

```python
if length < capacity:  # capacity = memory allocated for the fixed size array
    arr[length] = n
```

##### At the middle - O(n)
Shift all values >= `i` to the right

```python
def insertMiddle(arr, i, val, length):      # (arr, 1, val, 3)
    for index in range(length-1, i-1, -1):  # range(2,0,-1) = 2,1
        arr[index+1] = arr[index]           # start at index 3 because everything shifted to the right
    arr[i] = val                            # replace index 1 with new value
```

### Dynamic Arrays
Can change size. (Dont need their size specified.)

Default in *loosely typed languages*.
- Python
- JS

#### Complexity

Read: O(1)
Insertion: O(1) (O(n) if in middle but amortized O(1))
Deletion: O(1) (O(n) if in middle but amortized O(1))

#### Reallocate - O(n)
When the array gets too big for its allocation, it reallocates a bigger array (usually double) in memory. (Also it deallocates the old array.)

Reallocating happens so infrequently the O(n) time complexity for reallocating isnt really a concern. So, the amortized complexity (average) of pushing to the end of an array is still O(1).

#### Example

```python
class DynamicArray:
    
    def __init__(self, capacity: int):
        self.arr = [0] * capacity
        self.length = 0
        self.capacity = capacity

    def get(self, i: int) -> int:
        if(i < self.length):
            return self.arr[i]
        raise IndexError("Out of bounds")

    def set(self, i: int, n: int) -> None:
        if(i < self.length):
            self.arr[i] = n
        
    def pushback(self, n: int) -> None:
        if(self.length == self.capacity):
            self.resize()
        self.arr[self.length] = n
        self.length += 1

    def popback(self) -> int:
        self.length -= 1
        return self.arr[self.length]

    def resize(self) -> None:
        self.arr = self.arr + [0]*self.capacity
        self.capacity *= 2

    def getSize(self) -> int:
       return self.length

    def getCapacity(self) -> int:
        return self.capacity
```

## Stack

LIFO

Useful to:
- reverse sequences
- apply operator to previous entries (Pre / Post Order)
  - PS verify stack is empty at end to be valid

### Push - O(1)
Adds to the top

### Pop - O(1)
Removes from the top

### Peek - O(1)
Returns whats at the top

## Linked List

Ordered sequence of nodes w/ a value and next pointer
- may be ordered but stored randomly in memory

<mark> DONT THINK OF LINKED LIST AS ARRAY</mark>
- focus on each node as an individual

### Complexity

Access: O(n)
Search: O(n)
Insert at known: O(1)
Delete at known: O(1)

### List Node Example

```python
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
```

### Linked List Example
```python
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def get(self, index: int) -> int:
        cur = self.head
        if not cur:
            return -1
        while index:
            if not cur.next:
                return -1
            cur = cur.next
            index -= 1
        return cur.val
    def insertHead(self, val: int) -> None:
        new = Node(val)
        new.next = self.head
        if not self.head:
            self.tail = new
        self.head = new
    def insertTail(self, val: int) -> None:
        new = Node(val)
        if self.tail:
            self.tail.next = new
        else:
            self.head = new
        self.tail = new
        print(self.tail.val)
    def remove(self, index: int) -> bool:
        cur = self.head
        prev = None
        if not cur:
            return False
        while index:
            if not cur.next:
                return False
            prev = cur
            cur = cur.next
            index -= 1
        if prev:
            if cur == self.tail:
                self.tail = prev
            prev.next = prev.next.next
        elif self.head:
            self.head = self.head.next
        return True
    def getValues(self) -> List[int]:
        arr = []
        cur = self.head
        while cur:
            arr.append(cur.val)
            cur = cur.next
        return arr
```

## Doubly Linked List
Linked list with an added `prev` pointer

Useful to:
- build stack
- 

### Complexity
Access: O(n)
Search: O(n)
Insertion at known: O(1)
Deletion at known: O(1)

## Queues

FIFO

Implemented with linked list

Useful for:
- breadth first search for trees and graphs

### Enqueue - O(1)
Enter queue at `tail`

### Dequeue - O(1)
Remove from queue at `head`

**Check if queue is empty before removing**

## Deque | "deck"
Double-ended queue

Add and remove from both ends

## Recursion - O(n) time and space
When a function calls itself with a smaller output until a base case is reached

recursive function = 
1. base case
2. function calling itself with a different input

Useful for:
- working backwards
  - reversing
  - depth first search on trees

The O(n) space complexity comes from the method calls getting put into the call stack and if there are n method calls there are n methods in the call stack