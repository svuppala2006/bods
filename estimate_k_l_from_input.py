import numpy as np
import argparse
import os

parser = argparse.ArgumentParser(description='This script takes in the workload, and returns the workload description.')
parser.add_argument('-f', '--file_name', help='The relative path for the workload file')

args = parser.parse_args()
try:
    f = open(args.argument, 'r')
except:
    print('The argument provided was invalid.')
    os.system('python3 estimate_k_l_from_input.py --help')
    exit()

vals = []
N = 0

for row in f:
    vals.append(int(row))
    N += 1
sorted_vals = np.sort(vals)
I = sorted_vals[0]
fixed_window = True
max_window = 0

prev_window = sorted_vals[1] - sorted_vals[0]
for i in range(1, N - 1):
    current_window = sorted_vals[i + 1] - sorted_vals[i]
    if(current_window != prev_window):
        fixed_window = False
    max_window = max([max_window, current_window])
    prev_window = current_window


arr_L = []    
for i in range(N):
    arr_L.append(int(abs(i - vals.index(sorted_vals[i]))))
L = max(arr_L)
K = np.count_nonzero(arr_L)
print(vals, end="\n\n")
print(f'N = {N}')
print(f'Start Index = {I}')
print(f'K = {K}')
print(f'L = {L}')
print(f'Fixed Window: {fixed_window}')
if(fixed_window):
    print(f'Window Size: {max_window}')
else:
    print(f'Max Window Size: {max_window}')