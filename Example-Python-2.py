"""
Example 2: Monte Carlo Simulation to Calculate PI (Standard Python)
"""

import random
import time


NUM_SAMPLES = 100000000


def monte_carlo_pi(num_samples: int = NUM_SAMPLES):
    inside_circle = 0
    for _ in range(num_samples):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        if (x**2) + (y**2) <= 1:
            inside_circle += 1
    return (inside_circle / num_samples) * 4


if __name__ == "__main__":
    start_time = time.time()
    pi_estimate = monte_carlo_pi(num_samples=NUM_SAMPLES)
    end_time = time.time()

    print(f"Monte Carlo Simulation for PI with {NUM_SAMPLES} samples:")
    print(f"\t- Estimated PI (Python): {pi_estimate}")
    print(f"\t- Execution Time (Python): {end_time - start_time:.5f} (sec)")
