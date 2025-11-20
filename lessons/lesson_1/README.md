# Lesson 1: Basics - Python Tutorial

**Based on:** [Meep Python Tutorial - Basics](https://meep.readthedocs.io/en/latest/Python_Tutorials/Basics/)

Welcome to Lesson 1! This comprehensive tutorial covers the fundamentals of Meep through a series of practical examples. We follow the **Jeremy Howard teaching style**: learn by doing, with clear expectations and tests, following the official Meep tutorial structure with enhanced explanations.

## What You'll Learn

- **The Meep Library**: Understanding the core components and structure
- **Waveguide simulations**: Fields, bends, and transmission analysis
- **Scattering problems**: Interfaces, spheres, and cylinders
- **Resonators**: Ring resonator modes and symmetry exploitation
- **3D visualization**: Techniques for complex geometries
- **Three-level understanding**: Beginner → Intermediate → Advanced explanations

## Lesson Structure

This lesson follows the complete official Meep Basics tutorial structure:

### 1. The Meep Library

**Topics covered:**
- Overview of Meep's Python interface
- Core concepts and terminology
- Units and conventions
- Basic workflow

**Learning objectives:**
- 🟢 **Beginner**: Understand what Meep is and basic concepts
- 🟡 **Intermediate**: Learn the library structure and conventions
- 🔴 **Advanced**: Understand implementation architecture

**Status:** 📝 Coming Soon

---

### 2. Fields in a Waveguide

**Main topics:**

#### 2.1 A Straight Waveguide

**Topics covered:**
- Computational cell specification
- Waveguide geometry definition using `Block` objects
- Source configuration with `ContinuousSource`
- Boundary conditions via PML (Perfectly Matched Layers)
- Resolution settings and grid discretization
- Simulation object creation
- Field computation and analysis
- Output visualization using NumPy and Matplotlib

**Learning objectives:**
- 🟢 **Beginner**: Run your first waveguide simulation
- 🟡 **Intermediate**: Understand single-mode vs multi-mode operation
- 🔴 **Advanced**: FDTD grid setup and stability conditions

**Status:** ✅ Complete
**Files:** `meep_waveguide_tutorial.ipynb`, `quick_start.py`, `meep_helpers.py`

#### 2.2 A 90° Bend

**Topics covered:**
- Modified geometry with perpendicular waveguide segments
- Line source implementation with `size` property
- Gradual source turn-on using `width` parameter
- Alternative wavelength specification method
- Output to HDF5 format across time dimension
- Animation creation from time-series data

**Subtopic: Output Tips and Tricks**
- Efficient PNG image output versus raw data storage
- Volume-restricted output using `in_volume`
- Output directory organization
- Space-time slice generation

**Learning objectives:**
- 🟢 **Beginner**: Simulate light bending around corners and save results efficiently
- 🟡 **Intermediate**: Understand bending losses, create animations, and optimize output
- 🔴 **Advanced**: Optimize bend radius for minimum loss and custom HDF5 output

**Status:** 📝 Coming Soon

---

### 3. Transmittance Spectrum of a Waveguide Bend

**Topics covered:**
- Frequency-domain analysis using pulsed sources
- Flux region definition and measurement
- Normalization runs for accurate transmission
- Transmission spectrum calculation
- Resonance identification

**Learning objectives:**
- 🟢 **Beginner**: Measure how much light gets through a bend
- 🟡 **Intermediate**: Calculate wavelength-dependent transmission
- 🔴 **Advanced**: Understand flux plane placement and convergence

**Status:** 📝 Coming Soon

---

### 4. Angular Reflectance Spectrum of a Planar Interface

**Topics covered:**
- Planar interface setup (air-dielectric boundary)
- Oblique angle incidence
- Reflection and transmission coefficients
- Angular dependence analysis
- Comparison with Fresnel equations

**Learning objectives:**
- 🟢 **Beginner**: Understand reflection at interfaces
- 🟡 **Intermediate**: Validate against analytical Fresnel formulas
- 🔴 **Advanced**: Handle numerical dispersion at oblique angles

**Status:** 📝 Coming Soon

---

### 5. Mie Scattering of a Lossless Dielectric Sphere

**Topics covered:**
- 3D spherical geometry setup
- Planewave source implementation
- Far-field flux measurements
- Scattering cross-section calculation
- Validation against Mie theory

#### Subsection: Differential/Radar Cross Section

**Additional topics:**
- Angular scattering patterns
- Differential cross-section (DCS)
- Radar cross-section (RCS)
- Far-field decomposition
- Validation with analytical solutions

**Learning objectives:**
- 🟢 **Beginner**: Simulate light scattering from a sphere and visualize patterns
- 🟡 **Intermediate**: Calculate scattering and radar cross-sections
- 🔴 **Advanced**: Near-to-far field transformations and optimize accuracy

**Status:** 📝 Coming Soon

---

### 6. Absorbed Power Density Map of a Lossy Cylinder

**Topics covered:**
- Lossy material specification (complex permittivity)
- Power absorption calculations
- Field intensity mapping
- 2D visualization of absorption
- Applications to heating and sensing

**Learning objectives:**
- 🟢 **Beginner**: See where energy is absorbed in materials
- 🟡 **Intermediate**: Calculate absorption cross-sections
- 🔴 **Advanced**: Implement complex dispersive materials

**Status:** 📝 Coming Soon

---

### 7. Modes of a Ring Resonator

**Topics covered:**
- Ring resonator geometry setup
- Mode excitation techniques
- Quality factor (Q) measurement
- Free spectral range (FSR) calculation
- Resonance peak identification

#### Subsection: Exploiting Symmetry

**Additional topics:**
- Mirror symmetries in 2D
- Even/odd field components
- Computational speedup from symmetries
- Symmetry-based mode selection
- Limitations and considerations

**Learning objectives:**
- 🟢 **Beginner**: Understand ring resonators and use symmetries to speed up simulations
- 🟡 **Intermediate**: Design resonators with target Q and FSR, apply appropriate symmetries
- 🔴 **Advanced**: Mode coupling theory, critical coupling, and custom symmetry constraints

**Status:** 📝 Coming Soon

---

### 8. Visualizing 3D Structures

**Topics covered:**
- 3D geometry visualization techniques
- Epsilon (permittivity) field plotting
- Cross-sectional views
- Interactive 3D visualization
- Export for external rendering tools

**Learning objectives:**
- 🟢 **Beginner**: Visualize your 3D geometry before simulation
- 🟡 **Intermediate**: Create publication-quality figures
- 🔴 **Advanced**: Custom visualization scripts and VTK export

**Status:** 📝 Coming Soon

---

## Quick Start (Currently Available)

### A Straight Waveguide (Section 2.1)

#### Installation (5 minutes)

```bash
# Option A: Using conda (recommended for Meep)
conda create -n meep python=3.10
conda activate meep
conda install -c conda-forge pymeep matplotlib numpy jupyter

# Option B: Using pip (may require system dependencies)
pip install meep matplotlib numpy jupyter
```

#### Test Your Installation

```bash
cd lessons/lesson_1
python quick_start.py
```

This will run a complete straight waveguide simulation and show you the results!

#### Launch the Interactive Tutorial

```bash
cd lessons/lesson_1
jupyter notebook meep_waveguide_tutorial.ipynb
```

**Expected time:** ~2-3 minutes total (simulation takes ~5-10 seconds)

## What to Expect

When you complete this lesson, you'll be able to:

1. ✅ **Set up simulations** - Define geometry, sources, and boundaries
2. ✅ **Run FDTD simulations** - Execute and monitor convergence
3. ✅ **Analyze fields** - Extract and visualize electromagnetic fields
4. ✅ **Calculate spectra** - Compute transmission and reflection
5. ✅ **Measure cross-sections** - Scattering and absorption analysis
6. ✅ **Optimize designs** - Use symmetries and understand trade-offs
7. ✅ **Create visualizations** - Professional plots and animations

## Understanding at Three Levels

Each concept in the tutorial is explained at three levels:

### 🟢 Beginner: Simple Analogies
- No prior physics knowledge required
- Uses everyday examples (fiber optics, radio antennas, mirrors)
- Focus on "what" and "why"
- **Start here if:** New to photonics or simulation

### 🟡 Intermediate: Physics & Math
- Maxwell's equations and analytical solutions
- Quantitative analysis (Q-factors, cross-sections, Fresnel equations)
- Design principles and rules of thumb
- **Start here if:** Physics or engineering background

### 🔴 Advanced: Implementation Details
- FDTD algorithm (Yee lattice, Courant condition)
- Numerical methods (PML, dispersion, stability)
- Performance optimization and parallelization
- **Start here if:** Experienced in computational EM

**Choose your level!** Read all three, or just the one that matches your background.

## Learning Paths

### Path A: Absolute Beginner (Complete Lesson)
**Time commitment:** ~12-15 hours

1. Start with Section 1: The Meep Library
2. Work through Section 2: Fields in a Waveguide (currently run `quick_start.py`)
3. Read **only 🟢 beginner sections**
4. Run all code cells and observe outputs
5. Try **easy exercises** for each section
6. Progress through sections 3-8 sequentially
7. Come back later for intermediate/advanced sections

### Path B: Some Physics Background (Targeted Learning)
**Time commitment:** ~15-20 hours

1. Skim Section 1, focus on conventions
2. Work through Section 2, reading **🟢 and 🟡 sections**
3. Focus on sections most relevant to your interests:
   - Waveguides → Sections 2-3
   - Scattering → Sections 4-6
   - Resonators → Section 7
4. Try **medium exercises** (parameter exploration)
5. Use helper functions to validate understanding

### Path C: Advanced User (Comprehensive Mastery)
**Time commitment:** ~10-12 hours

1. Skim beginner content, focus on **🔴 advanced sections**
2. Study FDTD implementation details in each section
3. Try **hard exercises** (custom analysis, optimization)
4. Modify helper modules for your specific needs
5. Complete all sections for comprehensive understanding

## Files and Resources

### Current Files (Section 2.1 - A Straight Waveguide)
- `meep_waveguide_tutorial.ipynb` - Interactive tutorial with 3-level explanations
- `quick_start.py` - Quick demo script (run first!)
- `meep_helpers.py` - Test utilities and analysis functions
- `CHEATSHEET.md` - Quick reference for Meep commands

### Coming Soon (Sections 1, 2.2-2.3, 3-8)
Each section will include:
- Interactive Jupyter notebook
- Helper functions specific to that topic
- Automated tests
- Example scripts
- Exercises at three levels

## Key Concepts Reference

### Simulation Components
- **Geometry**: `Block`, `Cylinder`, `Sphere` objects
- **Materials**: `Medium` with epsilon, mu, conductivity
- **Sources**: `ContinuousSource`, `GaussianSource`, planewave
- **Boundaries**: PML, periodic, mirror symmetries
- **Outputs**: Field arrays, flux measurements, animations

### Analysis Techniques
- **Time domain**: Field evolution, animations
- **Frequency domain**: Transmission/reflection spectra
- **Spatial analysis**: Mode profiles, field distributions
- **Scattering**: Cross-sections, far-field patterns
- **Resonances**: Q-factors, mode frequencies

### Common Parameters
```python
resolution = 10           # pixels per unit length
frequency = 0.15          # in c/unit_length
wavelength = 1/frequency  # in unit_length
runtime = 200            # in time units
pml_thickness = 1.0      # in unit_length
```

## Testing Your Understanding

Automated tests (currently in Section 2.1) verify:
- ✅ **Confinement Factor**: Is light trapped? (expect >80%)
- ✅ **Single-Mode**: Is V-number < π/2?
- ✅ **Field Amplitude**: Are fields non-zero and finite?
- ✅ **Steady-State**: Did we run long enough?
- ✅ **Resolution**: Enough pixels per wavelength?

Each future section will include similar targeted tests.

## Exercises by Section

### Section 2.1 - A Straight Waveguide (Available Now)

#### 🟢 Easy
1. Change frequency to 0.1 → observe longer wavelength
2. Double resolution to 20 → see if result changes
3. Remove PML → see reflections from boundaries

#### 🟡 Medium
4. Make waveguide 2 μm wide → see higher-order modes
5. Change material to ε=4 → see weaker confinement
6. Add second source → observe interference

#### 🔴 Hard
7. Use `GaussianSource` and measure group velocity
8. Run at multiple frequencies → calculate dispersion
9. Add a 90° bend → find minimum radius

### Sections 2.2-8 (Coming Soon)
Each section will include exercises at three difficulty levels following the same format.

## Common Issues and Solutions

### Installation
**Problem:** `ModuleNotFoundError: No module named 'meep'`
**Solution:** Install using conda: `conda install -c conda-forge pymeep`

### Performance
**Problem:** Simulation is very slow
**Solution:**
- Reduce resolution: `resolution = 5`
- Reduce runtime: `runtime = 100`
- Use 2D instead of 3D
- Exploit symmetries (Section 7.2)

### Accuracy
**Problem:** No field confinement visible
**Solution:**
- Check permittivity: `epsilon > 1` (should be ~12)
- Verify PML layers are present
- Ensure runtime is sufficient: `runtime >= 100`

### Numerical Issues
**Problem:** Strange artifacts or instabilities
**Solution:**
- Increase resolution (especially near material interfaces)
- Check Courant condition is satisfied (automatic in Meep)
- Verify PML thickness is adequate (>= 0.5 wavelength)

## Resources

### See Also
- `CHEATSHEET.md` - Quick reference for Meep commands and equations
- [Official Meep Tutorial](https://meep.readthedocs.io/en/latest/Python_Tutorials/Basics/)
- [Meep Python API](https://meep.readthedocs.io/en/latest/Python_User_Interface/)

### Next Lesson
- **Lesson 2**: Cylindrical Coordinates - Exploit rotational symmetry for faster simulations

### Textbooks
- **Joannopoulos et al.**, "Photonic Crystals: Molding the Flow of Light"
- **Taflove & Hagness**, "Computational Electrodynamics: The FDTD Method"
- **Saleh & Teich**, "Fundamentals of Photonics"
- **Bohren & Huffman**, "Absorption and Scattering of Light by Small Particles"

### Community
- [Meep Discussions](https://github.com/NanoComp/meep/discussions)
- [Meep GitHub Issues](https://github.com/NanoComp/meep/issues)

## Development Roadmap

### ✅ Completed
- Section 2.1: A Straight Waveguide

### 📝 In Development (Priority Order)
1. Section 1: The Meep Library
2. Section 2.2: A 90° Bend
3. Section 2.3: Output Tips and Tricks
4. Section 3: Transmittance Spectrum of a Waveguide Bend
5. Section 7: Modes of a Ring Resonator
6. Section 4: Angular Reflectance Spectrum of a Planar Interface
7. Section 5: Mie Scattering of a Lossless Dielectric Sphere
8. Section 6: Absorbed Power Density Map of a Lossy Cylinder
9. Section 8: Visualizing 3D Structures

## Philosophy: Jeremy Howard Style

This tutorial follows the **fast.ai teaching philosophy**:

1. **Top-down learning**: Start with working code, understand later
2. **Learn by doing**: Run first, theory second
3. **Clear expectations**: Always know what to expect before running
4. **Progressive disclosure**: Three levels (beginner → advanced)
5. **Tests first**: Verify understanding with automated tests
6. **Complete examples**: Full, working code from start to finish

**Why?** Because you learn faster when you see immediate results, build intuition before equations, and test your knowledge!

---

## Current Status

**Overall Progress:** Section 2.1 complete (1 subsection of Section 2 done)

| Section | Status | Notebook | Tests | Exercises |
|---------|--------|----------|-------|-----------|
| 1. The Meep Library | 📝 | ❌ | ❌ | ❌ |
| 2. Fields in a Waveguide | 🔨 | 🔨 | 🔨 | 🔨 |
| ↳ 2.1 A Straight Waveguide | ✅ | ✅ | ✅ | ✅ |
| ↳ 2.2 A 90° Bend (+Output Tips) | 📝 | ❌ | ❌ | ❌ |
| 3. Transmittance Spectrum | 📝 | ❌ | ❌ | ❌ |
| 4. Angular Reflectance | 📝 | ❌ | ❌ | ❌ |
| 5. Mie Scattering | 📝 | ❌ | ❌ | ❌ |
| ↳ 5a. Differential/Radar Cross Section | 📝 | ❌ | ❌ | ❌ |
| 6. Absorbed Power Density | 📝 | ❌ | ❌ | ❌ |
| 7. Modes of a Ring Resonator | 📝 | ❌ | ❌ | ❌ |
| ↳ 7a. Exploiting Symmetry | 📝 | ❌ | ❌ | ❌ |
| 8. Visualizing 3D Structures | 📝 | ❌ | ❌ | ❌ |

**Legend:** ✅ Complete | 🔨 In Progress | 📝 Coming Soon | ❌ Not Started

---

**Ready to start?** Run `python quick_start.py` to try Section 2.1, or open `meep_waveguide_tutorial.ipynb` for the interactive tutorial!

**Have questions?** Check the [Meep FAQ](https://meep.readthedocs.io/en/latest/FAQ/) or [ask the community](https://github.com/NanoComp/meep/discussions)!
