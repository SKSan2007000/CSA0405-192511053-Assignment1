# Task 10 – Measure and Compare
## Run
```bash
gcc -std=c11 -Wall -Wextra -pthread process_thread_benchmark.c -o benchmark
./run_all.sh
```
The program sequentially creates and reaps 1,000 processes with fork()/waitpid(), then creates and joins 1,000 pthreads. It uses CLOCK_MONOTONIC. Five raw trials are written to `results/benchmark_trials.txt`.
## Additional required measurements
```bash
cd ../Task06
strace -c ./file_copy
/usr/bin/time -v ./file_copy
```
Record user time, system time, elapsed time, maximum resident set size and the read() row from strace. Run at least five trials, calculate median values, and note WSL2/host load and file-cache state.
## Interpretation
Threads often have lower startup overhead and share address space, while processes have separate virtual address spaces and stronger isolation. Do not assume threads always win: results depend on OS, CPU, memory, scheduler, thread stack defaults and WSL2. Compare actual measurements from your laptop.
