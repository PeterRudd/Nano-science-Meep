# Meep Waveguide Tutorial: From Zero to Hero 🚀

Welcome to the **most comprehensive** Meep waveguide tutorial! This tutorial teaches you nanophotonics simulation using the **Jeremy Howard teaching style**: learn by doing, with clear expectations and tests.

## What You'll Learn

- **Electromagnetic simulation** using FDTD (Finite-Difference Time-Domain) method
- **Waveguide physics**: how light is guided in nanoscale structures
- **Practical skills**: setup, run, analyze, and validate photonic simulations
- **Three-level understanding**: beginner → intermediate → advanced

## What's Included

```
Nano-science-Meep/
├── meep_waveguide_tutorial.ipynb   # Main interactive tutorial
├── meep_helpers.py                  # Test utilities and helper functions
├── requirements.txt                 # Python dependencies
└── README.md                        # This file
```

## Quick Start (5 minutes)

### 1. Install Dependencies

```bash
# Option A: Using conda (recommended for Meep)
conda create -n meep python=3.10
conda activate meep
conda install -c conda-forge pymeep matplotlib numpy jupyter

# Option B: Using pip (may require system dependencies)
pip install -r requirements.txt
```

### 2. Launch the Tutorial

```bash
jupyter notebook meep_waveguide_tutorial.ipynb
```

### 3. Run All Cells

Press `Shift + Enter` to run each cell, or `Cell → Run All` to run everything.

**Expected time:** ~2-3 minutes total (simulation takes ~5-10 seconds)

## What to Expect

When you run the tutorial, you'll:

1. ✅ **Import Meep** and verify installation
2. 🔲 **Define simulation space** (16 μm × 8 μm box)
3. 📦 **Create waveguide** (1 μm wide, silicon-like material)
4. 💡 **Add light source** (near-infrared frequency)
5. 🌊 **Add absorbing boundaries** (PML layers)
6. 🚀 **Run simulation** (~5 seconds)
7. 📊 **Visualize results** (see light confined in waveguide!)
8. ✓ **Run automated tests** (verify everything works)

## Tutorial Structure

The notebook is organized into **8 steps**, each with:

### 🎯 What to Expect
Clear statement of what will happen when you run the code.

### 💻 Code Cell
Working code that you can run immediately.

### 📚 Understanding at Three Levels

#### 🟢 **Beginner**: Simple analogies and intuitive explanations
- No prior physics knowledge required
- Uses everyday examples (fiber optic cable, water pipes)
- Focus on "what" and "why"

#### 🟡 **Intermediate**: Physics and mathematics
- Maxwell's equations and waveguide theory
- Quantitative analysis (V-number, mode profiles)
- Design principles and rules of thumb

#### 🔴 **Advanced**: Implementation details
- FDTD algorithm (Yee lattice, Courant condition)
- Numerical methods (PML, dispersion, stability)
- Performance optimization and parallelization

**Choose your level!** Read all three, or just the one that matches your background.

## Using the Helper Module

The `meep_helpers.py` file provides utilities for testing and analysis:

### Quick Simulation

```python
from meep_helpers import quick_waveguide_simulation

# Run simulation with one line!
results = quick_waveguide_simulation(width=1.0, frequency=0.15)

# Print test report
results['tests'].print_report()
```

### Individual Tests

```python
from meep_helpers import WaveguideTests
import numpy as np

tests = WaveguideTests()

# Test single-mode condition
tests.test_single_mode_condition(
    width=1.0,           # 1 μm wide
    wavelength=6.67,     # 6.67 μm vacuum wavelength
    n_core=3.46          # Silicon-like refractive index
)

# Print results
tests.print_report()
```

### Analysis Tools

```python
from meep_helpers import WaveguideAnalysis

# Calculate effective index
n_eff = WaveguideAnalysis.calculate_effective_index(
    field_data, cell_size, wavelength
)

# Measure decay length
delta = WaveguideAnalysis.measure_decay_length(
    field_data, waveguide_width, cell_size
)

# Plot mode profile
WaveguideAnalysis.plot_mode_profile(
    field_data, waveguide_width, cell_size
)
```

## Learning Path

### Absolute Beginner (New to Everything)
1. Read **only the 🟢 beginner sections** first
2. Run all code cells and observe the output
3. Try the **easy exercises** at the end
4. Come back later for intermediate/advanced sections

### Some Physics Background
1. Read **🟢 beginner** and **🟡 intermediate** sections
2. Pay attention to the equations and derivations
3. Try **medium exercises** (modify parameters, observe changes)
4. Use helper functions to validate your understanding

### Advanced (Experienced in EM/Photonics)
1. Skim beginner, focus on **🔴 advanced** sections
2. Study the FDTD implementation details
3. Try **hard exercises** (measure dispersion, add bends)
4. Modify `meep_helpers.py` to add your own analysis tools

## Key Concepts

### What is a Waveguide?
A structure that confines and guides electromagnetic waves (light). Like a pipe for water, but for light!

### Why Simulate?
- **Too small to see**: Nanoscale structures (~1000× thinner than human hair)
- **Predict before fabrication**: Simulation is cheap, making devices is expensive
- **Understand physics**: See fields evolve in space and time
- **Optimize designs**: Try different geometries quickly

### FDTD Method
**F**inite-**D**ifference **T**ime-**D**omain: Solves Maxwell's equations by:
1. Dividing space into a grid
2. Dividing time into small steps
3. Calculating fields at each point and time
4. Result: A "movie" of electromagnetic fields

