from collections import deque



class Queue():
    def __init__(self):
        self.stack_a = deque([])
        self.stack_b = deque([])

    def enqueue(self, x):
        self.stack_a.append(x)

    def dequeue(self):
        len_stack_b = len(self.stack_b)
        if (len_stack_b > 0):
            return self.stack_b.pop();
        else:
            len_stack_a = len(self.stack_a)
            i = 0
            while (len_stack_a > i ):
                if (len_stack_a - 1) != i:
                    self.stack_b.append(self.stack_a.pop())
                else:
                    return self.stack_a.pop();

                i += 1



def test_case():
    q = Queue()
    for i in range(10):
        q.enqueue(i)

    print 'stack_a', q.stack_a
    print 'stack_b', q.stack_b

    q.dequeue()

    print 'stack_a', q.stack_a
    print 'stack_b', q.stack_b
    test_ary = range(10)
    test_ary.reverse()
    test_ary.pop()

    assert q.stack_b == deque(test_ary)

