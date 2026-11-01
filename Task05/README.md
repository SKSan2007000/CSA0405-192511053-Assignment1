# Task 5 – Examine System Calls
## Run
```bash
gcc -std=c11 -Wall -Wextra syscall_demo.c -o syscall_demo
printf 'abnormal reading\n' | ./syscall_demo
strace -o strace.txt ./syscall_demo
strace -c ./syscall_demo
```
## Expected behaviour
The program writes a message using `write()`, reads standard input using `read()`, and writes the received bytes. Use `strace` to observe `read`, `write`, `exit_group` and runtime calls.
## read() path
C library wrapper → system-call number/arguments placed according to the ABI → trap/syscall instruction → CPU enters kernel mode → kernel validates descriptor and user buffer → data is obtained from device/page cache/file → result returned → CPU returns to user mode.
## Parameter passing
Linux system-call arguments are normally passed in architecture-defined registers. Some interfaces pass pointers to parameter blocks in memory; stack passing is part of some calling conventions but is not the normal Linux x86-64 syscall argument mechanism.
## Categories
Process control (fork/exec/wait/exit), file management (open/read/write/close), device management (ioctl), information maintenance (getpid/clock_gettime), communication (socket/pipe/send/recv), protection (chmod/chown/access).
## Alternative: stdio buffering
`fopen/fread/fwrite` use user-space stdio buffers. For n bytes and a buffer b, data-transfer calls are approximately O(n/b), plus EOF/setup calls. A 4096-byte stdio buffer reduces transitions compared with one-byte operations but uses O(b) extra user-space memory.
