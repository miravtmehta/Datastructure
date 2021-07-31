class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.head = None

    def head_exist(self):
        return 1 if self.head else 0

    def display(self):
        element = ''
        if self.head_exist():
            cur_node = self.head
            while cur_node is not None:
                element += (str(cur_node.data) + '-->')
                cur_node = cur_node.next
        print(element)

    def append(self, data):
        if not self.head_exist():
            self.head = Node(data)
        else:
            currnet_node = self.head
            while currnet_node.next is not None:
                currnet_node = currnet_node.next
            currnet_node.next = Node(data)

    def delete(self, data):
        if not self.head_exist():
            return None
        current_node = self.head
        if current_node.data == data:
            self.head = current_node.next
            return
        while current_node:
            previous = current_node
            current_node = current_node.next
            if current_node.data == data:
                previous.next = current_node.next
                return

    def removeNthFromEnd(self, k=3):

        right = left = self.head
        for i in range(k):
            right = right.next
        if not right:
            return self.head.next

        while right.next:
            left = left.next
            right = right.next

        left.next = left.next.next


node = LinkedList()
node.append(1)
node.append(2)
node.append(3)
node.append(4)
node.append(5)
node.append(6)
node.append(7)
node.append(8)
node.display()
node.removeNthFromEnd()
node.display()
