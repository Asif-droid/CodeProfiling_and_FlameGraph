import numpy as np
from memory_profiler import profile, memory_usage
import os

out_file=open('results.log','w+')
@profile(stream=out_file)
def profile_me():
    
    x = np.array(range(10**7))
    y = np.array(np.random.uniform(0, 100, size=(10**7)))
    z=x+y
    m= np. array(range(10**7))
    a=z-m
    print(a)
    print('ended')
if __name__=="__main__":    
    profile_me() # generates log file for both funcs
    profile_me()
    