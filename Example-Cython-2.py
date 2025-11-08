"""
Example 2: Monte Carlo Simulation to Calculate PI (Cython)
"""

import time
from cython_mods.monte_carlo import monte_carlo_pi


NUM_SAMPLES = 100000000


if __name__ == "__main__":
    start_time = time.time()
    pi_estimate = monte_carlo_pi(num_samples=NUM_SAMPLES)
    end_time = time.time()

    print(f"Monte Carlo Simulation for PI with {NUM_SAMPLES} samples:")
    print(f"\t- Estimated PI (Cython): {pi_estimate}")
    print(f"\t- Execution Time (Cython): {end_time - start_time:.5f} (sec)")
