import math

# Capacitance of a parallel-plate capacitor:
# C = ε₀ εr A / d

epsilon_0 = 8.854e-12  # Permittivity of free space (F/m)

area = float(input("Enter plate area (m²): "))
distance = float(input("Enter distance between plates (m): "))
relative_permittivity = float(input("Enter relative permittivity (εr): "))

capacitance = (epsilon_0 * relative_permittivity * area) / distance

print(f"\nCapacitance = {capacitance:.6e} F")
print(f"Capacitance = {capacitance * 1e12:.3f} pF")
