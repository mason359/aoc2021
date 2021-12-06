#!/usr/bin/env python3.9

import sys, time, requests
from os.path import exists

def run_problem(d, p, do_submit=False):
    download_input(d)
    day = __import__(f'day{d}')
    problem = day.problem1 if p == 1 else day.problem2
    start = time.perf_counter()
    result = problem()
    end = time.perf_counter()
    print(f'Day {d}, Problem {p}:')
    print(f'Result: {result}')
    print(f'Finished in {end - start:0.6f}s\n')
    if do_submit:
        submit(d, p, result)
    return end - start

def download_input(d):
    if not exists(f'input/input{d}.txt'):
        with open('session') as fh:
            session_id = fh.read()
        request = requests.get(f'https://adventofcode.com/2021/day/{d}/input', cookies={'session': session_id})
        with open(f'input/input{d}.txt', 'wb') as fh:
            fh.write(request.content)

def submit(d, p, answer):
    url = f'https://adventofcode.com/2021/day/{d}/answer'
    payload = {'level': str(p), 'answer': str(answer)}
    with open('session') as fh:
        session_id = fh.read()
    response = str(requests.post(url, data=payload, cookies={'session': session_id}).content)
    if 'your answer is too high' in response:
        result = 'Too high'
    elif 'your answer is too low' in response:
        result = 'Too low'
    elif 'right answer' in response:
        result = 'Correct!'
    else:
        result = response
    print(f'Submitted: {result}')


if __name__ == "__main__":
    do_submit = len(sys.argv) >= 4 and sys.argv[3] == '-s'
    run_problem(int(sys.argv[1]), int(sys.argv[2]), do_submit)
