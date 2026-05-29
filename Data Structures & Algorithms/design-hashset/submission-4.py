class ListNode:
    def __init__(self, next=None, value=0):
        self.next = next
        self.value = value

class MyHashSet:

    def __init__(self):
        self.hashset = [None for _ in range(10000 + 1)]
        
    def add(self, key: int) -> None:
        val = key
        key = key % 10000
        if self.hashset[key] is None:
            self.hashset[key] = ListNode(value=val)
        else:
            addNode = ListNode(value=val)
            curr = self.hashset[key]

            duplicate = False
            prev = None
            while curr is not None:
                if curr.value == val:
                    duplicate = True
                    break
                prev = curr
                curr = curr.next

            if duplicate is False:
                prev.next = addNode


    def remove(self, key: int) -> None:
        val = key
        key = key % 10000
        if self.hashset[key] is not None:
            curr = ListNode()
            curr.next = self.hashset[key]

            if curr.next.value == val:
                self.hashset[key] = curr.next.next
            else:

                while curr.next is not None:
                    if curr.next.value == val:
                        curr.next = curr.next.next
                        break
                    
                    curr = curr.next

    def contains(self, key: int) -> bool:
        val = key
        key = key % 10000
        if self.hashset[key] is not None:
            curr = self.hashset[key]
            while curr is not None:
                if curr.value == val:
                    return True
                
                curr = curr.next
        else:
            return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)