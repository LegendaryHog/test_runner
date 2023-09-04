#!/usr/bin/env python3

import sys, math, re, os, time
from termcolor import colored

LEN_DOTS = 61

def print_dots(len_name):
    for i in range(LEN_DOTS - len_name):
        print('.', end='')

def run_tests(exe, test_names, test_cmp):
    passed = 0
    total_time = 0.0

    for test_name in test_names:
        start = time.perf_counter()
        os.system('./' + exe + ' < ' + test_name + ' > tmp')
        end = time.perf_counter()
        time_res = end - start

        file_result = open('tmp', 'r')
        file_answer = open(test_name + '.ans', 'r')

        pair = test_cmp(file_result, file_answer)
        passed += pair[0]
        output = pair[1]
        print(test_name + ' ', end='')
        print_dots(LEN_DOTS - len(test_name))
        if pair[0] == 0:
            print(colored('   Failed    ', 'red'), end='')
            print(output)
        else:
            print(colored('   Passed    ', 'green'), end='')
        print(str(round(time_res), 2))
        
        total_time += time_res

    number_of_tests = len(test_names)
    final_output = str(int(float(passed)/float(number_of_tests) * 100.0)) + '% tests passed'
    print()
    color = ''
    if passed == number_of_tests:
        color = 'green'
    else:
        color = 'red'
    print(colored(final_output, color) + ', ' + str(number_of_tests - passed) + ' tests failed out of ' + str(number_of_tests))
    print('\nTotal Test time (real) = ' + str(round(total_time, 2)) + ' sec')