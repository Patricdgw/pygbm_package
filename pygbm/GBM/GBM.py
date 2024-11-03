import numpy as np
from pygbm.base import pygbm  

import matplotlib as plt

   

class GBMSimulator(pygbm):
    """
    Class for simulating Geometric Brownian Motion (GBM) paths.

    Inherits from the pygbm base class.
    """
    def __init__(self, start_price, mu, sigma):
        """
        Initializes the GBMSimulator class with the given parameters.

        Args:
            start_price (float): Initial stock price.
            mu (float): Drift coefficient.
            sigma (float): Volatility coefficient.
        """
        super().__init__(start_price, mu, sigma)

    def simulate_path(self, T, N):
        """
        Simulates the stock price path using the GBM model.

        Args:
            T (float): Time horizon.
            N (int): Number of time steps.

        Returns:
            tuple: A tuple containing two lists - times and prices.
        """
        prices = [self.start_price]
        times = [0]
        dt = T / N
        drift = (self.mu - 0.5 * self.sigma **2) * dt
        print(f'time: {times[-1]}, price: {prices[-1]}')
        
        for i in range(N):
            # Calculate the random jump component
            jump =  self.sigma * np.random.normal(0, np.sqrt(dt))
            times.append(i + 1)
            prices.append(prices[-1] * np.exp((drift + jump)))
            print(f'time: {times[-1]}, price: {prices[-1]}')
        
        return times, prices    