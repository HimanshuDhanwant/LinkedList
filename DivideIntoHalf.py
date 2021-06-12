class Node:    
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

def divideLinkedListToHalf(head: Node):
    sPtr = fPtr = head
    firstDiv, secondDiv = [], []
    while(fPtr != None):
        firstDiv.append(sPtr.data)
        if (fPtr.next != None and fPtr.next.next != None):
            fPtr = fPtr.next.next
            sPtr = sPtr.next
        else:
            fPtr = None
    sPtr = sPtr.next
    while(sPtr != None):
        secondDiv.append(sPtr.data)
        sPtr = sPtr.next
    
    return [firstDiv, secondDiv]

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

    print(divideLinkedListToHalf(header))

main()