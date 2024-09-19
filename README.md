## Code profiling
Code profiling is a crucial aspect of performance optimization and debugging in software development. It involves the analysis of a program's runtime behavior to identify performance bottlenecks, memory usage issues, and other inefficiencies. Profiling provides detailed insights into how a program executes, which functions consume the most time, and how resources are utilized during execution.
## Flame graph:
Flame graphs are a powerful visualization tool used to represent the performance profile of software applications. They are particularly useful for understanding where an application spends most of its time during execution, helping to identify performance bottlenecks and optimize code.
# cProfiler
* # Installation
cProfile, pstats are already installed with python need to install tuna to visalize call stack
``` console 
pip install tuna
``` 

* # usage
` import cProfile,pstats ` at the top
``` console

with cProfile.Profile() as profile: 

    # call main function here 

results=pstats.Stats(profile)
results.sort_stats(pstats.SortKey.TIME)
results.dump_stats('results.prof')
# results.print_stats()
```
Run the python scripts normally with ` python <script.py>`

` results.print_stats() ` will print all the functions, their runtime and number of calls.

` results.dump_stats('results.prof') ` will create a profile file that can be viewd using tuna
``` console
tuna <path_to_results.prof>
```
* # For jupyter notebook
same just change the results.prof file path to drive and after downloading the ` results.prof` file it can be opend in the same way with tuna.
# Memory Profiler

* # Installation
```console
pip install memory_profiler
```
* # Usage
` from memory_profiler import profile, memory_usage ` to import memory profiler
``` console
out_file=open("path_to_output.log","w+")

# codes/funcs not need to be profiled

#funcs need to be profiled
@profile(stream = out_file)
def func1():

#funcs need to be profiled
@profile(stream = out_file)
def func2():

...
main()
```
Run the python scripts normally with ` python <script.py>`

The log file will show the memory usage of that function line by line.

# [Pyflame](https://pypi.org/project/pyflame/)
* # Installation
``` console
python -m pip install pyflame 
//or 
pip install pyflame
```
Download [flamegraph.pl](https://github.com/brendangregg/FlameGraph/blob/master/flamegraph.pl) to generate flame graph.
* # Usage
No need to change anything the code. Just run the python script using this command.
``` console
python3 -m pyflame -p <path_to_flamegraph.pl> -o <path_to_output_file.svg>  <main_script.py>
```
Open the svg file with borwser for better understanding of the call stack.

# [Scalene](https://pypi.org/project/scalene/0.7.13/)
* # Installation
``` console
python3 -m pip install -U scalene
```
* # Usage
There are lots of options available with scalene.
to see run ` scalene -h `

- Example: CPU, GPU and memory profiling and output in html
``` console
scalene --html --outfile <path_to_output.html>  <main_script.py>
```
* # For jupyter notebook
* Installation:
` pip install scalene`
* load scalene ` %load_ext scalene`
* Usage:add ` %%scalene` at the top of the cell that has to be profiled
``` console
%%scalene
def profile_me():
    x = np.array(range(10**7))
    y = np.array(np.random.uniform(0, 100, size=(10**7)))
    z=x+y
    m= np. array(range(10**7))
    a=z-m
    print(a)
    print('ended')

profile_me()
```
Running the cell will generate a result of cpu runtime for the cell. Memory profiling is not available in .ipynb files. 

- Note: Most of the profiling was done in wsl and linux machine. There are some limitations in windows. 
