from mytest1 import LinkedList


def task1_8(linked_list_1: LinkedList, linked_list_2: LinkedList):
    ans = []
    if linked_list_1.len() == linked_list_2.len():
        node1 = linked_list_1.head
        node2 = linked_list_2.head
        while node1 is not None and node2 is not None:
            ans.append(node1.value + node2.value)
            node1 = node1.next
            node2 = node2.next
    return ans
