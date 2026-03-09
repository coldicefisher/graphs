# graphs/core/priority_queue.py
# Based on the binary heap priority queue from
# "Graph Algorithms the Fun Way" by Jeremy Kubica


class PriorityQueue:
    def __init__(self, size=100, min_heap=True):
        self.array_size = size
        self.heap_array = [None] * self.array_size
        self.last_index = 0
        self.is_min_heap = min_heap
        self.indices = {}

    def size(self):
        return self.last_index

    def is_empty(self):
        return self.last_index == 0

    def in_queue(self, value):
        return value in self.indices

    def get_priority(self, value):
        if value not in self.indices:
            return None
        index = self.indices[value]
        return self.heap_array[index][0]

    def _elements_inverted(self, parent, child):
        if parent < 1 or parent > self.last_index:
            return False
        if child < 1 or child > self.last_index:
            return False
        if self.is_min_heap:
            return self.heap_array[parent][0] > self.heap_array[child][0]
        else:
            return self.heap_array[parent][0] < self.heap_array[child][0]

    def _swap(self, i1, i2):
        self.indices[self.heap_array[i1][1]] = i2
        self.indices[self.heap_array[i2][1]] = i1
        self.heap_array[i1], self.heap_array[i2] = self.heap_array[i2], self.heap_array[i1]

    def _heapify_up(self, index):
        parent = index // 2
        while parent >= 1 and self._elements_inverted(parent, index):
            self._swap(parent, index)
            index = parent
            parent = index // 2

    def _heapify_down(self, index):
        while 2 * index <= self.last_index:
            child = 2 * index
            if child + 1 <= self.last_index and self._elements_inverted(child, child + 1):
                child = child + 1
            if self._elements_inverted(index, child):
                self._swap(index, child)
                index = child
            else:
                break

    def enqueue(self, value, priority):
        if value in self.indices:
            self.update_priority(value, priority)
            return
        self.last_index += 1
        if self.last_index >= self.array_size:
            self.heap_array.extend([None] * self.array_size)
            self.array_size *= 2
        self.heap_array[self.last_index] = (priority, value)
        self.indices[value] = self.last_index
        self._heapify_up(self.last_index)

    def dequeue(self):
        if self.is_empty():
            raise KeyError("dequeue from empty priority queue")
        result = self.heap_array[1][1]
        del self.indices[result]
        if self.last_index > 1:
            self.heap_array[1] = self.heap_array[self.last_index]
            self.indices[self.heap_array[1][1]] = 1
            self.heap_array[self.last_index] = None
            self.last_index -= 1
            self._heapify_down(1)
        else:
            self.heap_array[1] = None
            self.last_index = 0
        return result

    def update_priority(self, value, priority):
        if value not in self.indices:
            self.enqueue(value, priority)
            return
        index = self.indices[value]
        old_priority = self.heap_array[index][0]
        self.heap_array[index] = (priority, value)
        if self.is_min_heap:
            if priority < old_priority:
                self._heapify_up(index)
            else:
                self._heapify_down(index)
        else:
            if priority > old_priority:
                self._heapify_up(index)
            else:
                self._heapify_down(index)
