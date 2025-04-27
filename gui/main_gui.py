# gui/main_gui.py

from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                               QPushButton, QLabel, QLineEdit, QComboBox, 
                               QListWidget, QFileDialog, QMessageBox)
import sys
import os
from config import *
from run_simulation import run_simulation

class QuickFlow3D_GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QuickFlow3D Airflow Simulator')
        self.resize(600, 500)
        self.domain = {'boxes': []}
        self.obstacles = []
        self.windows = []
        self.pinn_model_path = None  # For PINN model selection

        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        # Box Config
        box_config_layout = QHBoxLayout()
        self.box_count_input = QLineEdit("2")
        self.velocity_input = QLineEdit(str(DEFAULT_INLET_VELOCITY))
        self.direction_dropdown = QComboBox()
        self.direction_dropdown.addItems(DIRECTIONS)
        box_config_layout.addWidget(QLabel("Number of Boxes:"))
        box_config_layout.addWidget(self.box_count_input)
        box_config_layout.addWidget(QLabel("Inlet Velocity:"))
        box_config_layout.addWidget(self.velocity_input)
        box_config_layout.addWidget(QLabel("Direction:"))
        box_config_layout.addWidget(self.direction_dropdown)

        # Obstacles and Windows
        self.obstacle_list = QListWidget()
        add_obstacle_button = QPushButton("Add Obstacle")
        add_obstacle_button.clicked.connect(self.add_obstacle)
        self.window_list = QListWidget()
        add_window_button = QPushButton("Add Window")
        add_window_button.clicked.connect(self.add_window)

        # Solver selection
        self.solver_dropdown = QComboBox()
        self.solver_dropdown.addItems(SOLVER_OPTIONS)

        # PINN Model Selection Button
        self.model_button = QPushButton("Select PINN Model (.pt)")
        self.model_button.clicked.connect(self.select_model)

        # Run button
        run_button = QPushButton("Run Simulation")
        run_button.clicked.connect(self.run_simulation_button)

        # Layout assembly
        layout.addLayout(box_config_layout)
        layout.addWidget(QLabel("Obstacles:"))
        layout.addWidget(self.obstacle_list)
        layout.addWidget(add_obstacle_button)
        layout.addWidget(QLabel("Windows:"))
        layout.addWidget(self.window_list)
        layout.addWidget(add_window_button)
        layout.addWidget(QLabel("Solver:"))
        layout.addWidget(self.solver_dropdown)
        layout.addWidget(self.model_button)
        layout.addWidget(run_button)

        self.setLayout(layout)

    def add_obstacle(self):
        if len(self.obstacles) < OBSTACLE_LIMIT:
            self.obstacles.append({'center': (10, 10, 10), 'size': (5, 5, 5)})
            self.obstacle_list.addItem(f"Obstacle {len(self.obstacles)} at center (10,10,10)")
        else:
            QMessageBox.warning(self, "Limit Reached", f"Maximum {OBSTACLE_LIMIT} obstacles allowed.")

    def add_window(self):
        self.windows.append({'between': (0, 1), 'position': (1.0, 1.0), 'size': (1.0, 1.0)})
        self.window_list.addItem(f"Window between Box 0 and Box 1")

    def select_model(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select PINN Model (.pt)", "pinn_models/", "PyTorch Model (*.pt)")
        if file_path:
            self.pinn_model_path = file_path
            QMessageBox.information(self, "Model Selected", f"Selected PINN model:\n{file_path}")

    def run_simulation_button(self):
        try:
            box_count = int(self.box_count_input.text())
            inlet_velocity = float(self.velocity_input.text())
            direction = self.direction_dropdown.currentText()

            self.domain['boxes'] = [{'size': DEFAULT_BOX_SIZE, 'inlet_velocity': inlet_velocity, 'direction': direction}
                                    for _ in range(box_count)]

            solver_type = self.solver_dropdown.currentText()
            run_simulation(
                self.domain,
                self.obstacles,
                self.windows,
                solver_type=solver_type,
                inlet_velocity=inlet_velocity,
                direction=direction,
                pinn_model_path=self.pinn_model_path  # Pass selected model path
            )
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QuickFlow3D_GUI()
    window.show()
    sys.exit(app.exec())
