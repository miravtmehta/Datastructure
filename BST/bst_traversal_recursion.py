# Binary tree node
class Node(object):

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def preorder(root):
    if not root:
        return

    print(root.data)
    if root.left:
        preorder(root.left)
    if root.right:
        preorder(root.right)


def inorder(root):
    if not root:
        return

    if root.left:
        inorder(root.left)
    print(root.data)
    if root.right:
        inorder(root.right)


def postorder(root):
    if not root:
        return

    if root.left:
        postorder(root.left)
    if root.right:
        postorder(root.right)
    print(root.data)


if __name__ == "__main__":

    root = Node(3)
    root.left = Node(9)
    root.right = Node(20)
    # root.right.left = Node(15)
    # root.right.right = Node(7)

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

    preorder(root)
