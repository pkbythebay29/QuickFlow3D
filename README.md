# QuickFlow3D 🚀  
**Fast, Modular Airflow Simulator with Physics Solvers, PINN Integration, and 3D Visualization**

![CI](https://github.com/yourusername/QuickFlow3D/actions/workflows/ci.yml/badge.svg)

---

## 🌟 Features
- ✅ **Multi-box airflow simulation** with configurable box sizes and directions.
- ✅ **Obstacle placement** (blocks and cylinders, up to 10 per box).
- ✅ **Window openings between boxes** (define position and size).
- ✅ **Physics-based solvers:**
  - Coarse Navier–Stokes (steady-state laminar).
  - Potential Flow solver (fast approximation).
- ✅ **PINN / Machine Learning surrogate model support:**
  - Use pretrained PyTorch PINN models.
  - GUI allows easy model selection (.pt file).
- ✅ **3D interactive visualization (PyVista):**
  - Pressure field mapping.
  - Streamlines.
  - Obstacle and window visualization.
- ✅ **PySide6 GUI for interactive configuration:**
  - Add/remove obstacles.
  - Define windows between boxes.
  - Choose solver type (Physics-based or PINN).
- ✅ **Plug-and-play architecture** for adding new solvers or models.
- ✅ **Testing suite with Pytest + GitHub Actions CI integration.**

## Usage

1. Install dependencies:

pip install -r requirements.txt


2. Run an example

 python examples/example_2box.py

3. Or launch the GUI:

##Structure

solvers/: Solver backends (potential flow, Navier–Stokes)

gui/: PySide6 GUI for box/obstacle setup

visualization/: 3D visualization tools

examples/: Example case


## Usage with trained PINN

(Optional) If using a trained PINN:

    Place your .pt model into the pinn_models/ folder.

    GUI will allow selecting it at runtime.

🤝 Contributing

    Fork the repo and create your feature branch:
    git checkout -b feature/my-new-feature

    Commit your changes:
    git commit -am 'Add new feature'

    Push to the branch:
    git push origin feature/my-new-feature

    Open a pull request.
	
	
	📌 Roadmap

    ✅ PINN scaffold integration (done).

    🔲 Optional pretrained PINN model library.

    🔲 Support for unstructured grid geometries.

    🔲 Extended boundary conditions (moving inlet/outlet).

    🔲 Model evaluation metrics and pressure drop analytics