"""
Meep Helper Functions for Testing and Analysis
Jeremy Howard Style: Write tests, know what to expect!
"""

import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple, Dict, Any


class WaveguideTests:
    """Test utilities for waveguide simulations."""

    def __init__(self, tolerance: float = 0.1):
        """
        Initialize test suite.

        Parameters:
        -----------
        tolerance : float
            Acceptable deviation from expected values (default 10%)
        """
        self.tolerance = tolerance
        self.results = []

    def test_confinement_factor(self, field_data: np.ndarray,
                               waveguide_width: float,
                               cell_size: Any,
                               expected: float = 0.8) -> bool:
        """
        Test if light is confined to the waveguide.

        Expected: > 80% of power in waveguide for good confinement.

        Parameters:
        -----------
        field_data : ndarray
            2D array of field values (Ez)
        waveguide_width : float
            Width of the waveguide in micrometers
        cell_size : mp.Vector3
            Size of the computational cell
        expected : float
            Minimum expected confinement factor (0-1)

        Returns:
        --------
        bool : True if test passes
        """
        ny = field_data.shape[1]
        y_positions = np.linspace(-cell_size.y/2, cell_size.y/2, ny)

        # Power is proportional to |E|²
        power = np.abs(field_data)**2
        total_power = np.sum(power)

        # Power in waveguide
        mask = np.abs(y_positions) < waveguide_width/2
        waveguide_power = np.sum(power[:, mask])

        gamma = waveguide_power / total_power
        passed = gamma >= expected

        result = {
            'test': 'Confinement Factor',
            'measured': gamma,
            'expected': f'>= {expected}',
            'passed': passed,
            'message': f"Γ = {gamma:.1%} ({'PASS' if passed else 'FAIL'})"
        }
        self.results.append(result)

        return passed

    def test_single_mode_condition(self, width: float,
                                   wavelength: float,
                                   n_core: float,
                                   n_cladding: float = 1.0) -> bool:
        """
        Test if waveguide operates in single-mode regime.

        Expected: V-number < π/2 for single mode.

        Parameters:
        -----------
        width : float
            Waveguide width in micrometers
        wavelength : float
            Vacuum wavelength in micrometers
        n_core : float
            Refractive index of waveguide core
        n_cladding : float
            Refractive index of cladding (default: 1.0 for air)

        Returns:
        --------
        bool : True if single-mode
        """
        V = (np.pi * width / wavelength) * np.sqrt(n_core**2 - n_cladding**2)
        cutoff = np.pi / 2
        passed = V < cutoff

        result = {
            'test': 'Single-Mode Condition',
            'measured': V,
            'expected': f'< {cutoff:.3f}',
            'passed': passed,
            'message': f"V = {V:.3f} ({'Single-mode PASS' if passed else 'Multi-mode FAIL'})"
        }
        self.results.append(result)

        return passed

    def test_field_amplitude(self, field_data: np.ndarray,
                            min_val: float = 1e-6,
                            max_val: float = 1e3) -> bool:
        """
        Test if field amplitude is in reasonable range.

        Expected: Non-zero but not infinite.

        Parameters:
        -----------
        field_data : ndarray
            Field values
        min_val : float
            Minimum acceptable amplitude
        max_val : float
            Maximum acceptable amplitude

        Returns:
        --------
        bool : True if in range
        """
        max_field = np.max(np.abs(field_data))
        passed = min_val < max_field < max_val

        result = {
            'test': 'Field Amplitude',
            'measured': max_field,
            'expected': f'{min_val} < |E| < {max_val}',
            'passed': passed,
            'message': f"|Ez|_max = {max_field:.4f} ({'PASS' if passed else 'FAIL'})"
        }
        self.results.append(result)

        return passed

    def test_steady_state(self, simulation_time: float,
                         frequency: float,
                         min_cycles: float = 10) -> bool:
        """
        Test if simulation ran long enough for steady-state.

        Expected: At least 10 optical cycles.

        Parameters:
        -----------
        simulation_time : float
            Total simulation time
        frequency : float
            Source frequency
        min_cycles : float
            Minimum number of cycles needed

        Returns:
        --------
        bool : True if sufficient time
        """
        cycles = simulation_time * frequency
        passed = cycles >= min_cycles

        result = {
            'test': 'Steady-State Convergence',
            'measured': cycles,
            'expected': f'>= {min_cycles}',
            'passed': passed,
            'message': f"{cycles:.1f} cycles ({'PASS' if passed else 'WARNING: may not converge'})"
        }
        self.results.append(result)

        return passed

    def test_resolution(self, resolution: float,
                       wavelength: float,
                       min_ppw: float = 8) -> bool:
        """
        Test if resolution is sufficient.

        Expected: At least 8 pixels per wavelength (better: 10-20).

        Parameters:
        -----------
        resolution : float
            Pixels per micrometer
        wavelength : float
            Smallest wavelength in simulation
        min_ppw : float
            Minimum pixels per wavelength

        Returns:
        --------
        bool : True if sufficient resolution
        """
        ppw = resolution * wavelength
        passed = ppw >= min_ppw

        result = {
            'test': 'Resolution',
            'measured': ppw,
            'expected': f'>= {min_ppw}',
            'passed': passed,
            'message': f"{ppw:.1f} pixels/wavelength ({'PASS' if passed else 'FAIL: too coarse'})"
        }
        self.results.append(result)

        return passed

    def print_report(self):
        """Print a formatted test report."""
        print("\n" + "="*70)
        print("SIMULATION TEST REPORT")
        print("="*70)

        for i, result in enumerate(self.results, 1):
            status = "✓" if result['passed'] else "✗"
            print(f"\n{status} Test {i}: {result['test']}")
            print(f"  Measured: {result['measured']}")
            print(f"  Expected: {result['expected']}")
            print(f"  {result['message']}")

        passed_count = sum(r['passed'] for r in self.results)
        total_count = len(self.results)

        print("\n" + "="*70)
        print(f"SUMMARY: {passed_count}/{total_count} tests passed")

        if passed_count == total_count:
            print("🎉 ALL TESTS PASSED!")
        else:
            print("⚠️  Some tests failed - review results above")
        print("="*70 + "\n")


