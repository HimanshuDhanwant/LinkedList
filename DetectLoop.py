class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

def detectLoop(head):
    sPtr, fPtr = head, head.next

    while(fPtr != None and fPtr.next != None):
        if(sPtr.data == fPtr.data):
            return "Loop detected!!"
        sPtr = sPtr.next
        fPtr = fPtr.next.next
    return "Doesn't contains a loop!!"

def main():

    # e = Node(5)
    # d = Node(4)
    # c = Node(3)
    # b = Node(2)
    # a = Node(1)
    # e.next = b
    # d.next = e
    # c.next = d
    # b.next = c
    # a.next = b
    # header = a

    b = Node(2)
    a = Node(1)
    a.next = b
    b.next = a
    print(detectLoop(a))

    # Straight LL without loop
    # e = Node(5)
    # d = Node(4)
    # c = Node(3)
    # b = Node(2)
    a = Node(1)
    # d.next = e
    # c.next = d
    # b.next = c
    # a.next = b
    header = a

    print(detectLoop(header))

main()