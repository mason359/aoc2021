#!/usr/bin/env python

import sys, time, requests
from os.path import exists

def run_problem(d, p):
    download_input(d)
    day = __import__(f'day{d}')
    problem = day.problem1 if p == 1 else day.problem2
    start = time.perf_counter()
    result = problem()
    end = time.perf_counter()
    print(f'Day {d}, Problem {p}:')
    print(f'Result: {result}')
    print(f'Finished in {end - start:0.6f}s\n')
    return end - start

def download_input(d):
    if not exists(f'input/input{d}.txt'):
        with open('session') as fh:
            session_id = fh.read()
        request = requests.get(f'https://adventofcode.com/2021/day/{1}/input', cookies={'session': session_id})
        with open(f'input/input{d}.txt', 'wb') as fh:
            fh.write(request.content)

if __name__ == "__main__":
    run_problem(int(sys.argv[1]), int(sys.argv[2]))
