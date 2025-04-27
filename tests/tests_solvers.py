# tests/test_solvers.py

import numpy as np
from solvers import potential_flow, navier_stokes

def test_potential_flow_solver():
    domain = {'boxes': [{'size': (2.0, 2.0, 5.0), 'inlet_velocity': 1.0, 'direction': 'Z'}]}
    obstacles = []
    windows = []
    velocity, pressure = potential_flow.solve(domain, obstacles, windows, 1.0, 'Z')
    assert isinstance(velocity, np.ndarray)
    assert isinstance(pressure, np.ndarray)
    assert velocity.shape[-1] == 3

def test_navier_stokes_solver():
    domain = {'boxes': [{'size': (2.0, 2.0, 5.0), 'inlet_velocity': 1.0, 'direction': 'Z'}]}
    obstacles = [{'center': (10, 10, 10), 'size': (5, 5, 5)}]
    windows = []
    velocity, pressure = navier_stokes.solve(domain, obstacles, windows, 1.0, 'Z')
    assert isinstance(velocity, np.ndarray)
    assert isinstance(pressure, np.ndarray)
    assert velocity.shape[-1] == 3
