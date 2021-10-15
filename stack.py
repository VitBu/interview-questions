class Node:
    def __init__(self, val, next_node, largest):
        self.val = val
        self.next_node = next_node
        self.largest = largest


class Stack:
    def __init__(self):
        self.head = None

    def add(self, val):
        if not self.head:
            self.head = Node(val, None, val)
        else:
            largest = max(self.head.val, val)
            self.head = Node(val, self.head, largest)

    def pop(self):
        
        
        val = self.head.val
        self.head = self.head.next_node
        return val

    def top(self):
        if not self.head:
            return None
        
        return self.head.val

    def clear(self):
        self.head = None

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
    stack.add(10)
    assert stack.top() == 10
    assert stack.get_largest() == 10
    stack.add(20)
    assert stack.get_largest() == 20
    assert stack.pop() == 20
    assert stack.get_largest() == 10
    stack.add(5)
    assert stack.__str__() == '5 -> 10'
    assert stack.get_largest() == 10
    stack.add(22)
    assert stack.get_largest() == 22
    

    
    
    
    
    


    
