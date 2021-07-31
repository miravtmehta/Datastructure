# Binary tree node
class Node(object):

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def pre_order(root):
    result = []
    stack = [root]
    while stack:
        root = stack.pop()
        result.append(root.data)
        if root.right:
            stack.append(root.right)
        if root.left:
            stack.append(root.left)
    print(result)


def inorder(root):
    stack = []
    result = []
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        result.append(root.data)
        root = root.right
    print(result)


def postorder(root):
    result = []
    stack = [root]
    while stack:
        root = stack.pop()
        result.append(root.data)
        if root.left:
            stack.append(root.left)
        if root.right:
            stack.append(root.right)
    print(result[::-1])


# ---------#---------#---------#---------#---------#---------#---------#---------#---------#---------

root = Node(24)

root.left = Node(18)
root.left.left = Node(17)
root.left.right = Node(19)

# ---- Right side -----

root.right = Node(34)
root.right.left = Node(32)
root.right.right = Node(42)

# ++++++ = FUNCTIONAL = +++++++++++

pre_order(root)  # [24, 18, 17, 19, 34, 32, 42]
inorder(root)  # [17, 18, 19, 24, 32, 34, 42]
postorder(root)  # [17, 19, 18, 32, 42, 34, 24]

# +++++++++++++++++


