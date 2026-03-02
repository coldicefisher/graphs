# graphs/core/priority_queue.py

import heapq


class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.entry_finder = {}  # item -> [priority, item]
        self.REMOVED = "<removed>"
        self.counter = 0

    def enqueue(self, item, priority: float):
        if item in self.entry_finder:
            self.update_priority(item, priority)
            return

        entry = [priority, self.counter, item]
        self.counter += 1
        self.entry_finder[item] = entry
        heapq.heappush(self.heap, entry)

    def update_priority(self, item, priority: float):
        if item not in self.entry_finder:
            self.enqueue(item, priority)
            return

        old_entry = self.entry_finder.pop(item)
        old_entry[-1] = self.REMOVED

        new_entry = [priority, self.counter, item]
        self.counter += 1
        self.entry_finder[item] = new_entry
        heapq.heappush(self.heap, new_entry)

    def dequeue(self):
        while self.heap:
            priority, _, item = heapq.heappop(self.heap)
            if item is not self.REMOVED:
                del self.entry_finder[item]
                return item
        raise KeyError("pop from empty priority queue")

    def is_empty(self) -> bool:
        return not self.entry_finder

    def in_queue(self, item) -> bool:
        return item in self.entry_finder

    def get_priority(self, item) -> float:
        return self.entry_finder[item][0]



# class PriorityQueue:
#     def __init__(self, size: int=100, min_heap: bool=True):
#         self.array_size: int = size
#         self.heap_array: list = [None] * self.array_size
#         self.last_index: int = 0
#         self.is_min_heap: bool = min_heap
#         self.indices: dict = {}
        
        
#     def size(self) -> int:
#         return self.last_index
    
    
#     def is_empty(self) -> bool:
#         return self.last_index == 0
    
#     def in_queue(self, value) -> bool:
#         return value in self.indices
    
    
#     def get_priority(self, value) -> float:
#         if value not in self.indices:
#             return None
        
#         index: int = self.indices[value]
#         return self.heap_array[index][0]
    
#     def _elements_inverted(self, parent: int, child: int) -> bool:
#         if parent < 1 or parent > self.last_index:
#             return False
#         if child < 1 or child > self.last_index:
#             return False
        
#         if self.is_min_heap:
#             return self.heap_array[parent] > self.heap_array[child]
#         else:
#             return self.heap_array[parent] < self.heap_array[child]