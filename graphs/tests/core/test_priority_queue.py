# tests/core/test_priority_queue.py

import pytest
from graphs.core.priority_queue import PriorityQueue


# Initialization

def test_initial_state():
    pq = PriorityQueue()
    assert pq.size() == 0
    assert pq.is_empty() is True
    assert pq.is_min_heap is True


def test_initial_state_max_heap():
    pq = PriorityQueue(min_heap=False)
    assert pq.is_min_heap is False


# Basic Enqueue/Dequeue

def test_enqueue_and_dequeue_single():
    pq = PriorityQueue()
    pq.enqueue("A", 5)

    assert pq.size() == 1
    assert not pq.is_empty()
    assert pq.dequeue() == "A"
    assert pq.is_empty()


def test_min_priority_ordering():
    pq = PriorityQueue()
    pq.enqueue("A", 10)
    pq.enqueue("B", 1)
    pq.enqueue("C", 5)

    assert pq.dequeue() == "B"
    assert pq.dequeue() == "C"
    assert pq.dequeue() == "A"


def test_max_heap_ordering():
    pq = PriorityQueue(min_heap=False)
    pq.enqueue("A", 10)
    pq.enqueue("B", 1)
    pq.enqueue("C", 5)

    assert pq.dequeue() == "A"
    assert pq.dequeue() == "C"
    assert pq.dequeue() == "B"


def test_in_queue():
    pq = PriorityQueue()
    pq.enqueue("X", 3)

    assert pq.in_queue("X") is True
    assert pq.in_queue("Y") is False

    pq.dequeue()
    assert pq.in_queue("X") is False


def test_get_priority():
    pq = PriorityQueue()
    pq.enqueue("A", 4)
    assert pq.get_priority("A") == 4
    assert pq.get_priority("Z") is None


# Priority Updates

def test_update_priority_decrease():
    pq = PriorityQueue()
    pq.enqueue("A", 10)
    pq.enqueue("B", 5)
    pq.update_priority("A", 1)

    assert pq.get_priority("A") == 1
    assert pq.dequeue() == "A"
    assert pq.dequeue() == "B"


def test_update_priority_increase():
    pq = PriorityQueue()
    pq.enqueue("A", 1)
    pq.enqueue("B", 5)
    pq.update_priority("A", 10)

    assert pq.dequeue() == "B"
    assert pq.dequeue() == "A"


def test_update_priority_new_item():
    pq = PriorityQueue()
    pq.update_priority("Z", 7)

    assert pq.in_queue("Z")
    assert pq.dequeue() == "Z"


def test_enqueue_existing_updates():
    pq = PriorityQueue()
    pq.enqueue("A", 10)
    pq.enqueue("A", 1)
    assert pq.get_priority("A") == 1


def test_update_priority_max_heap():
    pq = PriorityQueue(min_heap=False)
    pq.enqueue("A", 1)
    pq.enqueue("B", 5)
    pq.update_priority("A", 10)

    assert pq.dequeue() == "A"
    assert pq.dequeue() == "B"


def test_update_priority_decrease_max_heap():
    pq = PriorityQueue(min_heap=False)
    pq.enqueue("A", 10)
    pq.enqueue("B", 5)
    pq.update_priority("A", 1)

    assert pq.dequeue() == "B"
    assert pq.dequeue() == "A"


# Internal Methods

def test_elements_inverted_min_heap():
    pq = PriorityQueue()
    pq.enqueue("A", 5)
    pq.enqueue("B", 10)
    pq.enqueue("C", 3)
    # After heapify: C(3) at 1, then A(5) and B(10)
    # Test with out-of-bounds
    assert pq._elements_inverted(0, 1) is False
    assert pq._elements_inverted(1, 10) is False


def test_elements_inverted_max_heap():
    pq = PriorityQueue(min_heap=False)
    pq.enqueue("A", 5)
    pq.enqueue("B", 10)
    # In max heap, B(10) should be at root
    assert pq.dequeue() == "B"
    assert pq.dequeue() == "A"


# Edge Cases

def test_dequeue_empty_raises():
    pq = PriorityQueue()
    with pytest.raises(KeyError):
        pq.dequeue()


def test_many_items():
    pq = PriorityQueue(size=4)
    for i in range(20):
        pq.enqueue(i, 20 - i)

    for i in range(20):
        val = pq.dequeue()
        assert val == 19 - i


def test_array_resize():
    pq = PriorityQueue(size=2)
    pq.enqueue("A", 1)
    pq.enqueue("B", 2)
    pq.enqueue("C", 3)
    assert pq.dequeue() == "A"
    assert pq.dequeue() == "B"
    assert pq.dequeue() == "C"


def test_dequeue_single_element():
    pq = PriorityQueue()
    pq.enqueue("only", 42)
    assert pq.dequeue() == "only"
    assert pq.is_empty()
