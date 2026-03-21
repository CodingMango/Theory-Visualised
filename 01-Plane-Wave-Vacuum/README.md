# 🌌 Electromagnetic Plane Wave: The Cosmic Tango

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![VPython](https://img.shields.io/badge/VPython-7.x-orange.svg)](https://vpython.org/)
![Physics](https://img.shields.io/badge/Physics-Electromagnetism-success.svg)

## 🔭 Look Around You...
Right now, the space between your eyes and this screen looks empty. It isn't. It is boiling with a chaotic, invisible ocean of energy. The Wi-Fi connecting your device, the radio station playing a town over, the cellular signals piercing the walls, and the very light illuminating your room—they are all doing exactly what you see in this simulation. 

Welcome to the anatomy of an **Electromagnetic Plane Wave**.

I built this 3D VPython simulation to take the abstract math of Maxwell's equations and make it visible, interactive, and undeniable. 

## 🔬 The Physics: What Are You Looking At?

When a charged particle accelerates in the universe, it creates a ripple. A changing electric field gives birth to a changing magnetic field, which in turn gives birth to another electric field. They become locked in a self-sustaining loop, pushing each other across the cosmos at the speed of light. 

Here is how that cosmic leapfrog is mapped in this simulation:

### 1. The Orthogonal Rule (Transverse Waves)
Nature demands that these fields respect each other's space. They must be mutually perpendicular. 
* **The Electric Field (E - Blue):** Oscillates vertically along the Y-axis.
  > **E**(z,t) = **ĵ** E₀ sin(kz − ωt)

* **The Magnetic Field (B - Red):** Oscillates horizontally along the X-axis.
  > **B**(z,t) = −**î** B₀ sin(kz − ωt)

### 2. The Coincidence (In-Phase Oscillation)
Common sense tells us that in a vibrating system (like a pendulum), when one property is at its maximum, the other is at zero. *Not here.* In a pure vacuum, the Electric and Magnetic fields peak at the exact same moment and die out at the exact same moment. They are perfectly in phase.

### 3. The Pulsing of Power (The Poynting Vector)
Look at the **Yellow arrows** propagating forward along the Z-axis. This is the **Poynting Vector (S)**, representing the actual directional flow of the wave's energy.
  > **S** = (1 / μ₀) (**E** × **B**)

Because it is the cross-product of two sine waves (resulting in a sin² wave), the energy doesn't flow like a smooth, steady river. It *pulses*. It surges from zero to a positive maximum over and over, carrying literal momentum through the void.

## ⚠️ Simulation Limitations

While the math driving this simulation is strict, I had to break one fundamental rule of physics so you could actually see the wave. 

**The Magnetic Field Scaling**
In our physical universe, the magnitude of the electric field (E) and the magnetic field (B) are related by the speed of light (c):
  > B = E / c

Because the speed of light is so massive (3 × 10⁸ m/s), the magnetic component of an EM wave is *microscopically small* compared to the electric component when measured in standard units (Teslas vs. Volts/meter). 

If I rendered this simulation with strict real-world magnitudes, the blue Electric Field would fill your screen, and the red Magnetic Field would be so incredibly tiny it wouldn't even render a single pixel. 

**For the sake of visualisation, the magnitude of B has been artificially scaled up (C = A in the code), so both fields are equally visible.** Furthermore, this simulates an **ideal vacuum**. In the messy reality of the real world (passing through walls, atmosphere, or copper), waves experience *attenuation* (losing energy to heat) and *dispersion* (slowing down). This simulation models the perfect, eternal journey of light through deep space.

## ⚙️ Interactive Controls
Run the script, and use the on-screen sliders to play god with the universe:
* **Amplitude:** Watch how increasing the height of the fields drastically increases the size of the Poynting vector (representing a brighter light or a stronger signal).
* **Wavelength (λ):** Stretch or compress the spatial footprint of the wave.
* **Frequency (ω):** Speed up the cosmic vibration. 

## 🚀 Quick Start Guide

Get the simulation running locally in just a few steps:

1. **Install Python**: Ensure you have Python 3.x installed on your system.
2. **Install Dependencies**: Open your terminal or command prompt and install the VPython library:
   ```bash
   pip install vpython   
3. Run `python EM-planeWave-vector.py`
4. *Right-click and drag to rotate the camera in 3D space.*

