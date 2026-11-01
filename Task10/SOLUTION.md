# TASK 10 – Measure and Compare

## Measurements and evidence

The repository's benchmark creates and reaps 1,000 child processes using fork()/waitpid(), then creates and joins 1,000 pthreads using pthread_create()/pthread_join(). It uses CLOCK_MONOTONIC and records five trials in `Task10/results/benchmark_trials.txt`. Those sample values were collected in the package-preparation environment and are included only to verify that the benchmark runs; they are not the student's laptop measurements. Run `Task10/run_all.sh` on Ubuntu/WSL2 and replace the file with the local five or more trials.

## System-call and CPU timing

For Task 6, run `strace -c ./file_copy` to capture system-call counts and `/usr/bin/time -v ./file_copy` to capture elapsed, user and system time and maximum resident set size. Record the `read` row from strace, the program's own read() count, and the buffer size. Run multiple trials, report medians and state the Linux distribution, kernel, GCC version, WSL2 status and system load. The program's counter may differ from strace's total because strace includes runtime calls outside copy_file.

## Alternative: threads versus processes

Threads often start faster because they share the process address space and need less separate memory-management state. Processes have stronger address-space isolation and may use copy-on-write after fork. A thread stack and thread metadata still consume memory; process address spaces may share physical pages until modified. The measured winner depends on kernel, CPU, scheduler, memory pressure and whether process creation is sequential or concurrent. The benchmark measures a specific create-and-join pattern, not every possible workload.

## Complexity

For N creations, the benchmark performs O(N) create/join or fork/wait operations. Timing is empirical; do not extrapolate a single run linearly without repeated measurements and confidence about workload conditions.
