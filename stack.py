class Node:
    def __init__(self, val, next_node, largest):
        self.val = val
        self.next_node = next_node
        self.largest = largest


class Stack:
    def __init__(self):
        self.head = None
        self.length = 0

    def push(self, val):
        if not self.head:
            self.head = Node(val, None, val)
        else:
            largest = max(self.head.val, val)
            self.head = Node(val, self.head, largest)

        self.length += 1

    def pop(self):
        val = self.top()
        self.head = self.head.next_node
        self.length -= 1
        return val

    def top(self):
        if not self.head:
            raise LookupError('Stack is empty')
        
        return self.head.val

    def clear(self):
        self.head = None
        self.length = 0

    def __str__(self):
        result = []
        cur = self.head
        while cur:
            if cur.next_node:
                result.extend([str(cur.val), '->'])
            else:
                result.append(str(cur.val))

            cur = cur.next_node

        return ' '.join(result)

    def get_largest(self):
        if not self.head:
            return None
        
        return self.head.largest

        

if __name__ == '__main__':
    stack = Stack()
    stack.push(10)
    assert stack.top() == 10
    assert stack.get_largest() == 10
    assert stack.length == 1
    stack.push(20)
    assert stack.length == 2
    assert stack.get_largest() == 20
    assert stack.pop() == 20
    assert stack.length == 1
    assert stack.get_largest() == 10
    stack.push(5)
    assert stack.__str__() == '5 -> 10'
    assert stack.get_largest() == 10
    stack.push(22)
    assert stack.get_largest() == 22
    assert stack.length == 3
    

    
    
    
    
    


    
