from ListNode import *

L1 = ListNode(data=11)
node3 = ListNode(data=3)
node5 = ListNode(data=5)
node8 = ListNode(data=8)
node7 = ListNode(data=7)
node2 = ListNode(data=2)
insert_after(L1,node3)
insert_after(node3,node5)
insert_after(node5,node8)
insert_after(node8,node7)
insert_after(node7,node2)

def reverseSublist(head, start, end):
    # extract sublist
    dummy_head = sublist_head = ListNode(0, head)
    for _ in range(1,start):
        sublist_head = sublist_head.next

    # reverse the list
    target = sublist_head.next
    for i in range(end-start):
        temp = target.next
        # 3 way swap
        target.next, temp.next, sublist_head.next = temp.next, sublist_head.next, temp

    return dummy_head.next

L2 = reverseSublist(L1,2,4)
while L2:
    print(L2.data)
    L2 = L2.next
