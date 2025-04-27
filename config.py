# config.py

# Global configuration settings for airflow simulation

BOX_LIMIT = 5                 # Maximum number of boxes
OBSTACLE_LIMIT = 10           # Maximum number of obstacles per box

DEFAULT_BOX_SIZE = (2.0, 2.0, 5.0)  # Default dimensions (X, Y, Z) in meters
DEFAULT_INLET_VELOCITY = 1.0        # Default inlet velocity magnitude (m/s)
DEFAULT_DIRECTION = 'Z'             # Default airflow direction

# Supported airflow directions
DIRECTIONS = ['X', 'Y', 'Z']

# Solver options
SOLVER_OPTIONS = ['potential_flow', 'navier_stokes']

# Pressure and velocity field grid resolution
GRID_RESOLUTION = 40                # Coarse grid for fast computation

# Window configuration
WINDOW_DEFAULT_SIZE = (1.0, 1.0)    # Default window size (width, height) in meters
