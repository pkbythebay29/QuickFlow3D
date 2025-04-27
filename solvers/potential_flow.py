# solvers/potential_flow.py

import numpy as np

def solve(domain, obstacles, windows, inlet_velocity, direction):
    """
    Simplified potential flow solver for multi-box airflow.

    Args:
        domain (dict): Box definitions with dimensions and airflow settings.
        obstacles (list): List of obstacles.
        windows (list): Window connections between boxes.
        inlet_velocity (float): Inlet velocity magnitude.
        direction (str): Airflow direction ('X', 'Y', 'Z').

    Returns:
        velocity_field (np.ndarray): Dummy uniform velocity field.
        pressure_field (np.ndarray): Simplified pressure field.
    """
    print("[Potential Flow] Solving potential flow...")

    # Assuming a coarse uniform grid across the entire domain
    grid_shape = (40, 40, 40)
    velocity_field = np.zeros(grid_shape + (3,))  # 3D vector field (u, v, w)

    # Set uniform velocity according to direction
    dir_map = {'X': 0, 'Y': 1, 'Z': 2}
    velocity_field[..., dir_map[direction]] = inlet_velocity

    # Simplified pressure field using Bernoulli principle: p = p0 - 0.5 * rho * v^2
    rho = 1.225  # Air density (kg/m^3)
    speed_squared = np.sum(velocity_field**2, axis=-1)
    pressure_field = 101325.0 - 0.5 * rho * speed_squared  # Atmospheric pressure minus dynamic pressure

    return velocity_field, pressure_field
