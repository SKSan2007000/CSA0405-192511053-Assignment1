# Task 7 – Evaluate Process Control System Calls
## Run the required TODO completion
```bash
gcc -std=c11 -Wall -Wextra process_control.c -o process_control
./process_control
```
Expected output:
```text
shell: running job 1
42
job 1 exit status 0
shell: running job 2
job 2 exit status 3
```
## Concepts
`fork()` creates a child; `exec()` replaces the child program image; `waitpid()` collects child status; `exit()` terminates and makes status available. The shell forks, child execs, parent waits and reports status. Zombie: exited child not yet waited for. Orphan: child whose parent exits; adopted by system reaper. fork()+exec() separates process creation from program selection and allows setup between them.
## Why fflush?
When stdout is redirected, stdio is usually fully buffered. If a line remains in the buffer at fork(), parent and child inherit copies. If both later call `exit()` and flush, the line is written twice. `fflush(stdout)` before fork avoids this. `_exit()` does not flush stdio; `exit()` does.
## Alternative
`posix_spawn()` combines spawn actions and program execution and can be more efficient in some contexts. Threads share address space and are cheaper but have less isolation. For N commands, basic process/thread creation work is O(N); process memory uses separate virtual address spaces (often copy-on-write after fork), while threads share code/data/heap but each needs stack and thread metadata.
