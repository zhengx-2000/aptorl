"""
A Programme to compile and run test C programmes automatically
several times, and finally display mean execution time for each one.
Modified from the previous version of Matthew Tang
Author: Xiao Zheng
"""
import time
import numpy as np
import subprocess

test_num = 1000
# code = ['add_rplc_multi1', 'add_rplc_multi2']
# code = ['break_if1', 'break_if2']
# code = ['for_loop1', 'for_loop2', 'for_loop3', 'for_loop4', 'for_loop5']
# code = ['Register_B', 'Register_O']
code = ['Double', 'Float', 'Int', 'Long', 'Short', 'UnsignedInt', 'UnsignedLong', 'UnsignedShort']
time_used = np.zeros([len(code), test_num])

for i in range(test_num):
    if i % 10 == 0:
        print(i)
    for j in range(len(code)):
        subprocess.call('gcc ' + code[j] + '.c -o ' + code[j], shell=True)  # To avoid results executed in previous
        # episodes influence next execution, the programmes have to be compiled each time before execution

        # print(f'program = {code[j]}')
        t = time.perf_counter()  # start time
        x = subprocess.call('./' + code[j])  # just run with all outputs to stdout
        t = time.perf_counter() - t  # end time
        time_used[j, i] = t

        # print out messages
        # print(f'execution time = {t:02f} sec\nreturn value = {x}\n')
for i in range(len(code)):
    print('mean time for code ' + code[i] + '.c in ' + str(test_num) + ' cases: ' + str(time_used[i].mean()))
