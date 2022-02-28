import time
import sys
import subprocess

for line in sys.stdin: # a list of program in a file (see list.txt)
    cmd = line[:-1].split(' ')

    print(f'program = {line[:-1]}')
    t = time.perf_counter() # start time
    x = subprocess.call(cmd)  # just run with all outputs to stdout
    t = time.perf_counter() - t # end time

    # print out messages
    print(f'execution time = {t:02f} sec\nreturn value = {x}\n')

