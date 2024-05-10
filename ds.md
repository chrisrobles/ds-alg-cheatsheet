# Data Structures

- [ ] Find best way to implement in Python 3

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
0xA3

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

Worst case would be deleting from the beginning, which would require n-1 shifts ( O(n) ).

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
- PHP
- JS

#### Complexity

| Read | Insertion                                                        | Deletion                                                              |
|------|------------------------------------------------------------------|-----------------------------------------------------------------------|
| O(1) | Ends: Amortized O(1)<br/>Middle: O(n) | Ends: Amortized O(1)<br/>Middle: O(n) |

> Amortized - average time per operation
> > Use to ensure the average performance is acceptable, even if some individual operations might take longer

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

LIFO - Last in First out

*use list*

<mark>Stack should be empty at end to be valid</mark>

Useful to:
- reverse sequences
  - recursion goes in reverse because it pops off the call stack
- Pre / Post Order Operations (56+)
- Work on to do list by starting with smallest task

### Operations & Complexity

| Push       | Pop             | Peek          |
|------------|-----------------|---------------|
| Add to top | Remove from top | Read from top |
| O(1)       | O(1)            | O(1)          |

## Linked List

Ordered sequence of nodes w/ a value and next pointer
- stored randomly in memory

<mark> DONT THINK OF A LINKED LIST AS AN ARRAY</mark>

- focus on each node as an individual

### Complexity

| Read | Insert | Delete |
|------|--------|--------|
| O(n) | O(1)   | O(1)   |

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

### Time Complexity
Access: O(n)
Search: O(n)
Insertion at known: O(1)
Deletion at known: O(1)

### Example
```python

def update_decorator(func):
    def wrapper(linked_list_instance, *args, **kwargs):
        print(f"{func.__name__}({', '.join(map(str, args))}) ")
        # Call the original method (like 'add' or 'remove')
        result = func(linked_list_instance, *args, **kwargs)
        
        # After calling the original method
        linked_list_instance.traverse()
        
        return result
    return wrapper
class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.length:
            return -1
        i = 0
        curr = self.head
        while i != index:
            i += 1
            curr = curr.next
        return curr.val
    
    @update_decorator
    def addAtHead(self, val: int) -> None:
        new = Node(val)
        new.next = self.head
        if not self.length:
            self.tail = new
        else:
            self.head.prev = new
        self.head = new
        self.length += 1
    
    @update_decorator
    def addAtTail(self, val: int) -> None:
        new = Node(val)
        new.prev = self.tail
        if not self.length:
            self.head = new
        else:
            self.tail.next = new
        self.tail = new
        self.length += 1
    
    @update_decorator
    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.length:
            return
        if(index == 4 and val == 3):
            print(self.length)
        if index == self.length:
            self.addAtTail(val)
            return
        if index == 0:
            self.addAtHead(val)
            return

        i = 0
        curr = self.head
        
        while i != index:
            i += 1
            curr = curr.next
        new = Node(val)
        new.next = curr
        new.prev = curr.prev
        new.prev.next = new
        curr.prev = new
        self.length += 1
    
    @update_decorator
    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.length:
            return
        i = 0
        curr = self.head
        while i != index:
            i += 1
            curr = curr.next
        if curr.prev:
            curr.prev.next = curr.next
        else:
            self.head = curr.next
        if curr.next:
            curr.next.prev = curr.prev
        else:
            self.tail = curr.prev
        curr.prev = None
        curr.next = None
        self.length -= 1
        
    def traverse(self) -> None:
        curr = self.head
        print(self.length, end=" ")
        while curr:
            extra = ""
            if(curr == self.head):
                extra += "H"
            if(curr == self.tail):
                extra += "T"
            print(extra + str(curr.val),end="->")
            curr = curr.next
        print("")

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

obj = MyLinkedList()
obj.addAtHead(0)
obj.addAtIndex(1,4)
obj.addAtTail(8)
obj.addAtHead(5)
obj.addAtIndex(4,3)
obj.addAtTail(0)
obj.addAtTail(5)
obj.addAtIndex(6,3)
obj.deleteAtIndex(7)
obj.deleteAtIndex(5)
obj.addAtTail(4)
```

## Queues

FIFO | "First come first serve"

*use linked list*

<mark>Queue should be empty at end to be valid</mark>

Useful for:
- Removing from the beginning O(1)
  - Arrays cant do that because it would need to shift everything
- breadth first search

### Enqueue - O(1)
Enter queue at `tail`

```python
def enqueue(self, val):
    newNode = ListNode(val)

    # Queue is non-empty
    if self.right:
        self.right.next = newNode
        self.right = self.right.next
    # Queue is empty
    else:
        self.left = self.right = newNode
```

### Dequeue - O(1)
Remove from queue at `head`
- Check it's not empty first

```python
def dequeue(self):
    # Queue is empty
    if not self.left:
        return None
    
    # Remove left node and return value
    val = self.left.val
    self.left = self.left.next
    if not self.left:
        self.right = None
    return val
```

## Deque | "deck"
Double-ended queue

Add and remove from both ends

```python
def update_decorator(func):
    def wrapper(deque_instance, *args, **kwargs):
        print(f"{func.__name__}({', '.join(map(str, args))}) ")
        # Call the original method (like 'add' or 'remove')
        result = func(deque_instance, *args, **kwargs)
        
        # After calling the original method
        deque_instance.traverse()
        
        return result
    return wrapper
class Deque: 
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self) -> bool:
        if not self.head:
            return True
        return False
    
    @update_decorator
    def append(self, value: int) -> None:
        new = Node(value)
        if self.isEmpty():
            self.head = new
            self.tail = new
            return
        self.tail.next = new
        new.prev = self.tail
        self.tail = new
        
    @update_decorator
    def appendLeft(self, value: int) -> None:
        new = Node(value)
        if self.isEmpty():
            self.head = new
            self.tail = new
            return
        self.head.prev = new
        new.next = self.head
        self.head = new
        
    @update_decorator
    def pop(self) -> int:
        if self.isEmpty():
            return -1
        temp = self.tail.value
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        return temp
    
    @update_decorator
    def popLeft(self) -> int:
        if self.isEmpty():
            return -1
        temp = self.head.value
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        return temp
    
    def traverse(self) -> None:
        curr = self.head
        while curr:
            extra = ""
            if(curr == self.head):
                extra += "H"
            if(curr == self.tail):
                extra += "T"
            print(extra + str(curr.value),end="->")
            curr = curr.next
        print("")
        
class Node:
    def __init__(self, val):
        self.value = val
        self.next = None
        self.prev = None
       
myDeq = Deque() 
myDeq.isEmpty()
myDeq.append(10)
myDeq.isEmpty()
myDeq.appendLeft(20)
myDeq.popLeft()
myDeq.pop()
myDeq.pop()
myDeq.append(30)
myDeq.pop()
myDeq.isEmpty()
```

## Binary Tree

### Time Complexity

1) 1st level is 1 node, 2nd level is 2 nodes, 3rd level there is 4 nodes.
2) The pattern is the number of nodes is 2x / **doubles** the previous level
3) Double each at each level means multiple by 2 at each level which means **2^n**
4) Since we have to traverse to the last level, it is **O(n)**
