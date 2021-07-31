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

    def circular_point(self):
        head = current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = head.next

    def has_cycle(self):
        fast = slow = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def detect_cycle_node(self):
        head = fast = slow = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None
        while slow != head:
            slow = slow.next
            head = head.next
        return head.data


node = LinkedList()
node.append(3)
node.append(2)
node.append(0)
node.append(4)
node.display()

node.circular_point()

print(node.detect_cycle_node())

