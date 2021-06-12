class Node:    
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

def getMiddle(head: Node):
    sPtr = fPtr = head
    while(fPtr != None and fPtr.next != None):
        if (fPtr.next.next != None):
            fPtr = fPtr.next.next
            sPtr = sPtr.next
        else:
            break
    
    if (fPtr.next == None):
        return(sPtr.data)
    else:
        return([sPtr.data, sPtr.next.data])
    

def main():
    # f = Node(6)
    e = Node(5)
    # e.next = f
    d = Node(4)
    d.next = e
    c = Node(3)
    c.next = d
    b = Node(2)
    b.next = c
    a = Node(1)
    a.next = b
    header = a

    print(getMiddle(header))

main()