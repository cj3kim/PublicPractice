from collections import deque

class Queue():
    def __init__(self):
        self.stack_a = deque([])
        self.stack_b = deque([])

    def enqueue(self, x):
        self.stack_a.append(x)

    def dequeue(self):
        if (len(self.stack_b) > 0): return self.stack_b.pop();

        i = 0
        len_stack_a = len(self.stack_a)
        last_index_stack_a = len_stack_a - 1
        while (len_stack_a > i ):
            poppedValue = self.stack_a.pop()
            if i == last_index_stack_a: return poppedValue
            self.stack_b.append(poppedValue)
            i += 1

def test_case():
    q = Queue()
    for i in range(10):
        q.enqueue(i)
    print """
        This algorith is O(n) utilizing the accounting method to compute the average time an
        element spends in the system.
    """
    print """
        Stack A is in the IN stack and Stack B is the OUT stack. We accumulate new element on
        Stack A and then pop them onto Stack B when Stack B is empty and needs more elements to dequeue.
    """
    print """
        It's important to note Stack A keeps the elements in reversed order due to stack properties,
        but the order will be correct when the reversed elements are popped onto Stack B.
    """
    print 'stack_a', q.stack_a
    print 'stack_b', q.stack_b
    q.dequeue()

    print 'stack_a', q.stack_a
    print 'stack_b', q.stack_b
    test_ary = range(10)
    test_ary.reverse()
    test_ary.pop()

    assert q.stack_b == deque(test_ary)

