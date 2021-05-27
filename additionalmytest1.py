import mytest1


def delete_test():
    linkedList = mytest1.LinkedList()
    linkedList.add_in_tail(mytest1.Node(1))

    linkedList.add_in_tail(mytest1.Node(3))
    linkedList.add_in_tail(mytest1.Node(3))

    linkedList.delete(3, True)
    assert linkedList.len() == 1
    assert linkedList.head.value == 1




delete_test()
