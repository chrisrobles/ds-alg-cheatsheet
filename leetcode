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
        return not bool(self.head)
    
    @update_decorator
    def append(self, value: int) -> None:
        new = Node(value)
        if not self.head:
            self.head = new
        else:
            self.tail.next = new
        self.tail = new

    @update_decorator
    def appendleft(self, value: int) -> None:
        new = Node(value)
        if not self.head:
            self.tail = new
        else:
            self.head.prev = new
        self.head = new
            
    @update_decorator
    def pop(self) -> int:
        if not self.head:
            return -1
        curr = self.head
        while curr.next != self.tail:
            curr = curr.next
        self.tail = curr
        return self.tail.next.val
    @update_decorator
    def popleft(self) -> int:
        if not self.head:
            return -1
        temp = self.head.val
        self.head = self.head.next
        return temp
    def traverse(self):
        curr = self.head
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

myDeque = Deque()
print(myDeque.isEmpty())
myDeque.append(10)
print(myDeque.isEmpty())
myDeque.appendleft(20)
myDeque.popLeft()
myDeque.pop()
myDeque.pop()
myDeque.append(30)
myDeque.pop()
print(myDeque.isEmpty())