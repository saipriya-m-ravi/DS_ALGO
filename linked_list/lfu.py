from collections import defaultdict


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = None


class DLL:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def insert(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.size += 1

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

    def remove_lru(self):
        if self.size == 0:
            return None
        lru = self.tail.prev
        self.remove(lru)
        return lru


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.min_freq = 0

        self.key_map = {}                # key → node
        self.freq_map = defaultdict(DLL) # freq → DLL

    def _update(self, node):
        freq = node.freq
        self.freq_map[freq].remove(node)

        if freq == self.min_freq and self.freq_map[freq].size == 0:
            self.min_freq += 1

        node.freq += 1
        self.freq_map[node.freq].insert(node)

    def get(self, key: int) -> int:
        if key not in self.key_map:
            return -1

        node = self.key_map[key]
        self._update(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.key_map:
            node = self.key_map[key]
            node.value = value
            self._update(node)
        else:
            if self.size == self.capacity:
                lru = self.freq_map[self.min_freq].remove_lru()
                del self.key_map[lru.key]
                self.size -= 1

            new_node = Node(key, value)
            self.key_map[key] = new_node
            self.freq_map[1].insert(new_node)
            self.min_freq = 1
            self.size += 1
