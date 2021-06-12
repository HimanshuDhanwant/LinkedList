class Node:    
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

def reverseToStack(head: Node):
    stack = []
    tmp = head
    while(tmp != None):
        stack.append(tmp.data)
        tmp = tmp.next
    return stack
    
def checkForPalindrome(head: None) -> bool:
    stack = reverseToStack(head)
    tmp = head
    while(tmp != None):
        poppedElem = stack.pop()
        if tmp.data != poppedElem:
            return False
        else: 
            tmp = tmp.next
    return True

def main():
    f = Node(1)
    e = Node(2)
    e.next = f
    d = Node(3)
    d.next = e
    c = Node(3)
    c.next = d
    b = Node(2)
    b.next = c
    a = Node(1)
    a.next = b
    header = a

    print(checkForPalindrome(header))

main()