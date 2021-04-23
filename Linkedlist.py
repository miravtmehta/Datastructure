class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.headexist():
            self.head = Node(data)
        else:
            curr_node = self.head
            while curr_node.next is not None:
                curr_node = curr_node.next
            curr_node.next = Node(data)

    def get_data_of_index(self, index):
        if index >= self.total_length():
            raise Exception
        count = 0
        cur_node = self.head
        while True:
            if index == count:
                return cur_node.data
            count = count + 1
            cur_node = cur_node.next

    def delete_data(self, data):
        if not self.headexist():
            return Exception
        curr_node = self.head
        if curr_node.data == data:
            self.head = curr_node.next
            return
        while curr_node is not None:
            pre_node = curr_node
            curr_node = pre_node.next
            if curr_node.data == data:
                pre_node.next = curr_node.next
                return

    def display(self):
        element = ''
        if self.headexist():
            cur_node = self.head
            while cur_node is not None:
                element += (str(cur_node.data) + '-->')
                cur_node = cur_node.next
        print(element)

    def total_length(self):
        total = 0
        if self.headexist():
            cur_node = self.head
            while cur_node is not None:
                total = total + 1
                cur_node = cur_node.next
        return total

    def reverse(self):
        previous = None
        current = self.head
        while current is not None:
            temp = current
            current = current.next
            temp.next = previous
            previous = temp
        self.head = previous

    def headexist(self):
        return 0 if not self.head else 1

    def clear(self):
        self.head = None
        return True

    def alternate(self):
        elements = ''
        curr_node = self.head
        while curr_node:
            elements += str(curr_node.data) + '-->'
            if curr_node.next:
                curr_node = curr_node.next.next
            else:
                curr_node = None
        print(elements)

    def odd_even(self):
        odd = self.head
        even = self.head.next
        evenhead = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = evenhead


if __name__ == '__main__':
    my_list = LinkedList()
    my_list.append(1)
    my_list.append(2)
    my_list.append(3)
    my_list.append(4)
    my_list.append(5)
    my_list.append(6)
    my_list.display()
    my_list.odd_even()
    my_list.display()

# Ref : https://www.youtube.com/watch?v=XDO6I8jxHtA