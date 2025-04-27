# Roadmap for QuickFlow3D

## 🚀 Completed Features:
- Multi-box airflow simulator.
- Window coupling between boxes.
- Obstacles (blocks, cylinders).
- Physics-based solvers (potential flow + Navier–Stokes).
- PINN scaffold and GUI integration.
- PyVista 3D visualization.
- Testing framework + GitHub CI integration.

---

## 🛤️ Planned Features:
- ✅ PINN model plug-and-play (done).
- 🔲 Add pretrained PINN model examples.
- 🔲 Surrogate model selection from GUI with preview.
- 🔲 Turbulence modeling support (e.g., LES, RANS approximations).
- 🔲 Support for moving boundary conditions.
- 🔲 Pressure-drop analysis across windows with automated reporting.
- 🔲 Config validation and schema checking.
- 🔲 Real-time 3D visualization updates (streaming visualization).
- 🔲 Export results to `.vtk`, `.npy`, or `.csv`.

---

## 🧩 Ideas for Community Contributions:
- Implement better PINN training loops.
- Add alternative solvers (FEM, FVM).
- Improve UI (add draggable obstacles, live previews).
- Additional testing for edge cases and solver benchmarking.

---

## 💡 Long-Term Vision:
- Build a library of pretrained surrogates for common box/obstacle/window layouts.
- Deploy web-based remote solver with lightweight visualization.
- Cross-platform installer (PyInstaller for Windows/Linux/Mac).
- Multi-GPU PINN training support.

---

> Have ideas? Open an issue or suggest in your PR!