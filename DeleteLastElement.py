class Node:    
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

def deleteLastElement(head: Node) -> Node:
    if head == None or head.next == None:
        return None
    else:
        tmp = head
        ptr, nextPtr = tmp, tmp.next
        while(nextPtr.next != None):
            ptr = nextPtr
            nextPtr = nextPtr.next

        ptr.next = None
        return tmp

def printLL(head):
    tmp = head
    while(tmp != None):
        print(tmp.data, end= ' -> ')
        tmp = tmp.next
    print("*")

def main():
    f = Node(6)
    e = Node(5)
    e.next = f
    d = Node(4)
    d.next = e
    c = Node(3)
    c.next = d
    b = Node(2)
    b.next = c
    a = Node(1)
    a.next = b
    header = a

    printLL(header)
    print("After deletion of last node: ")
    printLL(deleteLastElement(header))

main()