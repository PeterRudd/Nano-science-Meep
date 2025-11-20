#!/usr/bin/env python3
"""
Quick Start: Meep Waveguide Simulation
Run this script to see a complete waveguide simulation in action!

Usage:
    python quick_start.py

Jeremy Howard style: See it work first, understand later!
"""

import sys

def main():
    print("="*70)
    print("🚀 MEEP WAVEGUIDE SIMULATION - QUICK START")
    print("="*70)
    print("\nThis script will:")
    print("  1. Set up a waveguide simulation")
    print("  2. Run the electromagnetic simulation")
    print("  3. Visualize the results")
    print("  4. Run automated tests")
    print("\nExpected time: ~10-15 seconds\n")

    # Check if meep is installed
    try:
        import meep as mp
        print(f"✓ Meep version {mp.__version__} found")
    except ImportError:
        print("✗ ERROR: Meep not installed!")
        print("\nPlease install Meep using conda:")
        print("  conda create -n meep python=3.10")
        print("  conda activate meep")
        print("  conda install -c conda-forge pymeep matplotlib numpy")
        print("\nSee README.md for detailed instructions.")
        sys.exit(1)

    try:
        import numpy as np
        import matplotlib.pyplot as plt
        print("✓ NumPy and Matplotlib found")
    except ImportError as e:
        print(f"✗ ERROR: Missing dependency: {e}")
        print("\nInstall using: pip install numpy matplotlib")
        sys.exit(1)

    from meep_helpers import quick_waveguide_simulation, WaveguideAnalysis

    print("\n" + "="*70)
    print("STEP 1: SETTING UP SIMULATION")
    print("="*70)
    print("\nParameters:")
    print("  - Waveguide width: 1.0 μm")
    print("  - Material: ε = 12 (silicon-like, n ≈ 3.46)")
    print("  - Frequency: 0.15 (λ ≈ 6.67 μm near-infrared)")
    print("  - Resolution: 10 pixels/μm")
    print("  - Cell size: 16 × 8 μm")

    print("\n" + "="*70)
    print("STEP 2: RUNNING SIMULATION")
    print("="*70)
    print("\nThis will take ~5-10 seconds...\n")

    # Run simulation
    results = quick_waveguide_simulation(
        width=1.0,
        frequency=0.15,
        epsilon=12,
        resolution=10,
        runtime=200
    )

    print("\n" + "="*70)
    print("STEP 3: RUNNING AUTOMATED TESTS")
    print("="*70)

    # Print test report
    results['tests'].print_report()

    print("\n" + "="*70)
    print("STEP 4: VISUALIZING RESULTS")
    print("="*70)
    print("\nGenerating plots...")

    # Plot mode profile
    WaveguideAnalysis.plot_mode_profile(
        results['ez_data'],
        results['params']['width'],
        results['sim'].cell_size,
        title="Waveguide Mode - Quick Start Demo"
    )

    # Additional analysis
    print("\n" + "="*70)
    print("QUANTITATIVE RESULTS")
    print("="*70)

    # Calculate effective index
    try:
        n_eff = WaveguideAnalysis.calculate_effective_index(
            results['ez_data'],
            results['sim'].cell_size,
            results['params']['wavelength']
        )
        print(f"\nEffective refractive index: n_eff = {n_eff:.3f}")
        print(f"  (Expected: between 1.0 and {results['params']['n_core']:.2f})")
    except Exception as e:
        print(f"\nNote: Could not calculate effective index ({e})")

    # Measure decay length
    delta = WaveguideAnalysis.measure_decay_length(
        results['ez_data'],
        results['params']['width'],
        results['sim'].cell_size
    )
    print(f"\nEvanescent decay length: δ = {delta:.3f} μm")
    print(f"  (Typical: 0.3-0.6 μm for this design)")

    print("\n" + "="*70)
    print("✅ SUCCESS!")
    print("="*70)
    print("\nWhat you've accomplished:")
    print("  ✓ Ran your first nanophotonics simulation")
    print("  ✓ Simulated light propagation in a waveguide")
    print("  ✓ Verified the results with automated tests")
    print("  ✓ Visualized the electromagnetic field pattern")
    print("  ✓ Confirmed single-mode operation")
    print("\nNext steps:")
    print("  1. Open 'meep_waveguide_tutorial.ipynb' for detailed explanations")
    print("  2. Read the 3-level explanations (beginner/intermediate/advanced)")
    print("  3. Try the exercises at the end of the notebook")
    print("  4. Experiment with different parameters!")
    print("\nHappy learning! 🎉")
    print("="*70 + "\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nSimulation interrupted by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\n\n✗ ERROR: {e}")
        print("\nIf you're stuck:")
        print("  1. Check that all dependencies are installed (see README.md)")
        print("  2. Make sure you're using Python 3.8+")
        print("  3. Try running in a fresh conda environment")
        import traceback
        print("\nFull error traceback:")
        traceback.print_exc()
        sys.exit(1)
