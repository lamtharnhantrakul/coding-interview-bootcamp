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

# Method 2 for reversing a sublist using Elements of Programming book approach
def reverseLL2(L):
    dummy_head = ListNode(0,L)

    target = dummy_head.next # target is the first node

    while target.next:  # if we are at the end, there is no node after target node
        temp = target.next

        # 3 way swap
        dummy_head.next, temp.next, target.next = temp, dummy_head.next, temp.next

    return target

def reverseSublistK(head, k):
    k_left = True # there are still `k` left nodes to reverse


    # call our function from above
    counter = 0
    while k_left:
        l_idx =
        r_idx =
        curr = reverseLL2(head, l_idx, r_idx)
