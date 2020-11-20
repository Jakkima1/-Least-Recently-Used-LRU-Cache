class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    '''
        `capacity` is the number of objects it can hold.
        `head` marks the Least Recently Used objects in the cache.
        `tail` makes the Most Recently Added objects in the cache.
        Functionality:
            get(key) - Returns the value of a key, if it exists.
            put(key, val) - Creates new Node and adds it to the cache.
            insert(node) - Inserts a Node into the list.
            remove(node) - Removes a Node from the list.
            delete(key) - Deletes the key
            reset() - Clear the cache
    '''
    def __init__(self, capacity):
        self.capacity = capacity
        self.objects = {}
        self.head = Node(None, None)
        self.tail = Node(None, None)
        # Head and Tail will point to eachother, making the list circular
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        # When we get() an object, we also need to update it's hotness. In
        # other words, move it towards the tail side of the linked list.
        if key in self.objects:
            node = self.objects[key]
            self.remove(node)
            self.insert(node)
            print('Retrieved {}'.format(node.val))
            return node.val
        else:
            print('{} not found in cache!'.format(key))
            return -1

    def put(self, key, val):
        # If the key already exists in the cache, remove it first, then add it
        # again to update it's hotness.
        if key in self.objects:
            del self.objects[key]

        # Create new node and insert it at the tail (most recently used)
        node = Node(key, val)
        self.insert(node)
        self.objects[key] = node

        # Check the capacity. If over capacity, remove the LRU node from the
        # list and the hashmap
        if len(self.objects) > self.capacity:
            lru_node = self.head.next
            self.remove(lru_node)
            del self.objects[lru_node.key]

        print('Added {}:{} to cache'.format(key, val))

    def insert(self, node):
        # We will insert new nodes at the tail
        prev = self.tail.prev
        if prev:
            prev.next = node
        else:
            self.tail.prev = node
        node.prev = prev
        self.tail.prev = node
        node.next = self.tail

    def remove(self, node):
        # Remove from the head (least recently used)
        prev = node.prev
        next = node.next
        if prev:
            prev.next = next
        next.prev = prev

    def delete(self,key):
        if key in self.objects:
            del self.objects[key]
        temp=self.head
        prev=None;
        while temp is not None :
            if(temp.key==key):
                break
            prev=temp;
            temp=temp.next;
        prev.next = temp.next
        if(temp.next is not None):
            temp.next.prev=prev
            temp.next=None
            temp.prev=None
        print("Deleted {}".format(key))

    def reset(self):
        self.objects.clear()
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        print("Successfully Reset ")

    def print(self):
        # Prints all objects in the cache (for testing, mainly)
        for key, node in self.objects.items():
            print('{}: {}'.format(key, node.val))




