# Meep Waveguide Cheat Sheet 📋

Quick reference for waveguide simulations in Meep.

## Meep Units (c = 1)

| Quantity | Unit | Conversion |
|----------|------|------------|
| **Distance** | μm (micrometers) | 1 μm = 10⁻⁶ m |
| **Time** | μm/c | 1 time unit = 3.33 femtoseconds |
| **Frequency** | c/μm | 1 freq unit = 300 THz |
| **Wavelength** | μm | λ = 1/f |

## Key Equations

### Waveguide Theory

```
V-number (normalized frequency):
  V = (π × width / λ) × √(n_core² - n_cladding²)

Single-mode condition:
  V < π/2 ≈ 1.57

Effective refractive index:
  n_cladding < n_eff < n_core

Confinement factor:
  Γ = ∫∫_core |E|² dA / ∫∫_all |E|² dA

Evanescent decay:
  E(y) = E₀ exp(-γy)  where γ = √(β² - k₀²n_cladding²)
```

### FDTD Method

```
Courant stability condition:
  Δt ≤ Δx / (c√d)  where d = dimensionality
  Meep uses: Δt = 0.5 × Δx / c

Resolution (pixels per wavelength):
  PPW = resolution × λ_min
  Required: PPW > 8 (better: 10-20)

Numerical dispersion error:
  Error ≈ (Δx/λ)²
```

## Common Material Properties

| Material | Permittivity (ε) | Refractive Index (n) | Notes |
|----------|------------------|---------------------|-------|
| **Vacuum/Air** | 1.0 | 1.0 | Reference |
| **SiO₂ (glass)** | ~2.1 | 1.45 | Fiber optics |
| **Si₃N₄** | ~4.0 | 2.0 | Low-loss waveguides |
| **Silicon (1.5 μm)** | ~12.0 | 3.46 | High-index contrast |
| **GaAs** | ~13.0 | 3.6 | Active devices |

## Typical Parameter Values

### Resolution
```python
resolution = 10    # Good default (10 pixels/μm)
resolution = 20    # High accuracy (slower)
resolution = 5     # Quick testing (less accurate)
```

### PML Thickness
```python
pml_thickness = 1.0           # Standard (1 μm)
pml_thickness = 0.5 * λ_max   # Rule of thumb
```

### Simulation Time
```python
runtime = 10 / frequency      # 10 optical cycles (minimum)
runtime = 200                 # Typical for CW steady-state
runtime = 50 / frequency      # Conservative (50 cycles)
```

### Waveguide Dimensions
```python
width = 0.5    # Narrow, strong confinement
width = 1.0    # Standard single-mode
width = 2.0    # May support higher-order modes
```

## Quick Simulation Template

```python
import meep as mp

# Parameters
resolution = 10
frequency = 0.15
waveguide_width = 1.0
epsilon = 12

# Geometry
cell_size = mp.Vector3(16, 8, 0)
geometry = [
    mp.Block(
        size=mp.Vector3(mp.inf, waveguide_width, mp.inf),
        center=mp.Vector3(0, 0, 0),
        material=mp.Medium(epsilon=epsilon)
    )
]

# Source
sources = [
    mp.Source(
        src=mp.ContinuousSource(frequency=frequency),
        component=mp.Ez,
        center=mp.Vector3(-7, 0, 0)
    )
]

# Boundaries
pml_layers = [mp.PML(thickness=1.0)]

# Simulation
sim = mp.Simulation(
    cell_size=cell_size,
    geometry=geometry,
    sources=sources,
    boundary_layers=pml_layers,
    resolution=resolution
)

# Run
sim.run(until=200)

# Get fields
ez_data = sim.get_array(center=mp.Vector3(), size=cell_size, component=mp.Ez)
```

## Field Components

### TE Modes (Transverse Electric)
- **Ez ≠ 0** (out of plane)
- **Hz = 0** (no magnetic field out of plane)
- **Use:** `component=mp.Ez` in source

### TM Modes (Transverse Magnetic)
- **Ez = 0**
- **Hz ≠ 0** (out of plane)
- **Use:** `component=mp.Hz` in source

## Common Source Types

```python
# Continuous wave (single frequency)
mp.ContinuousSource(frequency=f)

# Gaussian pulse (broadband)
mp.GaussianSource(frequency=f, width=w)

# Custom temporal profile
mp.CustomSource(src_func=lambda t: np.sin(2*np.pi*f*t))

# Eigenmode source (single mode, no backward wave)
mp.EigenModeSource(
    src=mp.GaussianSource(frequency=f, width=w),
    center=mp.Vector3(x, y, z),
    size=mp.Vector3(0, sy, sz),
    eig_band=1
)
```

