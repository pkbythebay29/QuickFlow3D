# tests/test_config.py

from config import BOX_LIMIT, OBSTACLE_LIMIT, SOLVER_OPTIONS

def test_config_values():
    assert BOX_LIMIT > 0
    assert OBSTACLE_LIMIT > 0
    assert 'navier_stokes' in SOLVER_OPTIONS
    assert 'potential_flow' in SOLVER_OPTIONS