## Common Issues and Solutions

### Problem: Import error `ModuleNotFoundError: No module named 'meep'`
**Solution:** Meep is not installed. Use conda (recommended):
```bash
conda install -c conda-forge pymeep
```

### Problem: Simulation is very slow
**Solution:**
- Reduce resolution (try `resolution = 5` instead of 10)
- Reduce simulation time (try `run_time = 100`)
- Use 2D instead of 3D (already done in this tutorial)

### Problem: Plots don't show up
**Solution:** Make sure you have `%matplotlib inline` in first cell, and matplotlib installed.

### Problem: "Out of memory" error
**Solution:**
- Reduce resolution
- Reduce cell size
- Close other applications

### Problem: Results look wrong / no confinement
**Solution:**
- Check that permittivity `epsilon > 1` (should be ~12)
- Verify PML layers are present
- Ensure simulation ran long enough (`run_time >= 100`)

## Testing Your Understanding

Each section includes **tests** that verify the simulation is working correctly:

- ✅ **Confinement Factor**: Is light trapped in waveguide? (expect >80%)
- ✅ **Single-Mode**: Is V-number < π/2? (expect ~1.5)
- ✅ **Field Amplitude**: Are fields non-zero and finite? (expect 0.1-10)
- ✅ **Steady-State**: Did we run long enough? (expect >10 cycles)
- ✅ **Resolution**: Enough pixels per wavelength? (expect >8, better >10)

**All tests should PASS** ✓ if your simulation is correct!

## Exercises

### 🟢 Easy
1. Change frequency to 0.1 → observe longer wavelength
2. Double resolution to 20 → see if result changes
3. Remove PML → see reflections from boundaries

### 🟡 Medium
4. Make waveguide 2 μm wide → see higher-order modes
5. Change material to ε=4 → see weaker confinement
6. Add second source → observe interference

### 🔴 Hard
7. Use `GaussianSource` and measure group velocity
8. Run at multiple frequencies → calculate dispersion
9. Add a 90° bend → find minimum radius

## Next Steps

After mastering this tutorial, explore:

### More Meep Tutorials
- **Bent waveguides**: Radius of curvature, bending loss
- **Waveguide couplers**: Directional couplers, power splitting
- **Ring resonators**: Quality factor Q, free spectral range
- **Photonic crystals**: Band gaps, slow light

### Real Applications
- Fiber optic communications
- Integrated photonic circuits
- Optical sensors (biosensing, gas detection)
- Quantum photonics (single photon sources, qubits)

### Advanced Topics
- 3D simulations (slower but more realistic)
- Mode solvers (eigenmode decomposition)
- Optimization (inverse design, topology optimization)
- Near-to-far field transformations

## Resources

### Documentation
- [Meep Official Docs](https://meep.readthedocs.io/)
- [Meep Python Tutorial](https://meep.readthedocs.io/en/latest/Python_Tutorials/Basics/)
- [Simpetus (Meep developers)](https://www.simpetus.com/)

### Textbooks
- **Joannopoulos et al.**, "Photonic Crystals: Molding the Flow of Light" (theory)
- **Taflove & Hagness**, "Computational Electrodynamics: The FDTD Method" (numerics)
- **Saleh & Teich**, "Fundamentals of Photonics" (general photonics)

### Online Courses
- [Photonics Boot Camp (edX)](https://www.edx.org/course/silicon-photonics)
- [fast.ai](https://www.fast.ai/) (for the teaching philosophy used here!)

### Community
- [Meep Discussions](https://github.com/NanoComp/meep/discussions)
- [Photonics subreddit](https://www.reddit.com/r/photonics/)

## Contributing

Found a bug? Have a suggestion? Want to add more examples?

1. This is a learning project - questions welcome!
2. Try to solve issues using the helper functions
3. Share your own exercises and modifications

## Philosophy: Jeremy Howard Style

This tutorial follows the **fast.ai teaching philosophy**:

1. **Top-down learning**: Start with working code, understand later
2. **Learn by doing**: Run first, theory second
3. **Tests before execution**: Always know what to expect
4. **Progressive disclosure**: Three levels (beginner → advanced)
5. **Practical first**: Real simulations, then mathematical details

**Why?** Because you learn faster when you:
- See immediate results (motivation!)
- Build intuition before equations (understanding!)
- Test your knowledge (confidence!)

## License

This tutorial is for educational purposes. Meep is free software (GPL v2+).

---

## Quick Reference Card

### Meep Units (c = 1)
```
Distance: micrometers (μm)
Time: μm/c = 3.33 femtoseconds
Frequency: c/μm = 300 THz
Wavelength: λ = 1/f (in μm)
```

### Key Equations
```
V-number: V = (π·width/λ) × √(n_core² - n_cladding²)
Single-mode: V < π/2
Effective index: n_cladding < n_eff < n_core
Confinement: Γ = Power_waveguide / Power_total
```

### Typical Values
```
Resolution: 10-20 pixels per wavelength
PML thickness: 0.5-1.0 wavelengths
Simulation time: 10-50 optical cycles
Waveguide permittivity: ε = 4 (glass), 12 (silicon)
```

---

**Happy learning!** 🎉 Start with `meep_waveguide_tutorial.ipynb` and enjoy the journey from zero to hero!
