
# cProfiler
* # Installation
cProfile, pstats are already intalled with python need to install tuna to visalize call stack
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
There are lots of options available with scalene.
to see run ` scalene -h `

- Example: CPU, GPU and memory profiling and output in html
``` console
scalene --html --outfile <path_to_output.html>  <main_script.py>
```

* Note: Most of the profiling was done in wsl and linux machine. There are some limitations in windows.