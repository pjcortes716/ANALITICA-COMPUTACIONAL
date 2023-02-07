from multiprocessing import Pool
import time
import math

N = 5000000

def cube(x):
    return x**3+math.sqrt(x)+x**2+x

if __name__ == "__main__":
    