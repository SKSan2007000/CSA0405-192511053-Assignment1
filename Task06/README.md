# Task 6 – Evaluate the Cost of System Calls
## Run
```bash
gcc -std=c11 -Wall -Wextra file_copy.c -o file_copy
./file_copy
strace -c ./file_copy
/usr/bin/time -v ./file_copy
```
## Expected program output
```text
buffer    1 bytes: 10001 read() calls
buffer  512 bytes:    21 read() calls
buffer 4096 bytes:     4 read() calls
```
For a 10,000-byte file, calls are `ceil(n/b)+1` because the final read returns EOF. The code validates buffer size, handles EINTR and partial writes, and counts completed read attempts.
## Complexity
Copy time/data movement O(n); read-call count O(n/b); buffer space O(b). Larger buffers reduce kernel crossings but consume more memory. Select the production backup buffer by benchmarking realistic file sizes and concurrency, not this tiny test alone.
## Alternative: mmap()
`mmap()` maps file pages into virtual memory and can reduce explicit read/write calls and copying. It still incurs page faults, mapping calls and dirty-page writeback. A whole huge file mapping can increase virtual-memory pressure; windowed mapping bounds the working set. Compare with measurements before choosing.
## strace interpretation
The program's counter counts read() calls made by `copy_file`. `strace -c` includes all read() calls in the process, including runtime/library calls, so its total may differ slightly.
