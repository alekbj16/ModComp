# -*- coding: utf-8 -*-
"""
Title:      Modcomp ex 1
Author:     Aleksander B. Jakobsen
Created:    Wed Dec  2 12:55:51 2020


"""
import numpy as np


class RandomWalkEpidemicSimulator:
    """
    Class used to model the spreading of a contagious disease in a
    population of individuals with a 2D random walk.

    Each walker has a disease status which is represented by an 
    integer Enum. Also, a set of integer (x, y)-coordinates are 
    stored for each walker. The possible coordinates are:

        {0, 1, ..., Lx-1} in the x-direction
        {0, 1, ..., Ly-1} in the y-direction

    It is only possible to move North, South, East, or West. If a 
    walker attempts to move outside of the physical domain, nothing 
    happens (i.e., a "bounce-back boundary condition" is enforced).
    """
    def __init__(self,
                 population_size,
                 no_init_infected=1,
                 nx=50,
                 ny=50,
                 q=0.9):
        """
        :param population_size: The total number of people (N).
        :param no_init_infected: The number of infected people at t=0.
        :param nx: The number of lattice nodes in the x-direction 
        :param ny: The number of lattice nodes in the y-direction.
        :param q: The probability of infection (0 <= q <= 1).
        """
        self.N_ = population_size
        self.I0_= no_init_infected
        self.nx_= nx
        self.ny_= ny
        self.infection_probability_ = q
        
        #Position of Walkers
        self.Walkers_ = np.random.randint(0,
                                         [self.nx_, self.ny_],
                                         size = (self.N_, 2))