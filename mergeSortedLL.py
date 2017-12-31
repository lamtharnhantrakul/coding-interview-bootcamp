from ListNode import *

L1 = ListNode(data=1)
node3 = ListNode(data=3)
node7 = ListNode(data=7)
insert_after(L1,node3)
insert_after(node3,node7)

'''
while L1:
    print(L1.data)
    L1 = L1.next
'''

L2 = ListNode(data=2)
node5 = ListNode(data=5)
node6 = ListNode(data=6)

insert_after(L2,node5)
insert_after(node5,node6)

'''
while L2:
    print(L2.data)
    L2 = L2.next
'''

def mergeSortedLL(L1, L2):
    dummy_head = tail = ListNode()

    while L1 and L2:
        if L1.data < L2.data:
            tail.next, L1 = L1, L1.next
        else: # L1.data > L2.data
            tail.next, L2 = L2, L2.next
        tail = tail.next

    tail.next = L1 or L2 # tag on whatever is remaining

    return dummy_head.next

L3 = mergeSortedLL(L1, L2)
while L3:
    print(L3.data)
    L3 = L3.next
