# examples/example_2box.py

from run_simulation import run_simulation
from config import DEFAULT_BOX_SIZE

if __name__ == '__main__':
    # Two boxes, airflow downward in Z direction, window between them
    domain = {
        'boxes': [
            {'size': DEFAULT_BOX_SIZE, 'inlet_velocity': 1.0, 'direction': 'Z'},
            {'size': DEFAULT_BOX_SIZE, 'inlet_velocity': 0.5, 'direction': 'Z'}
        ]
    }

    # One block obstacle inside the first box
    obstacles = [
        {'center': (10, 10, 10), 'size': (5, 5, 5)}
    ]

    # One window connecting box 0 and box 1
    windows = [
        {'between': (0, 1), 'position': (1.0, 1.0), 'size': (1.0, 1.0)}
    ]

    run_simulation(domain, obstacles, windows, solver_type='navier_stokes', inlet_velocity=1.0, direction='Z')
