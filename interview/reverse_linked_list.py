


def reverse_linked_list(node):

    previous = None
    start = True
    while (node._next):
        current = node   #find current node
        _next = node._next
        node = _next

        if previous:
            current._next = previous
        else: 
            prevous = current







