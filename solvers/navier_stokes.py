# solvers/navier_stokes.py

import numpy as np
from scipy.ndimage import gaussian_filter

def solve(domain, obstacles, windows, inlet_velocity, direction):
    """
    Coarse Navier-Stokes solver (simplified for laminar, steady-state flow).
    
    Args:
        domain (dict): Box definitions with dimensions and airflow settings.
        obstacles (list): List of obstacles.
        windows (list): Window connections between boxes.
        inlet_velocity (float): Inlet velocity magnitude.
        direction (str): Airflow direction ('X', 'Y', 'Z').

    Returns:
        velocity_field (np.ndarray): Approximate velocity field.
        pressure_field (np.ndarray): Approximate pressure field.
    """
    print("[Navier-Stokes] Solving coarse Navier-Stokes...")

    grid_shape = (40, 40, 40)
    velocity_field = np.zeros(grid_shape + (3,))  # 3D vector field (u, v, w)
    dir_map = {'X': 0, 'Y': 1, 'Z': 2}
    main_dir = dir_map[direction]

    # Initialize uniform inlet flow
    velocity_field[..., main_dir] = inlet_velocity

    # Simulate obstacle-induced slowdown via Gaussian smoothing (simple approximation)
    if obstacles:
        for obs in obstacles:
            center = obs.get('center', (20, 20, 20))
            size = obs.get('size', (5, 5, 5))
            mask = np.zeros(grid_shape)
            x, y, z = np.indices(grid_shape)
            cx, cy, cz = center
            sx, sy, sz = size
            mask[((x - cx)**2 / sx**2 + (y - cy)**2 / sy**2 + (z - cz)**2 / sz**2) <= 1] = 1
            velocity_field[mask == 1] = 0  # Zero velocity inside obstacle

        # Smooth the field to simulate viscosity effects (very simplified)
        for i in range(3):
            velocity_field[..., i] = gaussian_filter(velocity_field[..., i], sigma=1)

    # Pressure field approximation (based on velocity magnitude)
    rho = 1.225  # Air density (kg/m^3)
    speed_squared = np.sum(velocity_field**2, axis=-1)
    pressure_field = 101325.0 - 0.5 * rho * speed_squared

    return velocity_field, pressure_field
