class Node(object):
    def __init__(self, data=None, next_node=None, prev_node=None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node 

# find the node where two linked lists merge
def FindMergeNode(headA, headB):
    # keep a list of all seen nodes
    lon = []
    # iterate over all nodes of A
    while headA.next:
        # append them all to the list
        lon.append(headA)
        # move onto the next node
        headA = headA.next

    # iterate over all nodes of B
    while headB.next:
        # if node is shared between A and B
        if headB in lon:
            # return the data
            return headB.data
        # move onto next node of B
        headB = headB.next
    #return B data 
    return headB.data

# see if a linked list has a cycle
def has_cycle(head):
    # keep a track of all nodes seen
    lon = []
    # iterate over the following nodes
    while head.next:
        # if the node has been seen
        if head in lon:
        # return True - there is a cycle
            return True
        # otherwise append node to seen nodes
        lon.append(head)
        # move onto next node
        head = head.next
    # return False since seen all nodes
    return False

# sort an element into a sorted list
def sortedInsert(head, data):
    # if the head is NULL
    if not head:
        # return just this Node
        return Node(data=data)
    
    b = head
    # while there is a a head.next
    while head.next:
        # compare the data to the head's data; if it's bigger than current but smaller than next, insert it
        if data > head.data and data < head.next.data:
            # create a node object with correct pointers
            n = Node(data=data, next_node=head.next, prev_node=head)
            # ilink from next node to look back at new node
            head.next.prev = n
            # head.next = new node
            head.next = n
            return b
        # otherwise move onto the next node
        else:
            # move onto the next node
            head= head.next
    
    # only get there is there is no head.next; meaning last node
    # create a new node object with prev_node being head
    n = Node(data=data, prev_node=head)
    # update head
    head.next = n
    
    return b


# reverse a doubly linked list
def Reverse(head):
    if not head:
        return None
    
    # while there's a next node
    while head.next:
        # store a temp variable of the previous value
        temp = head.prev
        # swap next and prev
        head.prev = head.next
        head.next = temp
        # take the prev node
        head = head.prev

    # perform the final swap
    temp = head.next
    head.next = head.prev
    head.prev = temp
    
    # return the first (last) node
    return head
