
def balanceChecker(tree, depth):
    depth += 1

    if leaf?(tree):
        return depth
    else:
        left_depth = balanceChecker(tree.left, depth)
        right_depth = balanceChecker(tree.right, depth)
        return (left_depth + right_depth)/2

if balanceChecker > 1:
    print "not super balanced"

    print "this algorithm doesn't work"


def superBalanceChecker(tree):
    nodes = []
    depths = []

    nodes.push((tree, 0))

    while (not nodes.isEmpty()):
        node, depth = nodes.pop();

        if (not node.left and not node.right):
            if depth not in depths: depths.append(depth)
            if len(depths) > 2 or abs(depths[0] - depths[1)]) > 1:
                return False
        else:
            if node.left:  nodes.push(node.left, depth+1)
            if node.right: nodes.push(node.right, depth+1)
    return True



