import numpy as np
from ..base import Simulation  

import matplotlib as plt

class GBMSimulator(Simulation):
    def __init__(self, start_price, mu, sigma):
        super().__init__(start_price, mu, sigma)


    def simulate_path(self, T, N):
        prices = [self.start_price]
        times = [0]
        drift = self.mu * T/N
        print(f'time: {times[-1]}, price: {prices[-1]}')
        for i in range(N):
            jump = 0.5 * self.sigma * np.random.choice([1, -1]) * np.sqrt(T/N)
            times.append(i+1)
            prices.append(prices[-1] + drift - jump)

            print(f'time: {times[-1]}, price: {prices[-1]}')
        return times, prices
    

    