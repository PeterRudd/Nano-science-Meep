# Meep Nanophotonics: From Zero to Hero 🚀

Welcome to the **most comprehensive** Meep tutorial series! Learn nanophotonics simulation using the **Jeremy Howard teaching style**: learn by doing, with clear expectations and tests, following the official Meep tutorial structure with enhanced explanations.

## What You'll Learn

- **Electromagnetic simulation** using FDTD (Finite-Difference Time-Domain) method
- **Waveguide physics**: How light is guided and manipulated in nanoscale structures
- **Advanced techniques**: Cylindrical coordinates, mode analysis, optimization
- **Practical skills**: Setup, run, analyze, and validate photonic simulations
- **Three-level understanding**: Beginner → Intermediate → Advanced

## Repository Structure

```
Nano-science-Meep/
├── lessons/
│   ├── lesson_1/          # Fields in a Waveguide
│   │   ├── README.md
│   │   ├── meep_waveguide_tutorial.ipynb
│   │   ├── meep_helpers.py
│   │   ├── quick_start.py
│   │   └── CHEATSHEET.md
│   │
│   └── lesson_2/          # Cylindrical Coordinates (Coming Soon)
│       └── README.md
│
└── README.md              # This file
```

## Lessons Overview

### 📘 Lesson 1: Fields in a Waveguide
**Status:** ✅ Complete | **Time:** 2-3 hours | **Level:** Beginner-friendly

Learn the fundamentals of Meep by simulating light propagation in waveguides.

**Topics:**
1. **A Straight Waveguide** - Field patterns from a CW source
   - Computational cell setup
   - Geometry definition with `Block` objects
   - Source configuration
   - PML boundaries
   - Field visualization

2. **A 90° Bend** (Coming Soon)
   - Bending loss analysis
   - Time-series animations

3. **Output Tips and Tricks** (Coming Soon)
   - Efficient data output
   - HDF5 format
   - Visualization techniques

**Quick Start:**
```bash
cd lessons/lesson_1
python quick_start.py
```

**Or use interactive notebook:**
```bash
cd lessons/lesson_1
jupyter notebook meep_waveguide_tutorial.ipynb
```

[📖 Go to Lesson 1](./lessons/lesson_1/README.md)

---

### 📗 Lesson 2: Cylindrical Coordinates
**Status:** 📝 In Development | **Time:** TBD | **Level:** Intermediate

Learn to exploit rotational symmetry for dramatically faster simulations.

**Topics:**
1. **Modes of a Ring Resonator** - 2D → 1D transformation
2. **Sensitivity Analysis via Perturbation Theory** - Shape optimization
3. **Scattering Cross Section of a Finite Dielectric Cylinder**
4. **Scattering from a Sphere with Oblique Planewave**
5. **Focusing Properties of a Binary-Phase Zone Plate**
6. **Nonaxisymmetric Dipole Sources**

**Prerequisites:** Complete Lesson 1

[📖 Go to Lesson 2](./lessons/lesson_2/README.md)

---

### 📙 Lesson 3: Coming Soon
More lessons will be added following the official Meep tutorial structure!

## Quick Start Guide

### Installation (5 minutes)

#### Option A: Conda (Recommended)
```bash
# Create environment
conda create -n meep python=3.10
conda activate meep

# Install Meep and dependencies
conda install -c conda-forge pymeep matplotlib numpy jupyter

# Verify installation
python -c "import meep as mp; print(f'Meep {mp.__version__} installed!')"
```

#### Option B: pip
```bash
pip install meep matplotlib numpy jupyter
```

### Run Your First Simulation (1 minute)
```bash
cd lessons/lesson_1
python quick_start.py
```

You should see:
- ✓ Simulation setup and execution
- ✓ Automated test results
- ✓ Field visualizations
- ✓ Quantitative analysis

## Learning Paths

### 🎯 Path 1: Absolute Beginner (New to Everything)
**Time commitment:** ~4-6 hours

1. Start with Lesson 1
2. Run `quick_start.py` first
3. Read **only 🟢 beginner sections** in the notebook
4. Run all code cells
5. Try **easy exercises**
6. Return later for intermediate/advanced content

**You'll learn:**
- What is electromagnetic simulation
- How waveguides work
- Basic Meep commands
- How to visualize results

### 🎯 Path 2: Physics/Engineering Background
**Time commitment:** ~6-10 hours

