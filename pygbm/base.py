class pygbm:
    def __init__(self, start_price, mu, sigma):
        self.start_price = start_price
        self.mu = mu
        self.sigma = sigma
        

    def simulate_path(self): 
        raise NotImplementedError("This method should be overridden by subclasses")