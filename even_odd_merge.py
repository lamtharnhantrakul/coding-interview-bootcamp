from ListNode import *

L1 = ListNode(data=0)
node1 = ListNode(data=1)
node2 = ListNode(data=2)
node3 = ListNode(data=3)
node4 = ListNode(data=4)
node5 = ListNode(data=5)
node6 = ListNode(data=6)
node7 = ListNode(data=7)
node8 = ListNode(data=8)
insert_after(L1,node1)
insert_after(node1,node2)
insert_after(node2,node3)
insert_after(node3,node4)
insert_after(node4,node5)
insert_after(node5,node6)
insert_after(node6,node7)
insert_after(node7,node8)

def even_odd_merge(L):
    even_head = even_dummy_head = ListNode(0)
    odd_head = odd_dummy_head = ListNode(0)
    turn = 0

    while L:
        if turn: # turn=1 or odd
            odd_head.next = L
            L = L.next
            odd_head = odd_head.next
        else: # turn=0 or even
            even_head.next = L
            L = L.next
            even_head = even_head.next
        turn ^= 1

    #link odd chain to None
    odd_head.next = None

    # link even chain to odd chain
    even_head.next = odd_dummy_head.next

    # return the start of the even_dummy_head
    return even_dummy_head.next

def even_odd_merge_textbook(L):
    even_dummy_head, odd_dummy_head = ListNode(), ListNode()
    tails = [even_dummy_head, odd_dummy_head]
    turn = 0

    while L:
        tails[turn].next = L
        L = L.next
        tails[turn] = tails[turn].next
        turn ^= 1

    tails[1].next = None
    tails[0].next = odd_dummy_head.next

    return even_dummy_head.next


L2 = even_odd_merge_textbook(L1)

string = ''
while L2:
    string = string + str(L2.data)  # append letter at the end
    L2 = L2.next
print(string)