1. Start with Lesson 1, reading **🟢 and 🟡 sections**
2. Study the equations and theory
3. Try **medium exercises** (parameter exploration)
4. Use helper functions for validation
5. Proceed to Lesson 2
6. Apply to your own designs

**You'll learn:**
- Maxwell's equations in FDTD
- Waveguide mode theory
- Design principles and optimization
- How to validate simulations

### 🎯 Path 3: Advanced User (Experienced in EM)
**Time commitment:** ~3-5 hours

1. Skim beginner content, focus on **🔴 advanced sections**
2. Study FDTD implementation details
3. Try **hard exercises** (custom analysis, optimization)
4. Modify helper modules for your needs
5. Quickly progress through all lessons

**You'll learn:**
- Meep implementation details
- Numerical methods and stability
- Performance optimization
- Advanced analysis techniques

## Teaching Philosophy

This tutorial series follows the **fast.ai / Jeremy Howard approach**:

### Core Principles

1. **🎬 Top-down Learning**
   - Start with working code
   - See results immediately
   - Understand theory later

2. **🎯 Learn by Doing**
   - Run simulations first
   - Experiment with parameters
   - Build intuition through practice

3. **✅ Clear Expectations**
   - Know what to expect before running
   - Automated tests verify correctness
   - Immediate feedback on results

4. **📚 Progressive Disclosure**
   - Three levels: Beginner → Intermediate → Advanced
   - Choose your learning level
   - Deep dive when ready

5. **🔬 Practical First**
   - Real simulations from day one
   - Theory follows practice
   - Applications drive learning

### Why This Works

You learn faster when you:
- ✨ See immediate results (motivation!)
- 🧠 Build intuition before equations (understanding!)
- ✓ Test your knowledge (confidence!)
- 🎨 Experiment freely (creativity!)

## Three-Level Explanations

Every concept is explained at three levels:

### 🟢 Beginner: Simple Analogies
- **Audience:** No prior physics knowledge
- **Style:** Everyday examples (fiber optics, water pipes)
- **Focus:** What and why
- **Math:** Minimal

**Example:** "A waveguide is like a pipe for light. Just as water flows through a pipe, light flows through a waveguide. The high refractive index material 'contains' the light, preventing it from escaping."

### 🟡 Intermediate: Physics & Math
- **Audience:** Physics or engineering background
- **Style:** Equations, theory, analysis
- **Focus:** How and when
- **Math:** Moderate (calculus, vectors)

**Example:** "The waveguide supports confined modes when the V-number V = (πw/λ)√(n₁² - n₂²) < π/2. For our design with w=1μm and n₁=3.46, V≈1.5, ensuring single-mode operation."

### 🔴 Advanced: Implementation Details
- **Audience:** Experienced in computational EM
- **Style:** Algorithms, numerics, optimization
- **Focus:** Implementation and performance
- **Math:** Advanced (PDEs, numerical methods)

**Example:** "Meep uses the Yee lattice with staggered E and H fields. The Courant stability condition Δt ≤ Δx/(c√d) is satisfied using Δt = 0.5Δx/c. The PML uses complex coordinate stretching with σ(ρ) = σ_max(ρ/d)³."

## Key Features

### ✅ Automated Testing
Every simulation includes tests that verify:
- Physical correctness
- Numerical accuracy
- Expected behavior
- Common pitfalls

### 📊 Rich Visualizations
All tutorials include:
- Field plots with proper scaling
- Animation creation guides
- Analysis plots (mode profiles, dispersion)
- Comparison with theory

### 🛠️ Helper Utilities
Each lesson provides:
- `*_helpers.py` - Analysis and testing functions
- `quick_start.py` - Fast demo scripts
- `CHEATSHEET.md` - Quick reference
- `*.ipynb` - Interactive notebooks

### 🎓 Structured Exercises
Exercises at three levels:
- 🟢 **Easy:** Parameter exploration
- 🟡 **Medium:** Design modifications
- 🔴 **Hard:** Novel analysis and applications

## Prerequisites

### Required
- **Python 3.8+**
- **Basic Python knowledge** (variables, functions, loops)
- **Curiosity about light and optics!**

### Optional but Helpful
- Jupyter notebook familiarity
- NumPy and Matplotlib basics
- Physics background (helpful but not required!)
- Electromagnetic theory (for intermediate/advanced levels)

## System Requirements

