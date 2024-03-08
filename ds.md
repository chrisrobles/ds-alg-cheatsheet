# Data Structures

## RAM
Random Access Memory

![img.png](img.png)

### Address
- Stores a byte value
- 4 bytes apart 

### Bit
1's and 0's

### Byte
1 byte = 8 bits

### Hexadecimal
1 hex = 4 bits

2 hex = 8 bits = 1 byte

## Array
Ordered, contiguous group of elements.

### Static Arrays
Cannot change size after initialization in *strictly typed languages*.
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
Can change size in *loosely typed languages*.
- Python
- JS

