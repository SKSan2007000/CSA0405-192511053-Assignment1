#!/bin/sh
set -eu
gcc -std=c11 -Wall -Wextra -pthread process_thread_benchmark.c -o benchmark
./benchmark
