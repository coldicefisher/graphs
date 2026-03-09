"""
Chapter 15: Priority Queues
Demonstrates the binary heap priority queue from the book.
"""

from graphs.core.priority_queue import PriorityQueue


def min_heap_example():
    """Basic min-heap priority queue operations."""
    print("=== Min-Heap Priority Queue ===")
    pq = PriorityQueue()

    # Enqueue tasks with priorities (lower = higher priority)
    tasks = [("Fix bug", 1), ("Write docs", 5), ("Deploy", 3),
             ("Code review", 2), ("Meeting", 4)]

    for task, priority in tasks:
        pq.enqueue(task, priority)
        print(f"  Enqueued '{task}' with priority {priority}")

    print(f"\nQueue size: {pq.size()}")
    print(f"Is empty: {pq.is_empty()}")
    print(f"'Fix bug' in queue: {pq.in_queue('Fix bug')}")
    print(f"Priority of 'Deploy': {pq.get_priority('Deploy')}")

    print("\nDequeue order:")
    while not pq.is_empty():
        task = pq.dequeue()
        print(f"  {task}")
    print()


def max_heap_example():
    """Max-heap priority queue (highest priority first)."""
    print("=== Max-Heap Priority Queue ===")
    pq = PriorityQueue(min_heap=False)

    pq.enqueue("Bronze", 1)
    pq.enqueue("Gold", 3)
    pq.enqueue("Silver", 2)

    print("Dequeue order (highest first):")
    while not pq.is_empty():
        print(f"  {pq.dequeue()}")
    print()


def update_priority_example():
    """Demonstrate updating priorities (used in Dijkstra's, Prim's)."""
    print("=== Priority Updates ===")
    pq = PriorityQueue()

    pq.enqueue("A", 10)
    pq.enqueue("B", 5)
    pq.enqueue("C", 8)
    print(f"Initial priority of A: {pq.get_priority('A')}")

    pq.update_priority("A", 1)
    print(f"Updated priority of A: {pq.get_priority('A')}")

    print(f"Dequeue (should be A now): {pq.dequeue()}")
    print(f"Dequeue: {pq.dequeue()}")
    print(f"Dequeue: {pq.dequeue()}")
    print()


def main():
    min_heap_example()
    max_heap_example()
    update_priority_example()


if __name__ == "__main__":
    main()
