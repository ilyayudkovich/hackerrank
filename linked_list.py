class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Solution:
    def display(self, head):
        current = head
        while current:
            print(current.data)
            current = current.next
    def insert(self, head, data):
        if not head:
            head = Node(data)
            return head

        current = head
        while current.next:
            current = current.next

        current.next = Node(data)
        return head


mylist = Solution()
T = 4
arr = [2, 3, 4, 1]
head = None
for i in range(T):
    data = arr[i]
    head=mylist.insert(head, data)
mylist.display(head)

        
