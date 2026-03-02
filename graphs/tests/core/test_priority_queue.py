# tests/core/test_priority_queue.py

import pytest
from graphs.core.priority_queue import PriorityQueue



# Basic Behavior


def test_enqueue_and_dequeue_single():
    pq = PriorityQueue()
    pq.enqueue("A", 5)

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


def test_in_queue():
    pq = PriorityQueue()

    pq.enqueue("X", 3)

    assert pq.in_queue("X") is True
    assert pq.in_queue("Y") is False

    pq.dequeue()

    assert pq.in_queue("X") is False



# Priority Updates


def test_update_priority_decrease():
    pq = PriorityQueue()

    pq.enqueue("A", 10)
    pq.enqueue("B", 5)

    pq.update_priority("A", 1)

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


def test_get_priority():
    pq = PriorityQueue()

    pq.enqueue("A", 4)
    assert pq.get_priority("A") == 4

    pq.update_priority("A", 2)
    assert pq.get_priority("A") == 2



# Removal & Internal Behavior


def test_lazy_removal_behavior():
    pq = PriorityQueue()

    pq.enqueue("A", 5)
    pq.enqueue("B", 10)

    pq.update_priority("A", 1)

    # Ensure proper order despite lazy removal
    assert pq.dequeue() == "A"
    assert pq.dequeue() == "B"


def test_dequeue_empty_raises():
    pq = PriorityQueue()

    with pytest.raises(KeyError):
        pq.dequeue()



# Stability Test


def test_stability_same_priority():
    pq = PriorityQueue()

    pq.enqueue("A", 5)
    pq.enqueue("B", 5)
    pq.enqueue("C", 5)

    # Should return in insertion order due to counter
    assert pq.dequeue() == "A"
    assert pq.dequeue() == "B"
    assert pq.dequeue() == "C"