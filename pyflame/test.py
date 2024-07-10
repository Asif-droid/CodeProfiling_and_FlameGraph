import numpy as np

def print_out(x):
    print(x)

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b
def profile_me():
    
    x = np.array(range(10**7))
    y = np.array(np.random.uniform(0, 100, size=(10**7))) #
    z=add(x,y)
    m= np. array(range(10**7))
    a=subtract(z,m)
    print_out(a)
    print_out('ended')
if __name__=="__main__":    
    profile_me()
    
    
# call: python3 -m pyflame -p ./flamegraph.pl -o ./outfile.svg  test.py