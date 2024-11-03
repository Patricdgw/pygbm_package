class pygbm:
    """
    Base class for Geometric Brownian Motion (GBM) simulation.

    Attributes:
        start_price (float): Initial stock price.
        mu (float): Drift coefficient.
        sigma (float): Volatility coefficient.
    """
    def __init__(self, start_price, mu, sigma):
        """
        Initializes the pygbm class with the given parameters.

        Args:
            start_price (float): Initial stock price.
            mu (float): Drift coefficient.
            sigma (float): Volatility coefficient.
        """
        self.start_price = start_price
        self.mu = mu
        self.sigma = sigma

    def simulate_path(self):
        """
        Simulates the stock price path. This method should be overridden by subclasses.

        Raises:
            NotImplementedError: If the method is not overridden by a subclass.
        """
        raise NotImplementedError("This method should be overridden by subclasses")

