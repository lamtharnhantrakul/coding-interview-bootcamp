from ListNode import *

L1 = ListNode(data=1)
node2 = ListNode(data=2)
node3 = ListNode(data=3)
node4 = ListNode(data=4)
node5 = ListNode(data=5)
node6 = ListNode(data=6)
node7 = ListNode(data=7)
node8 = ListNode(data=8)
insert_after(L1,node2)
insert_after(node2,node3)
insert_after(node3,node4)
insert_after(node4,node5)
insert_after(node5,node6)
insert_after(node6,node7)
insert_after(node7,node8)

def removeLastK(L,k):
    dummy_head = ListNode(0, L) # we will return this dummy head at the end

    r_pointer = dummy_head.next
    # move the r_pointer up k steps
    for _ in range(k):
        r_pointer = r_pointer.next

    l_pointer = dummy_head
    while r_pointer:
        l_pointer, r_pointer = l_pointer.next, r_pointer.next

    l_pointer.next = l_pointer.next.next

    return dummy_head.next

L2 = removeLastK(L1,4)
curr = L2
string = ''
while curr:
    string = string + str(curr.data)
    curr = curr.next
print(string)
