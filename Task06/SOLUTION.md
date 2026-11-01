# TASK 6 – Evaluate the Cost of System Calls

## Completed code and measured call counts

`Task06/file_copy.c` completes the supplied TODO using open(), read(), write() and close(). It validates the requested buffer size, retries interrupted reads/writes, handles partial writes and counts each read attempt. For the supplied 10,000-byte file, the verified program output is: buffer 1 byte → 10,001 read() calls; buffer 512 bytes → 21 calls; buffer 4096 bytes → 4 calls. The extra call is the final read that returns EOF. These are exact expected counts for the supplied loop.

## Interpretation and recommendation

A system call is more expensive than an ordinary function call because it requires a privilege transition, validation, kernel work and a return transition; it may also block or cause scheduling. Larger buffers reduce transitions: the call count is approximately ceil(n/b)+1 for this loop, so it grows as O(n/b). Copying n bytes remains O(n) time and the buffer uses O(b) space. For this small experiment, 4096 bytes makes far fewer read calls than 1 or 512 bytes. A production backup buffer should be chosen by testing realistic file sizes, concurrent jobs, storage devices and memory limits; a larger buffer may improve throughput but consumes more memory per worker.

## strace and mmap alternative

Run `strace -c ./file_copy` and compare its `read` row with the program's counter. The program counter measures read() calls in copy_file; strace also observes runtime/library calls, so totals may differ. `/usr/bin/time -v ./file_copy` provides elapsed time, user/system CPU time and maximum resident set size. With mmap(), the program maps file pages into virtual memory and can avoid repeated explicit read() calls and some copying. It still requires mapping/unmapping and page faults; dirty pages are written back by the kernel. Mapping an enormous file all at once can increase virtual-memory pressure, while windowed mapping bounds the working set.

## Implementation command

`gcc -std=c11 -Wall -Wextra file_copy.c -o file_copy && ./file_copy`. The repository includes `Task06/run.sh` and output.txt. `strace` was not installed in the package-preparation environment, so the strace/time measurements must be captured on the student's Ubuntu/WSL2 installation.