## Boundary Conditions

```python
# PML (absorbing)
pml_layers = [mp.PML(thickness=1.0)]

# Periodic (for photonic crystals)
geometry_lattice = mp.Lattice(size=mp.Vector3(sx, sy))
k_points = [mp.Vector3(kx, ky)]

# Perfect electric conductor (PEC)
# Add a metallic Block with epsilon = -∞

# Perfect magnetic conductor (PMC)
# Use symmetry: sim.symmetries = [mp.Mirror(mp.Y, phase=-1)]
```

## Data Output

```python
# Get field arrays
ez = sim.get_array(center=mp.Vector3(), size=cell_size, component=mp.Ez)
eps = sim.get_array(center=mp.Vector3(), size=cell_size, component=mp.Dielectric)

# Output to HDF5
sim.output_field_components(mp.Ez)

# Flux measurement
flux_region = mp.FluxRegion(center=mp.Vector3(x, 0), size=mp.Vector3(0, sy))
flux = sim.add_flux(frequency, 0, 1, flux_region)

# Run and get flux
sim.run(until=200)
flux_value = mp.get_fluxes(flux)[0]
```

## Analysis Formulas

### Wavelength Conversions
```python
# Vacuum wavelength from frequency
λ_vacuum = 1 / f

# Material wavelength
λ_material = λ_vacuum / n

# Frequency from wavelength
f = 1 / λ_vacuum
```

### Effective Index (from simulation)
```python
# From spatial frequency of field pattern
k_x = 2π / λ_pattern
n_eff = k_x / k_0 = λ_vacuum / λ_pattern
```

### Confinement Factor
```python
power_density = np.abs(E)**2
total_power = np.sum(power_density)
core_power = np.sum(power_density[core_mask])
Γ = core_power / total_power
```

## Debugging Checklist

When results look wrong:

- [ ] Check permittivity: `epsilon > 1`?
- [ ] Check PML: `pml_thickness ≥ 0.5λ`?
- [ ] Check resolution: `resolution × λ > 8`?
- [ ] Check runtime: `runtime × frequency > 10`?
- [ ] Check source position: Inside simulation domain?
- [ ] Check cell size: Large enough (4-8× waveguide width)?
- [ ] Check units: All distances in same units (μm)?
- [ ] Check visualization: `origin='lower'` in imshow?

## Performance Optimization

```python
# 2D simulation (fastest)
cell_size = mp.Vector3(sx, sy, 0)

# Symmetries (2× speedup per symmetry)
sim.symmetries = [mp.Mirror(mp.Y)]

# Parallel (MPI)
# Run with: mpirun -np 4 python script.py
# Requires: pip install mpi4py

# Reduce resolution for testing
resolution = 5  # Quick test
resolution = 10  # Production

# Adaptive time stepping (automatic in Meep)
# Meep automatically uses Courant factor ~0.5
```

## Common Errors and Fixes

| Error | Cause | Solution |
|-------|-------|----------|
| `ModuleNotFoundError: meep` | Meep not installed | `conda install -c conda-forge pymeep` |
| Simulation very slow | High resolution or 3D | Reduce resolution or use 2D |
| No confinement | Wrong material | Check `epsilon > 1` |
| Strange oscillations | Too short runtime | Increase `until` parameter |
| Jagged field patterns | Low resolution | Increase `resolution` |

## Quick Calculations

```python
# V-number calculator
def v_number(width, wavelength, n_core, n_clad=1.0):
    return (np.pi * width / wavelength) * np.sqrt(n_core**2 - n_clad**2)

# Single mode?
V = v_number(1.0, 6.67, 3.46)
is_single_mode = V < np.pi/2

# Required resolution
λ_min = wavelength / n_core
pixels_per_λ = resolution * λ_min
# Should be > 8, preferably > 10

# Memory estimate (2D)
grid_points = (cell_x * resolution) * (cell_y * resolution)
memory_MB = grid_points * 6 * 8 / 1e6  # 6 field components, 8 bytes each
```

## References

- [Meep Documentation](https://meep.readthedocs.io/)
- [Python API Reference](https://meep.readthedocs.io/en/latest/Python_User_Interface/)
- [Meep Tutorial](https://meep.readthedocs.io/en/latest/Python_Tutorials/Basics/)

---

**Pro Tip:** Start with low resolution (5-10) for quick tests, then increase (20-40) for final results!
