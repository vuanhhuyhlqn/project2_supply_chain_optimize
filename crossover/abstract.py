import numpy as np
from task import Task
from plant import Plant
from dc import DC
from retailer import Retailer
from customer import Customer
from indi import Individual

class AbstractCrossover:
    def __init__(self):
        pass
    def __call__(self, pa: Individual, pb: Individual) -> Individual:
        pass