class WaveguideAnalysis:
    """Analysis tools for waveguide simulations."""

    @staticmethod
    def calculate_effective_index(field_data: np.ndarray,
                                  cell_size: Any,
                                  wavelength_vacuum: float) -> float:
        """
        Calculate effective refractive index from field pattern.

        Measures spatial frequency of the field oscillation.

        Parameters:
        -----------
        field_data : ndarray
            2D field data
        cell_size : mp.Vector3
            Simulation cell size
        wavelength_vacuum : float
            Vacuum wavelength

        Returns:
        --------
        float : Effective index n_eff
        """
        # Take cross-section along x at y=0
        mid_y = field_data.shape[1] // 2
        field_x = field_data[:, mid_y]

        # FFT to find spatial frequency
        fft = np.fft.fft(field_x)
        freqs = np.fft.fftfreq(len(field_x), d=cell_size.x/len(field_x))

        # Find dominant spatial frequency (skip DC)
        dominant_idx = np.argmax(np.abs(fft[1:])) + 1
        k_x = 2 * np.pi * freqs[dominant_idx]

        # Effective index
        k_0 = 2 * np.pi / wavelength_vacuum
        n_eff = k_x / k_0

        return abs(n_eff)

    @staticmethod
    def measure_decay_length(field_data: np.ndarray,
                            waveguide_width: float,
                            cell_size: Any) -> float:
        """
        Measure evanescent decay length outside waveguide.

        Finds 1/e decay distance.

        Parameters:
        -----------
        field_data : ndarray
            2D field data
        waveguide_width : float
            Waveguide width
        cell_size : mp.Vector3
            Cell size

        Returns:
        --------
        float : Decay length in micrometers
        """
        mid_x = field_data.shape[0] // 2
        cross_section = np.abs(field_data[mid_x, :])

        y = np.linspace(-cell_size.y/2, cell_size.y/2, len(cross_section))

        # Find edge of waveguide
        edge_idx = np.argmin(np.abs(y - waveguide_width/2))
        edge_field = cross_section[edge_idx]

        # Find 1/e point
        target = edge_field / np.e

        # Look outside waveguide
        outside_idx = edge_idx + np.argmin(np.abs(cross_section[edge_idx:] - target))

        decay_length = abs(y[outside_idx] - y[edge_idx])
        return decay_length

    @staticmethod
    def plot_mode_profile(field_data: np.ndarray,
                         waveguide_width: float,
                         cell_size: Any,
                         title: str = "Mode Profile"):
        """
        Plot the waveguide mode profile.

        Shows field distribution and decay.

        Parameters:
        -----------
        field_data : ndarray
            2D field data
        waveguide_width : float
            Waveguide width
        cell_size : mp.Vector3
            Cell size
        title : str
            Plot title
        """
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

        # Plot 1: 2D field
        extent = [-cell_size.x/2, cell_size.x/2, -cell_size.y/2, cell_size.y/2]
        im = ax1.imshow(field_data.T, extent=extent, cmap='RdBu',
                       origin='lower', aspect='auto')
        ax1.axhline(y=waveguide_width/2, color='white', linestyle='--', alpha=0.5)
        ax1.axhline(y=-waveguide_width/2, color='white', linestyle='--', alpha=0.5)
        ax1.set_xlabel('x (μm)')
        ax1.set_ylabel('y (μm)')
        ax1.set_title('Field Pattern')
        plt.colorbar(im, ax=ax1)

        # Plot 2: Cross-section
        mid_x = field_data.shape[0] // 2
        y = np.linspace(-cell_size.y/2, cell_size.y/2, field_data.shape[1])
        field_cross = np.abs(field_data[mid_x, :])

        ax2.plot(y, field_cross, 'b-', linewidth=2)
        ax2.axvline(x=waveguide_width/2, color='r', linestyle='--', label='Waveguide edge')
        ax2.axvline(x=-waveguide_width/2, color='r', linestyle='--')
        ax2.fill_between([-waveguide_width/2, waveguide_width/2],
                        0, np.max(field_cross), alpha=0.2)
        ax2.set_xlabel('y (μm)')
        ax2.set_ylabel('|Ez|')
        ax2.set_title('Cross-section at x=0')
        ax2.legend()
        ax2.grid(True, alpha=0.3)

        plt.suptitle(title, fontsize=14, fontweight='bold')
        plt.tight_layout()
        plt.show()


