# Lesson 2: Cylindrical Coordinates

**Based on:** [Meep Python Tutorial - Cylindrical Coordinates](https://meep.readthedocs.io/en/latest/Python_Tutorials/Cylindrical_Coordinates/)

Welcome to Lesson 2! This lesson teaches you how to exploit rotational symmetry in your simulations to dramatically improve performance. We'll transform 2D problems into 1D calculations using cylindrical coordinates.

## What You'll Learn

- **Cylindrical coordinate systems**: Transform rotationally symmetric structures
- **Performance optimization**: Reduce 2D simulations to 1D (much faster!)
- **Angular mode analysis**: Understanding exp(imφ) dependence
- **Perturbation theory**: Shape optimization using semi-analytical methods
- **Scattering problems**: Cylinders, spheres, and zone plates in cylindrical coordinates

## Why Cylindrical Coordinates?

### The Power of Symmetry
When your structure has **continuous rotational symmetry** (looks the same when rotated), you can:
- **Reduce dimensionality**: 2D → 1D, 3D → 2D
- **Speed up dramatically**: 10-100× faster simulations
- **Analyze modes separately**: Each angular mode number m runs independently
- **Reduce memory**: Smaller computational domain

### When to Use It
✅ Ring resonators
✅ Circular gratings
✅ Cylindrical waveguides
✅ Spherical particles
✅ Zone plates
❌ Rectangular waveguides
❌ Non-circular structures

## Lesson Structure

This lesson follows the official Meep cylindrical coordinates tutorial with enhanced explanations:

### 1. Modes of a Ring Resonator

**Topics covered:**
- Setting up cylindrical coordinates with `mp.CYLINDRICAL`
- Understanding angular dependence exp(imφ)
- Converting 2D ring resonator to 1D simulation
- Comparing performance: cylindrical vs Cartesian
- Mode number m and field patterns
- PML behavior in cylindrical geometries

**Learning objectives:**
- 🟢 **Beginner**: Understand what rotational symmetry means
- 🟡 **Intermediate**: Set up cylindrical simulations in Meep
- 🔴 **Advanced**: Optimize convergence and understand PML artifacts

### 2. Sensitivity Analysis via Perturbation Theory

**Topics covered:**
- Computing frequency derivatives ∂ω/∂r for shape optimization
- Semi-analytical perturbation theory implementation
- Validation against finite-difference methods
- Parallel (Ez) and perpendicular (Hz) polarizations
- Computational efficiency comparison

**Learning objectives:**
- 🟢 **Beginner**: Why perturbation theory matters for optimization
- 🟡 **Intermediate**: Calculate sensitivity from field patterns
- 🔴 **Advanced**: Implement and validate perturbation theory

### 3. Scattering Cross Section of a Finite Dielectric Cylinder

**Topics covered:**
- Scattering problems in cylindrical coordinates
- Cross-section calculations
- Far-field analysis
- Mode decomposition of scattered fields

**Learning objectives:**
- 🟢 **Beginner**: What is scattering cross-section?
- 🟡 **Intermediate**: Set up scattering simulations
- 🔴 **Advanced**: Accurate far-field transformations

### 4. Scattering from a Sphere with Oblique Planewave

**Topics covered:**
- 3D problems in cylindrical coordinates
- Oblique incidence angles
- Mie scattering theory validation
- Angular resolution requirements

**Learning objectives:**
- 🟢 **Beginner**: How to handle 3D in cylindrical coordinates
- 🟡 **Intermediate**: Oblique planewave sources
- 🔴 **Advanced**: Validate against analytical Mie theory

### 5. Focusing Properties of a Binary-Phase Zone Plate

**Topics covered:**
- Diffractive optics in cylindrical coordinates
- Binary phase structures
- Focal point analysis
- Efficiency calculations

**Learning objectives:**
- 🟢 **Beginner**: What is a zone plate and how does it work?
- 🟡 **Intermediate**: Design and simulate zone plates
- 🔴 **Advanced**: Optimize focusing efficiency

### 6. Nonaxisymmetric Dipole Sources

**Topics covered:**
- Breaking rotational symmetry with sources
- Dipole orientation effects
- Mode excitation analysis
- Source positioning strategies

**Learning objectives:**
- 🟢 **Beginner**: How sources work in cylindrical coordinates
- 🟡 **Intermediate**: Position and orient dipole sources
- 🔴 **Advanced**: Mode coupling and excitation efficiency

## Prerequisites

Before starting Lesson 2, you should:
- ✅ Complete **Lesson 1** (Straight Waveguide)
- ✅ Understand basic Meep simulation setup
- ✅ Be comfortable with field visualization
- ✅ Know what waveguide modes are

Optional but helpful:
- 📖 Basic understanding of cylindrical coordinates (r, φ, z)
- 📖 Complex exponentials and Fourier modes
- 📖 Eigenmode analysis

## Key Concepts

### Cylindrical Coordinate System

**In Cartesian (2D):**
```
x, y → Full 2D grid needed
Memory: N × N points
```

**In Cylindrical (exploit symmetry):**
```
r, φ, z → φ is analytical (exp(imφ))
Only simulate r-direction
Memory: N points (1D!)
```

### Angular Mode Number (m)

The field has angular dependence: **exp(imφ)**

- **m = 0**: Radially symmetric (no angular variation)
- **m = 1**: Dipole-like pattern (one lobe)
- **m = 2**: Quadrupole pattern (two lobes)
- **m = ±n**: n-fold symmetry

### The `mp.CYLINDRICAL` Setting

```python
sim = mp.Simulation(
    cell_size=cell_size,
    geometry=geometry,
    sources=sources,
    boundary_layers=pml_layers,
    resolution=resolution,
    dimensions=mp.CYLINDRICAL,  # Key setting!
    m=2  # Angular mode number
)
```

### Performance Comparison

| Setup | Dimensions | Grid Points | Relative Speed |
|-------|------------|-------------|----------------|
| Ring in Cartesian | 2D | 200 × 200 = 40,000 | 1× (baseline) |
| Ring in Cylindrical | 1D | 200 | **200× faster!** |

## Quick Start (Coming Soon)

Files that will be added:
- `ring_resonator.ipynb` - Interactive tutorial for section 1
- `perturbation_theory.ipynb` - Sensitivity analysis (section 2)
- `scattering_cylinder.ipynb` - Cylinder scattering (section 3)
- `sphere_scattering.ipynb` - Sphere scattering (section 4)
- `zone_plate.ipynb` - Zone plate focusing (section 5)
- `dipole_sources.ipynb` - Dipole source tutorial (section 6)
- `cylindrical_helpers.py` - Analysis utilities
- `quick_start.py` - Demo script

## Understanding at Three Levels

### 🟢 Beginner: Intuitive Understanding
- **Symmetry analogy**: Like using a pie slice to understand the whole pie
- **Why it's faster**: Only simulate what changes (radius), not what repeats (angle)
- **When to use it**: Circles, rings, spheres, cylinders
- Focus on running examples and seeing the speedup

### 🟡 Intermediate: Mathematical Foundation
- **Separation of variables**: F(r,φ,z) = R(r) × exp(imφ) × Z(z)
- **Mode orthogonality**: Different m values don't interact
- **Boundary conditions**: PML and continuity in cylindrical coords
- **Convergence**: Resolution requirements in r-direction

### 🔴 Advanced: Implementation Details
- **Yee lattice in cylindrical**: Staggered grid complications
- **Origin handling**: Special treatment at r=0
- **PML in cylindrical**: Stretched coordinates and stability
- **Numerical dispersion**: Anisotropic in (r,φ,z)

## Lesson Roadmap

```
Week 1: Modes of a Ring Resonator
├─ Understand cylindrical coordinates
├─ Convert ring resonator simulation
├─ Compare Cartesian vs cylindrical
└─ Analyze different mode numbers m

Week 2: Perturbation Theory
├─ Calculate frequency derivatives
├─ Implement perturbation theory
├─ Validate against finite differences
└─ Apply to shape optimization

Week 3: Scattering Problems
├─ Cylinder scattering cross-section
├─ Sphere with oblique incidence
├─ Far-field analysis
└─ Compare with analytical solutions

Week 4: Advanced Topics
├─ Zone plate focusing
├─ Nonaxisymmetric sources
├─ Optimization applications
└─ Final project ideas
```

## Coming Soon

This lesson is under development. We're creating:

1. ✏️ Interactive Jupyter notebooks for each section
2. ✏️ Helper functions for cylindrical coordinate analysis
3. ✏️ Automated tests for each tutorial
4. ✏️ Visualization tools for cylindrical geometries
5. ✏️ Exercises at three difficulty levels

## Prerequisites Check

Before starting, make sure you can answer:

### From Lesson 1
- ❓ What is a PML boundary and why do we need it?
- ❓ What does "resolution = 10" mean?
- ❓ How do you create geometry with `mp.Block`?
- ❓ What's the difference between CW and pulsed sources?

If you're unsure, review **Lesson 1** first!

## Resources

### Documentation
- [Official Cylindrical Coordinates Tutorial](https://meep.readthedocs.io/en/latest/Python_Tutorials/Cylindrical_Coordinates/)
- [Meep Cylindrical API](https://meep.readthedocs.io/en/latest/Python_User_Interface/#dimensions)

### Theory Background
- **Balanis**, "Advanced Engineering Electromagnetics" (cylindrical coordinates chapter)
- **Jackson**, "Classical Electrodynamics" (separation of variables in cylinders)
- **Bohren & Huffman**, "Absorption and Scattering of Light by Small Particles" (Mie theory)

### Related Topics
- Lesson 1: Fields in a Waveguide (prerequisite)
- Lesson 3: Resonant Modes (coming soon)
- Advanced: Subpixel Smoothing

## Stay Tuned!

This lesson will be released after Lesson 1 is completed. In the meantime:
1. Master Lesson 1
2. Read about cylindrical coordinates in textbooks
3. Think about rotationally symmetric structures you want to simulate

---

**Current Status:** 📝 In Development
**Expected Release:** After Lesson 1 completion
**Estimated Time:** 4-6 hours of interactive learning

Check back soon! 🚀
