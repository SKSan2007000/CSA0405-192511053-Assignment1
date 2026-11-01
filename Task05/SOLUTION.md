# TASK 5 – Examine System Calls

## Categories and read() path

System calls are commonly grouped into process control (fork, exec, wait, exit), file management (open, read, write, close), device management (ioctl), information maintenance (getpid, clock_gettime), communication (pipe, socket, send, recv) and protection (chmod, chown, access). A call such as read() begins in the application through a C library wrapper. The wrapper places the syscall number and arguments according to the platform ABI and executes the syscall/trap instruction. The CPU switches to kernel mode; the kernel validates the file descriptor and user buffer, performs the file/device operation, and returns a byte count or error. The CPU returns to user mode and the wrapper exposes the result to the application.

## Parameter passing and strace

On Linux x86-64, system-call arguments are normally passed in architecture-defined registers. Some interfaces use pointers to parameter structures in memory. Stack passing is common in some function calling conventions, but is not the usual Linux x86-64 syscall argument mechanism. `strace` observes system calls and signals, showing names, arguments, return values and errors. `strace -c` summarises counts and time spent in traced calls.

## Alternative: stdio functions

`fopen`, `fread` and `fwrite` provide buffered C library I/O. For a file of n bytes and a user-space buffer of b bytes, data-transfer system calls are approximately O(n/b), rather than O(n) for one-byte direct calls. A 4096-byte buffer for n bytes gives roughly ceil(n/4096) data reads plus an EOF read, subject to library/runtime behaviour. The library buffer consumes O(b) additional user-space memory. Buffering reduces mode transitions but may add copying and requires correct flush/error handling.

## Implementation and run

The repository contains `Task05/syscall_demo.c`, which uses write() to print a message, read() to receive input, and write() again to echo the bytes. Compile with `gcc -std=c11 -Wall -Wextra syscall_demo.c -o syscall_demo`; run `printf 'abnormal reading\n' | ./syscall_demo`; inspect with `strace -o strace.txt ./syscall_demo` and `strace -c ./syscall_demo`.
