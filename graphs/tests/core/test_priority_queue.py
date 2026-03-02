# tests/core/test_priority_queue.py

import pytest
from graphs.core.priority_queue import PriorityQueue




# def setup_basic_queue(min_heap=True):
#     pq = PriorityQueue(size=10, min_heap=min_heap)

#     # Manually populate internal state for testing
#     # Using 1-based indexing
#     pq.heap_array[1] = (5, "A")
#     pq.heap_array[2] = (10, "B")
#     pq.heap_array[3] = (3, "C")

#     pq.indices = {
#         "A": 1,
#         "B": 2,
#         "C": 3
#     }

#     pq.last_index = 3
#     return pq



# def test_initial_state():
#     pq = PriorityQueue()

#     assert pq.size() == 0
#     assert pq.is_empty() is True
#     assert pq.is_min_heap is True
    
    
# def test_size_and_empty():
#     pq = PriorityQueue()

#     assert pq.is_empty() is True

#     pq.last_index = 1
#     assert pq.size() == 1
#     assert pq.is_empty() is False
    
    
    
# def test_in_queue():
#     pq = setup_basic_queue()

#     assert pq.in_queue("A") is True
#     assert pq.in_queue("Z") is False
    
    
# def test_get_priority():
#     pq = setup_basic_queue()

#     assert pq.get_priority("A") == 5
#     assert pq.get_priority("C") == 3
#     assert pq.get_priority("Z") is None
    
    
# def test_elements_inverted_min_heap():
#     pq = setup_basic_queue(min_heap=True)

#     # A(5) parent, C(3) child → 5 > 3 → inverted
#     assert pq._elements_inverted(1, 3) is True

#     # A(5) parent, B(10) child → 5 < 10 → not inverted
#     assert pq._elements_inverted(1, 2) is False
    
    
    
# def test_elements_inverted_max_heap():
#     pq = setup_basic_queue(min_heap=False)

#     # A(5) parent, B(10) child → 5 < 10 → inverted
#     assert pq._elements_inverted(1, 2) is True

#     # A(5) parent, C(3) child → 5 > 3 → not inverted
#     assert pq._elements_inverted(1, 3) is False




# def test_elements_inverted_out_of_bounds():
#     pq = setup_basic_queue()

#     assert pq._elements_inverted(0, 1) is False
#     assert pq._elements_inverted(1, 10) is False






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