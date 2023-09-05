import matplotlib.pyplot as plt
import random
class RandomWalk:
    def __init__(self,steps,dimantions):
        self.steps=steps
        self.dim=dimantions
        self.system=[[0for step in self.steps]for dim in self.dim]
    def walk(self):
        for step in range(1,self.steps):
            rand=random.randint(0,self.dim-1)
            for dim in range(self.dim):
                if dim==rand:
                    pass
                else:
                    pass
    def move(self):
        for