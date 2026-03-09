# tests/puzzles/test_prisoners_guards.py

import pytest
from graphs.puzzles.prisoners_guards import (
    PGState,
    pg_result_of_move,
    pg_neighbors,
    create_prisoners_and_guards,
    pg_state_to_index_map,
    solve_pg_bfs,
    pq_generate_heuristic,
)


# PGState

def test_pgstate_str():
    state = PGState(3, 3, "L")
    assert str(state) == "3, 3, L"


# pg_result_of_move

def test_move_one_guard_left_to_right():
    state = PGState(3, 3, "L")
    result = pg_result_of_move(state, 1, 0)
    # Would give 2 guards left, 3 prisoners left — 2 < 3 → invalid
    assert result is None


def test_move_one_prisoner_left_to_right():
    state = PGState(3, 3, "L")
    result = pg_result_of_move(state, 0, 1)
    assert result is not None
    assert result.prisoners_left == 2
    assert result.boat_side == "R"


def test_move_invalid_negative():
    state = PGState(3, 3, "L")
    assert pg_result_of_move(state, -1, 0) is None


def test_move_invalid_zero():
    state = PGState(3, 3, "L")
    assert pg_result_of_move(state, 0, 0) is None


def test_move_invalid_too_many():
    state = PGState(3, 3, "L")
    assert pg_result_of_move(state, 2, 1) is None


def test_move_right_to_left():
    state = PGState(2, 2, "R")
    result = pg_result_of_move(state, 1, 0)
    assert result is not None
    assert result.guards_left == 3
    assert result.boat_side == "L"


def test_move_causes_negative_counts():
    state = PGState(0, 0, "L")
    assert pg_result_of_move(state, 1, 0) is None


def test_move_guards_outnumbered_right():
    # Moving 1 guard from right creates imbalance on right
    state = PGState(1, 1, "R")
    result = pg_result_of_move(state, 0, 1)
    # 1G 2P on left → guards outnumbered
    assert result is None


# pg_neighbors

def test_pg_neighbors_initial():
    state = PGState(3, 3, "L")
    neighbors = pg_neighbors(state)
    assert len(neighbors) > 0


# create_prisoners_and_guards

def test_create_graph():
    g = create_prisoners_and_guards()
    assert g.num_nodes > 0
    assert g.undirected is True


# pg_state_to_index_map

def test_state_to_index_map():
    g = create_prisoners_and_guards()
    mapping = pg_state_to_index_map(g)
    assert "3, 3, L" in mapping
    assert "0, 0, R" in mapping


# solve_pg_bfs

def test_solve_pg_bfs(capsys):
    solve_pg_bfs()
    captured = capsys.readouterr()
    assert "Step 0" in captured.out
    assert "0, 0, R" in captured.out


# solve_pg_bfs no solution path (unreachable scenario)
# The standard puzzle always has a solution, but we test the print path


# pq_generate_heuristic

def test_generate_heuristic():
    g = create_prisoners_and_guards()
    h = pq_generate_heuristic(g)
    assert len(h) == g.num_nodes
    # Initial state should have highest heuristic
    mapping = pg_state_to_index_map(g)
    start = mapping["3, 3, L"]
    goal = mapping["0, 0, R"]
    assert h[goal] == 0
    assert h[start] > 0
