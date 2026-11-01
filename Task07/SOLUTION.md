# TASK 7 – Evaluate Process Control System Calls

## Process lifecycle and implementation

fork() creates a child process. In the child, exec()/execlp() replaces the current process image with the requested command. The parent calls wait()/waitpid() to collect the child's termination status. exit() terminates normally and flushes stdio; _exit() terminates without flushing C stdio buffers. A shell typically parses a command, forks, performs redirection/setup in the child, execs the program and waits in the parent. The parent checks WIFEXITED and WEXITSTATUS. An exited child that has not yet been waited for is a zombie; an orphan is a child whose parent exits first and is adopted by a system reaper/init process.

## Completed TODO and expected output

`Task07/process_control.c` implements the assignment TODO with fork(), execlp("expr", "expr", "6", "*", "7", NULL), waitpid() and WEXITSTATUS. The tested output is: shell: running job 1; 42; job 1 exit status 0; shell: running job 2; job 2 exit status 3. fork() and exec() are separate so the child can configure file descriptors, environment, credentials and process attributes before replacing itself with the new program.

## Why fflush and duplicate output

When stdout is redirected to a file, it is usually fully buffered. If a message is still in the stdio buffer when fork() duplicates the process, both parent and child inherit a copy. If both later call exit(), both copies may be flushed, causing the line to appear twice. Calling fflush(stdout) before fork() empties the buffer. The repository includes `duplicate_output.c` and `run_duplicate_output_experiment.sh` to demonstrate this intentionally; the main required program uses fflush before fork and _exit in the child failure path.

## Alternative and complexity

posix_spawn() can create a child and execute a new program through one API, often avoiding some of the overhead and complexity of fork() in multithreaded programs. Threads share address space and are generally cheaper to create, but have less isolation: a memory error in one thread can corrupt the process. Creating N commands costs O(N) creation operations. fork() initially uses copy-on-write rather than eagerly copying every page, but each process has its own virtual address space and kernel process metadata. Threads share code/data/heap but need individual stacks and thread metadata.
