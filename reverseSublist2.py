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



def reverseSublist2(head, k):
    # extract sublist
    dummy_head = sublist_head = ListNode(0, head)
    target = sublist_head.next
    while target.next: # if we get to the end of the linked list, then there will be no target in the next grouping
        for _ in range(1,k): # if k = 3, we perform 2 swaps
            if target.next:
                temp = target.next
                print(temp.data, 'temp.data')
                print(sublist_head.next.data, 'sublist_head.next.data')
                print(temp.next.data,'temp.next.data')
                sublist_head.next, temp.next, target.next = temp, sublist_head.next, temp.next

    # initialize pointers for next grouping
        print(sublist_head.data, target.data)
        sublist_head = target
        target = sublist_head.next
        print(sublist_head.data, target.data)
    return dummy_head.next

def reverseSublist3(head, k):
    curr = head
    prev = None
    nex = None


print("_" * 25)
L2 = reverseSublist2(L1,3)

curr = L2
while curr:
    print(curr.data)
    curr = curr.next
