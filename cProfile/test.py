import numpy as np
import cProfile,pstats

def print_out(x):
    print(x)

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b
def profile_me():
    
    x = np.array(range(10**7))
    y = np.array(np.random.uniform(0, 100, size=(10**7)))
    z=add(x,y)
    m= np. array(range(10**7))
    a=subtract(z,m)
    print_out(a)
    print_out('ended')
    
    
with cProfile.Profile() as profile:
    #main functio call 
    profile_me()  
results=pstats.Stats(profile)
results.sort_stats(pstats.SortKey.TIME)
results.dump_stats('results.prof')
# results.print_stats()