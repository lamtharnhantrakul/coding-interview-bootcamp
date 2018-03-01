from ListNode import *

L1 = ListNode(data=11)
node3 = ListNode(data=3)
node5 = ListNode(data=5)
node7 = ListNode(data=7)
node2 = ListNode(data=2)
insert_after(L1,node3)
insert_after(node3,node5)
insert_after(node5,node7)
insert_after(node7,node2)

# Method 1 for reversing a sublist
def reverseLL(L):
    curr = L
    prev = None
    nex = None

    while curr:
        print(curr.data)
        nex = curr.next

        curr.next = prev

        prev = curr
        curr = nex

    return prev

# Method 2 for reversing a sublist using Elements of Programming book approach
def reverseLL2(L):
    dummy_head = ListNode(0,L)

    target = dummy_head.next # target is the first node

    while target.next:  # if we are at the end, there is no node after target node
        temp = target.next

        # 3 way swap
        dummy_head.next, temp.next, target.next = temp, dummy_head.next, temp.next

    return dummy_head.next

rL = reverseLL2(L1)

print('_' * 25)
curr = rL
while curr:
    print(curr.data)
    curr = curr.next
