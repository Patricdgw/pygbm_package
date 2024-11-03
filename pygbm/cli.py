
# Import the click library for creating command-line interfaces
import click
import matplotlib.pyplot as plt

#from .base import Simulation

from GBM import GBMSimulator


# Define a command-line group using the click librarycl
@click.group()
def cli():
    pass

# Define a command-line command using the click library
@cli.command()
# Define an option for the command with a default value and a help message
@click.option('--y0', default=100.0, help='Initial stock price')
# Define an option for the drift coefficient with a default value and a help message
@click.option('--mu', default=0.1, help='Drift coefficient')
# Define an option for the volatility coefficient with a default value and a help message
@click.option('--sigma', default=0.05, help='Volatility coefficient')
# Define an option for the time step with a default value and a help message
@click.option('--t', default=1/252, help='Time step')
# Define an option for the number of steps to simulate with a default value and a help message
@click.option('--n', default=252, help='Number of steps to simulate')
# Define an option for the output file
@click.option('--output', default='gbm_plot.png', help='Output file for the plot')
# Define the main function that will be executed when the command is run
def simulate(y0, mu, sigma, t, n, output):

    # Debugging statements to print the values of the options
    print(f'y0: {y0}, mu: {mu}, sigma: {sigma}, t: {t}, n: {n}, output: {output}')
    
    # Create an instance of the GeometricBrownianMotion class with the provided parameters
    gbm = GBMSimulator(y0, mu, sigma)
    # Simulate the stock prices for the given number of steps
    times, prices = gbm.simulate_path(t, n)
    # Plot the simulated prices
    plt.plot(times, prices)
    plt.xlabel('Time Steps')
    plt.ylabel('Stock Price')
    plt.title('Geometric Brownian Motion Simulation')
    # Save the plot to the specified output file
    plt.savefig(output)
    print(f'Plot saved to {output}')

if __name__ == '__main__':
    cli()