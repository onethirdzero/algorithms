# Implement an XOR linked list

“
This problem was asked by Google.

An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding `next` and `prev` fields, it holds a field named `both`, which is an XOR of the next node and the previous node. Implement an XOR linked list; it has an `add(element)` which adds the element to the end, and a `get(index)` which returns the node at index.

If using a language that has no pointers (such as Python), you can assume you have access to `get_pointer` and `dereference_pointer` functions that converts between nodes and memory addresses.
“

## Implementation

```py
class XORNode:
    def __init__(self, val, prev_ptr=get_pointer(None), next_ptr=get_pointer(None)):
        self.val = val
        self.both = prev_ptr ^ next_ptr

class XORLinkedList:
    def __init__(self, lst):
        if len(lst) == 0: return

        self.head = get_pointer(XORNode(lst[0]))

        # For the remaining elements.
        for i in range(1, len(lst)):
            self.add(lst[i])

    def add(self, elem):
        # Traverse to the end of the list.
        curr = self.head

        # Return a pointer to the next node.
        next_ptr = self.next_addr(curr, get_pointer(None))

        while next_ptr is not None:
            tmp = self.next_addr(next_ptr, curr)
            curr = next_ptr
            next_ptr = tmp

        # Add new node to the end of the list.
        XORNode(elem, curr)

    def get(self, index):
        i = 0
        curr = self.head
        next_ptr = self.next_addr(curr, get_pointer(None))

        # Traverse the list till we get to the desired index.
        while i != index:
            tmp = self.next_addr(next_ptr, curr)
            curr = next_ptr
            next_ptr = tmp
            i += 1

        return dereference_pointer(curr).val

    def next_addr(self, curr_ptr, prev_ptr):
        return curr_ptr ^ prev_ptr

    def prev_addr(self, curr_ptr, next_ptr):
        return curr_ptr ^ next_ptr

def get_pointer(n):
    # Assume these actually work in Python.
    return n

def dereference_pointer(p):
    # Assume these actually work in Python.
    return p
```

## Comments

* Because Python doesn’t have pointers, we can only mock the `&` and `*` operators that exist in C

* An XOR linked list is memory efficient because it uses 1 field to store what a doubly linked list would use 2 fields to store
	* ie. it encodes the pointers for `next` and `prev` in a single field
* It takes advantage of the fact that XOR returns the same value when applied twice
	* eg. `A XOR B XOR A == A`

* To extract the address of `next`, we need to know the address of `prev`, and vice versa
* [XOR linked list - Wikipedia](https://en.wikipedia.org/wiki/XOR_linked_list#Description)

```
A				<-> B 					<-> C <-> ...
0 xor addr(B)		addr(A) xor addr(C)		addr(B) xor addr(D)

addr(C) = both(B) xor addr(A)
		  = (addr(A) xor addr(C)) xor addr(A)
		  = addr(A) xor addr(A) addr(C)
		  = 0 xor addr(C)
		  = addr(C)
```

* Therefore, when we traverse an XOR linked list, we always need to remember the address of the previous node
* Note that we can only start traversal from the head or the tail of the list, because we always need a complementary address to derive the next or previous address from `both`

* [algorithm - How exactly does a XOR Linked list work? - Stack Overflow](https://stackoverflow.com/questions/16138998/how-exactly-does-a-xor-linked-list-work)
* The XOR of the 2 pointers will not be recognized by anything except our code
* It also slows down pointer access since we always need to do an XOR operation to recover the true pointer first
* XOR-ed pointers are also not recognized by garbage collectors - so they can’t be used in certain languages
