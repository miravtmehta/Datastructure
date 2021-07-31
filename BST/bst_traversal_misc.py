from collections import deque


class Node(object):

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def level(root):
    if not root:
        return []
    level = []
    parents = [root]
    new_parents = []
    final = []
    while parents:
        for _ in parents:
            level.append(root.data)
            if root.left:
                new_parents.append(root.left)
            if root.right:
                new_parents.append(root.right)
        final.append(level)
        parents = new_parents
        new_parents = []
        level = []
    print(final)


def level_using_que(root):
    if not root:
        return []
    de_que = deque([root])
    result = []
    while de_que:
        level = []
        for _ in range(len(de_que)):
            node = de_que.popleft()
            if node.left:
                de_que.append(node.left)
            if node.right:
                de_que.append(node.right)
            level.append(node.data)
        result.append(level)
    return result


def onlyleaf(root):
    if not root:
        return 0

    if not root.left and not root.right:
        print(root.data)

    if root.left:
        onlyleaf(root.left)

    if root.right:
        onlyleaf(root.right)


def sysmetric(root):
    def istrue(L, R):
        if not L and not R:
            return True
        if L and R and L.data == R.data:
            return istrue(L.left, R.right) and istrue(R.right, L.left)
        else:
            return False

    return istrue(root.left, root.right)


def zigzag(root):
    if root is None:
        return []
    parents = deque([root])
    final = []
    rev = False
    while parents:
        level = []
        for i in range(len(parents)):
            root = parents.popleft()
            if root.left:
                parents.append(root.left)
            if root.right:
                parents.append(root.right)
            level.append(root.data)
        if rev:
            level = level[::-1]
        rev = not rev
        final.append(level)
    return final


def inverse(root):
    if root:
        root.left, root.right = inverse(root.right) , inverse(root.left)

    return root


def inverse_stack(root):
    if not root:
        return []
    stack = []
    while stack:
        root = stack.pop()
        if root:
            root.left, root.right = root.right, root.left
            stack += root.left, root.right
    return root


def isSameTree_stack(p, q):
    stack = [(p, q)]
    while stack:
        n1, n2 = stack.pop()
        if n1 and n2 and n1.val == n2.val:
            stack.append((n1.right, n2.right))
            stack.append((n1.left, n2.left))
        elif not n1 and not n2:
            continue
        else:
            return False
    return True


def isSameTree(p, q):
    if p and q:
        return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
    else:
        return p == q


def inverse(root):
    if not root:
        return []
    stack = []
    while stack:
        root = stack.pop()
        if root:
            root.left, root.right = root.right, root.left
            stack += root.left, root.right
    return root

if __name__ == "__main__":
    root = Node(24)
    root.left = Node(18)
    root.left.left = Node(17)
    root.left.right = Node(19)
    root.right = Node(34)
    root.right.left = Node(32)
    root.right.right = Node(42)

    # root = Node(1)
    # root.left = Node(2)
    # root.left.left = Node(3)
    # root.left.right = Node(4)
    # root.left.left.left = Node(5)
    # root.left.left.right = Node(6)
    # root.left.right.left = Node(7)
    # root.left.right.right = Node(8)
    #
    # root.right = Node(2)
    # root.right.right = Node(3)
    # root.right.left = Node(4)
    # root.right.right.right = Node(5)
    # root.right.right.left = Node(6)
    # root.right.left.right = Node(7)
    # root.right.left.left = Node(8)
    print(level_using_que(root))
