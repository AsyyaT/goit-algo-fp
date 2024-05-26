class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def reverse_node(self):
        prev_node = None
        current_node = self.head
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head = prev_node

    def search_element(self, data: int) -> Node:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return

    def sort(self):
        if not self.head or not self.head.next:
            return

        sorted_head = None  # Початково відсортований список порожній
        current = self.head
        while current:
            next_node = current.next

            if not sorted_head or current.data < sorted_head.data:
                # Вставка в початок відсортованого списку
                current.next = sorted_head
                sorted_head = current
            else:

                # Пошук місця для вставки відсортованого елементу
                search_node = sorted_head
                while search_node.next and search_node.next.data < current.data:
                    search_node = search_node.next
                current.next = search_node.next
                search_node.next = current

            current = next_node
        self.head = sorted_head

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def merge_sorted(self, other):
        merged_list = LinkedList()
        current_self = self.head
        current_other = other.head

        while current_self is not None and current_other is not None:
            if current_self.data <= current_other.data:
                merged_list.insert_at_end(current_self.data)
                current_self = current_self.next
            else:
                merged_list.insert_at_end(current_other.data)
                current_other = current_other.next

        while current_self is not None:
            merged_list.insert_at_end(current_self.data)
            current_self = current_self.next

        while current_other is not None:
            merged_list.insert_at_end(current_other.data)
            current_other = current_other.next

        return merged_list


if __name__ == '__main__':
    llist = LinkedList()
    llist.insert_at_beginning(5)
    llist.insert_at_beginning(10)
    llist.insert_at_beginning(15)
    llist.insert_at_end(20)
    llist.insert_at_end(25)

    print("Зв'язний список:")
    llist.print_list()
    llist.reverse_node()
    print("Зв'язний список:")
    llist.print_list()
    llist.sort()
    llist.print_list()

    llist2 = LinkedList()
    llist2.insert_at_beginning(21)
    llist2.insert_at_beginning(18)
    llist2.insert_at_beginning(3)

    merged_list = llist.merge_sorted(llist2)
    print("Об'єднаний список:")
    merged_list.print_list()
