class Node(object):
    def __init__(self, data):
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

    def reverse(self):
        previous = None
        current_node = self.head
        while current_node:
            temp = current_node
            current_node = current_node.next
            temp.next = previous
            previous = temp
        self.head = previous


node = LinkedList()
node.append(1)
node.append(10)
node.append(20)
node.display()   
node.reverse()
node.display()

