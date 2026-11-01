#!/bin/sh
set -eu
gcc -std=c11 -Wall -Wextra -pthread process_thread_benchmark.c -o benchmark
mkdir -p results
: > results/benchmark_trials.txt
i=1
while [ "$i" -le 5 ]; do
  echo "TRIAL $i" | tee -a results/benchmark_trials.txt
  ./benchmark | tee -a results/benchmark_trials.txt
  i=$((i+1))
done
echo "For Task06, run: (cd ../Task06 && strace -c ./file_copy && /usr/bin/time -v ./file_copy)"