def quick_waveguide_simulation(width: float = 1.0,
                               frequency: float = 0.15,
                               epsilon: float = 12,
                               resolution: int = 10,
                               runtime: float = 200) -> Dict[str, Any]:
    """
    Run a quick waveguide simulation with default parameters.

    Jeremy Howard style: One function to run everything!

    Parameters:
    -----------
    width : float
        Waveguide width in micrometers
    frequency : float
        Source frequency (Meep units)
    epsilon : float
        Waveguide permittivity
    resolution : int
        Pixels per micrometer
    runtime : float
        Simulation time

    Returns:
    --------
    dict : Contains simulation object and field data

    Example:
    --------
    >>> results = quick_waveguide_simulation(width=1.0, frequency=0.15)
    >>> results['tests'].print_report()
    """
    import meep as mp

    # Setup
    cell_size = mp.Vector3(16, 8, 0)
    pml_layers = [mp.PML(thickness=1.0)]

    geometry = [
        mp.Block(
            size=mp.Vector3(mp.inf, width, mp.inf),
            center=mp.Vector3(0, 0, 0),
            material=mp.Medium(epsilon=epsilon)
        )
    ]

    sources = [
        mp.Source(
            src=mp.ContinuousSource(frequency=frequency),
            component=mp.Ez,
            center=mp.Vector3(-7, 0, 0)
        )
    ]

    # Create and run simulation
    sim = mp.Simulation(
        cell_size=cell_size,
        geometry=geometry,
        sources=sources,
        boundary_layers=pml_layers,
        resolution=resolution
    )

    print("🚀 Running simulation...")
    sim.run(until=runtime)
    print("✅ Simulation complete!")

    # Get field data
    ez_data = sim.get_array(center=mp.Vector3(0, 0, 0),
                           size=cell_size, component=mp.Ez)
    eps_data = sim.get_array(center=mp.Vector3(0, 0, 0),
                            size=cell_size, component=mp.Dielectric)

    # Run tests
    tests = WaveguideTests()
    wavelength = 1 / frequency
    n_core = np.sqrt(epsilon)

    tests.test_resolution(resolution, wavelength/n_core, min_ppw=8)
    tests.test_single_mode_condition(width, wavelength, n_core)
    tests.test_field_amplitude(ez_data)
    tests.test_confinement_factor(ez_data, width, cell_size, expected=0.7)
    tests.test_steady_state(runtime, frequency, min_cycles=10)

    return {
        'sim': sim,
        'ez_data': ez_data,
        'eps_data': eps_data,
        'tests': tests,
        'params': {
            'width': width,
            'frequency': frequency,
            'epsilon': epsilon,
            'wavelength': wavelength,
            'n_core': n_core
        }
    }


if __name__ == "__main__":
    print("Meep Helper Functions")
    print("=" * 50)
    print("\nUsage:")
    print("  from meep_helpers import quick_waveguide_simulation")
    print("  results = quick_waveguide_simulation()")
    print("  results['tests'].print_report()")
    print("\nOr run individual tests:")
    print("  tests = WaveguideTests()")
    print("  tests.test_single_mode_condition(width=1.0, wavelength=6.67, n_core=3.46)")
    print("  tests.print_report()")