### Minimum
- **OS:** Windows, macOS, or Linux
- **RAM:** 4 GB
- **Disk:** 2 GB free space
- **Python:** 3.8 or later

### Recommended
- **RAM:** 8+ GB (for larger simulations)
- **CPU:** Multi-core (Meep can parallelize)
- **GPU:** Not required (Meep is CPU-based)

## Common Issues

### Installation Problems

**Issue:** `conda install pymeep` fails
**Solution:** Make sure conda-forge channel is accessible:
```bash
conda config --add channels conda-forge
conda config --set channel_priority strict
```

**Issue:** `ModuleNotFoundError: No module named 'meep'`
**Solution:** Activate the correct environment:
```bash
conda activate meep
```

### Simulation Problems

**Issue:** Simulation is very slow
**Solution:**
- Reduce resolution: `resolution = 5`
- Reduce runtime: `runtime = 100`
- Use 2D instead of 3D

**Issue:** No field confinement visible
**Solution:**
- Check permittivity: `epsilon > 1`
- Verify PML is present
- Run longer: `runtime = 200`

**Issue:** "Out of memory" error
**Solution:**
- Reduce resolution
- Reduce cell size
- Use 2D simulation

## Resources

### Official Documentation
- [Meep Homepage](https://meep.readthedocs.io/)
- [Python Tutorials](https://meep.readthedocs.io/en/latest/Python_Tutorials/Basics/)
- [Python API Reference](https://meep.readthedocs.io/en/latest/Python_User_Interface/)
- [FAQ](https://meep.readthedocs.io/en/latest/FAQ/)

### Textbooks
- **Joannopoulos et al.** - "Photonic Crystals: Molding the Flow of Light"
- **Taflove & Hagness** - "Computational Electrodynamics: The FDTD Method"
- **Saleh & Teich** - "Fundamentals of Photonics"

### Online Courses
- [Photonics Boot Camp (edX)](https://www.edx.org/course/silicon-photonics)
- [fast.ai](https://www.fast.ai/) - Teaching philosophy inspiration

### Community
- [Meep Discussions](https://github.com/NanoComp/meep/discussions)
- [Meep Issues](https://github.com/NanoComp/meep/issues)
- [r/photonics](https://www.reddit.com/r/photonics/)

## Contributing

This is a learning project and contributions are welcome!

### How to Contribute
1. Found a typo or error? Open an issue
2. Have a better explanation? Submit a PR
3. Want to add exercises? Share your ideas
4. Created a cool example? Show us!

### Guidelines
- Follow the three-level explanation format
- Include tests for new examples
- Provide clear learning objectives
- Match the Jeremy Howard teaching style

## What's Next?

### Future Lessons (Planned)
- **Lesson 3:** Resonant Modes and Transmission
- **Lesson 4:** Local Density of States
- **Lesson 5:** Photonic Crystals
- **Lesson 6:** Frequency vs. Time Domain
- **Lesson 7:** Advanced Topics

### Advanced Topics (Future)
- Optimization and inverse design
- Mode decomposition
- Subpixel smoothing
- Parallel computing with MPI
- 3D simulations

## License

This educational tutorial series is free to use. Meep itself is free software licensed under GPL v2+.

## Acknowledgments

- **Meep developers** at MIT and Simpetus for the amazing software
- **Jeremy Howard** and fast.ai for the teaching philosophy
- **The photonics community** for support and feedback

---

## Quick Reference

### Meep Units
```
Distance:   μm (micrometers)
Time:       μm/c = 3.33 femtoseconds
Frequency:  c/μm = 300 THz
Wavelength: λ = 1/f (in μm)
```

### Essential Commands
```python
import meep as mp

# Geometry
geometry = [mp.Block(size=..., center=..., material=...)]

# Source
sources = [mp.Source(src=mp.ContinuousSource(frequency=...), ...)]

# PML
pml_layers = [mp.PML(thickness=1.0)]

# Simulation
sim = mp.Simulation(cell_size=..., geometry=..., sources=...,
                    boundary_layers=..., resolution=...)

# Run
sim.run(until=200)

# Get fields
ez_data = sim.get_array(center=..., size=..., component=mp.Ez)
```

### Getting Help
```bash
python -c "import meep as mp; help(mp.Simulation)"
```

---

**Ready to begin your nanophotonics journey?**

Start with **[Lesson 1: Fields in a Waveguide](./lessons/lesson_1/README.md)** 🚀

**Happy learning!** 🎉
