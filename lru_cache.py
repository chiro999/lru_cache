class Node:
    def __init__(self, value=None, next_node=None, prev_node=None):
        self.value = value
        self.next = next_node
        self.prev = prev_node

head = None
tail = None
temp = None

def add_node(value):
    global head, tail, temp
    if head is None:
        head = Node(value)
        tail = head
        head.prev = None
    else:
        temp = tail
        tail.next = Node(value)
        tail = tail.next
        tail.prev = temp
    tail.next = None
    return 0

def display():
    global head, temp
    if head is None:
        print("Add a node first")
        return -2
    else:
        temp = head
        while temp is not None:
            print(f"[{temp.value}]->", end="")
            temp = temp.next
        print("NULL")
    return 0

def search_cache(value):
    global head, temp
    if head is None:
        print("Add a node first")
        return -1
    temp = head
    while temp is not None:
        if temp.value == value:
            while temp != head:
                temp.value = temp.prev.value
                temp = temp.prev
            head.value = value
            return 0
        temp = temp.next
    temp = tail.prev
    while temp is not None:
        temp.next.value = temp.value
        temp = temp.prev
    head.value = value
    return 0

def create_nodes(number):
    global status
    for i in range(number):
        status = add_node(0)
        if status < 0:
            print("Could not assign node")
            return status
    return 0

def free_cache(number):
    global head, tail, temp
    temp = head
    while temp is not None:
        head = head.next
        del temp
        temp = head
    tail = None
    return 0

def lru_operations(values, n):
    global status
    for i in range(n):
        status = search_cache(values[i])
        if status < 0:
            exit(1)
        status = display()

if __name__ == '__main__':
    CACHE_CAPACITY = 5
    status = create_nodes(CACHE_CAPACITY)
    n = 10
    values = [1, 2, 3, 4, 5, 2, 10, 7, 11, 1]
    lru_operations(values, n)
    free_cache(CACHE_CAPACITY)
