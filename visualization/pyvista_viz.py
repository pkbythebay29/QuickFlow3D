# visualization/pyvista_viz.py

import pyvista as pv
import numpy as np

def visualize(domain, obstacles, windows, velocity_field, pressure_field, inlet_velocity, direction):
    """
    Visualizes the airflow simulation results using PyVista.

    Args:
        domain (dict): Box definitions.
        obstacles (list): Obstacles in the domain.
        windows (list): Windows between boxes.
        velocity_field (np.ndarray): Velocity vector field.
        pressure_field (np.ndarray): Pressure scalar field.
        inlet_velocity (float): Inlet velocity magnitude.
        direction (str): Airflow direction.
    """
    print("[Visualization] Generating 3D visualization...")

    grid_shape = velocity_field.shape[:3]
    x = np.linspace(0, domain['boxes'][0]['size'][0], grid_shape[0])
    y = np.linspace(0, domain['boxes'][0]['size'][1], grid_shape[1])
    z = np.linspace(0, domain['boxes'][0]['size'][2], grid_shape[2])
    grid = pv.StructuredGrid(*np.meshgrid(x, y, z, indexing='ij'))

    # Add data to the grid
    grid['velocity'] = velocity_field.reshape(-1, 3)
    grid['pressure'] = pressure_field.flatten()

    # Streamlines
    streamlines = grid.streamlines('velocity', source_center=(0, 0, 0),
                                   n_points=100, source_radius=0.5,
                                   terminal_speed=1e-4)

    # Plotter setup
    plotter = pv.Plotter()
    plotter.add_mesh(grid.slice_orthogonal(), scalars='pressure', cmap='coolwarm', opacity=0.5)
    plotter.add_mesh(streamlines.tube(radius=0.01), color='blue', label='Streamlines')

    # Obstacles rendering (simple spheres or cubes)
    for obs in obstacles:
        center = obs.get('center', (1.0, 1.0, 1.0))
        size = obs.get('size', (0.5, 0.5, 0.5))
        cube = pv.Cube(center=center, x_length=size[0], y_length=size[1], z_length=size[2])
        plotter.add_mesh(cube, color='gray', opacity=0.8)

    plotter.add_scalar_bar(title='Pressure (Pa)')
    plotter.show(title="QuickFlow3D Airflow Simulation")
