# Lesson 1: Fields in a Waveguide

**Based on:** [Meep Python Tutorial - Basics](https://meep.readthedocs.io/en/latest/Python_Tutorials/Basics/)

Welcome to Lesson 1! This lesson teaches you how to simulate electromagnetic fields in waveguide structures using Meep's FDTD method. We follow the **Jeremy Howard teaching style**: learn by doing, with clear expectations and tests.

## What You'll Learn

- **A Straight Waveguide**: Field patterns excited by a localized CW source
- **Waveguide physics**: How light propagates and is confined in nanoscale structures
- **Practical Meep skills**: Setup geometry, sources, boundaries, and visualization
- **Three-level understanding**: Beginner → Intermediate → Advanced explanations

## Lesson Structure

This lesson follows the official Meep tutorial structure with enhanced explanations and experimental components:

### 1. A Straight Waveguide

**Topics covered:**
- Computational cell specification
- Waveguide geometry definition using `Block` objects
- Source configuration with `ContinuousSource`
- Boundary conditions via PML (Perfectly Matched Layers)
- Resolution settings and grid discretization
- Simulation object creation
- Field computation and analysis
- Output visualization using NumPy and Matplotlib

**Files:**
- `meep_waveguide_tutorial.ipynb` - Interactive tutorial with 3-level explanations
- `quick_start.py` - Quick demo script (run first!)
- `meep_helpers.py` - Test utilities and analysis functions

### 2. A 90° Bend (Coming Soon)

**Topics to be covered:**
- Modified geometry with perpendicular waveguide segments
- Line source implementation
- Gradual source turn-on
- Time-series analysis
- Animation creation

### 3. Output Tips and Tricks (Coming Soon)

**Topics to be covered:**
- Efficient PNG image output
- Volume-restricted output
- Output directory organization
- Space-time slice generation

## Quick Start (5 minutes)

### 1. Install Dependencies

```bash
# Option A: Using conda (recommended for Meep)
conda create -n meep python=3.10
conda activate meep
conda install -c conda-forge pymeep matplotlib numpy jupyter

# Option B: Using pip (may require system dependencies)
pip install meep matplotlib numpy jupyter
```

### 2. Test Your Installation

```bash
python quick_start.py
```

This will run a complete waveguide simulation and show you the results!

### 3. Launch the Interactive Tutorial

```bash
jupyter notebook meep_waveguide_tutorial.ipynb
```

**Expected time:** ~2-3 minutes total (simulation takes ~5-10 seconds)

## What to Expect

When you run the tutorial, you'll:

1. ✅ **Import Meep** and verify installation
2. 🔲 **Define computational cell** (16 μm × 8 μm simulation space)
3. 📦 **Create waveguide geometry** (1 μm wide, silicon-like material)
4. 💡 **Add CW light source** (near-infrared frequency)
5. 🌊 **Add PML boundaries** (absorbing boundaries to prevent reflections)
6. 🚀 **Run FDTD simulation** (~5 seconds)
7. 📊 **Visualize field patterns** (see light confined and propagating!)
8. ✓ **Run automated tests** (verify single-mode operation)

## Understanding at Three Levels

Each concept in the tutorial is explained at three levels:

### 🟢 Beginner: Simple Analogies
- No prior physics knowledge required
- Uses everyday examples (fiber optic cable, water pipes)
- Focus on "what" and "why"
- **Start here if:** New to photonics or simulation

### 🟡 Intermediate: Physics & Math
- Maxwell's equations and waveguide theory
- Quantitative analysis (V-number, mode profiles)
- Design principles and rules of thumb
- **Start here if:** Physics or engineering background

### 🔴 Advanced: Implementation Details
- FDTD algorithm (Yee lattice, Courant condition)
- Numerical methods (PML, dispersion, stability)
- Performance optimization
- **Start here if:** Experienced in computational EM

**Choose your level!** Read all three, or just the one that matches your background.

## Key Concepts

### Computational Cell
The rectangular simulation domain where Maxwell's equations are solved:
- **x-direction (16 μm)**: Long enough for fields to propagate and stabilize
- **y-direction (8 μm)**: Wide enough that boundaries don't affect the waveguide mode
- **z-direction (0)**: 2D simulation (faster than 3D)

### Waveguide Geometry
- **Material**: High refractive index core (ε = 12, n ≈ 3.46, silicon-like)
- **Width**: 1 μm (designed for single-mode operation)
- **Infinite length**: Using `mp.inf` in x-direction

### Source
- **Type**: Continuous wave (CW) at single frequency
- **Frequency**: 0.15 (in Meep units, λ ≈ 6.67 μm)
- **Position**: Near left edge to excite waveguide mode
- **Component**: Ez (TE-like polarization in 2D)

### Boundary Conditions
- **PML layers**: 1 μm thick absorbing boundaries on all sides
- **Purpose**: Simulate infinite space by absorbing outgoing waves

### Resolution
- **Setting**: 10 pixels per μm
- **Rule of thumb**: Need >8 pixels per wavelength in material
- **Trade-off**: Higher resolution = more accurate but slower

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

## Learning Paths

### Path A: Absolute Beginner
1. Run `quick_start.py` to see a working simulation
2. Open the notebook and read **only 🟢 beginner sections**
3. Run all code cells and observe the output
4. Try the **easy exercises** at the end
5. Come back later for intermediate/advanced sections

### Path B: Some Physics Background
1. Run `quick_start.py` for quick context
2. Work through the notebook, reading **🟢 and 🟡 sections**
3. Pay attention to equations and derivations
4. Try **medium exercises** (modify parameters, observe changes)
5. Use helper functions to validate understanding

### Path C: Advanced User
1. Skim beginner sections, focus on **🔴 advanced**
2. Study FDTD implementation details
3. Try **hard exercises** (measure dispersion, add bends)
4. Modify `meep_helpers.py` to add your own analysis tools

## Testing Your Understanding

Each section includes **automated tests** that verify simulation correctness:

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
9. Add a 90° bend → find minimum radius (prepares for section 2!)

## Common Issues and Solutions

### Problem: Import error `ModuleNotFoundError: No module named 'meep'`
**Solution:** Install using conda:
```bash
conda install -c conda-forge pymeep
```

### Problem: Simulation is very slow
**Solution:**
- Reduce resolution (try `resolution = 5`)
- Reduce simulation time (try `run_time = 100`)

### Problem: No confinement visible
**Solution:**
- Check that permittivity `epsilon > 1` (should be ~12)
- Verify PML layers are present
- Ensure simulation ran long enough (`run_time >= 100`)

## Resources

### See Also
- `CHEATSHEET.md` - Quick reference for Meep commands and equations
- [Official Meep Tutorial](https://meep.readthedocs.io/en/latest/Python_Tutorials/Basics/)
- [Meep Python API](https://meep.readthedocs.io/en/latest/Python_User_Interface/)

### Next Lesson
- **Lesson 2**: Cylindrical Coordinates - Learn to exploit rotational symmetry for faster simulations

### Textbooks
- **Joannopoulos et al.**, "Photonic Crystals: Molding the Flow of Light"
- **Taflove & Hagness**, "Computational Electrodynamics: The FDTD Method"
- **Saleh & Teich**, "Fundamentals of Photonics"

## Philosophy: Jeremy Howard Style

This tutorial follows the **fast.ai teaching philosophy**:

1. **Top-down learning**: Start with working code, understand later
2. **Learn by doing**: Run first, theory second
3. **Clear expectations**: Always know what to expect before running
4. **Progressive disclosure**: Three levels (beginner → advanced)
5. **Tests first**: Verify understanding with automated tests

**Why?** Because you learn faster when you see immediate results, build intuition before equations, and test your knowledge!

---

**Ready to start?** Run `python quick_start.py` or open `meep_waveguide_tutorial.ipynb`!
