# TASK 8 – Evaluate CPU States and Protection

## CPU modes, interrupts and protection

User mode restricts applications from executing privileged instructions or directly changing protected hardware state. Kernel mode allows the operating system to perform privileged operations. A hardware mode bit and privilege checks enforce the distinction. A system call or exception/trap transfers control to the kernel through a controlled entry point. Hardware interrupts notify the CPU of external events; a timer interrupt lets the scheduler regain control from a running process. Virtual memory and page-table permissions isolate process address spaces and prevent one ordinary process from reading another process's protected memory.

## Monitor safety

If arbitrary monitor software could disable interrupts, it could prevent the scheduler and alarm-handling path from running, potentially missing the 10 ms deadline and compromising patient safety. Only a small, validated kernel component should manage interrupt masking, and critical sections must be bounded. The real-time system must analyse interrupt latency, handler execution, scheduling and application processing as one end-to-end deadline.

## Alternative: polling instead of interrupts

With polling every P milliseconds, an event that occurs just after a poll may wait almost P milliseconds before detection, before additional processing delay. A 10 ms polling interval alone can consume the entire 10 ms alarm budget and therefore cannot guarantee the deadline. A shorter polling interval reduces worst-case detection wait but consumes CPU cycles and energy even when no event occurs. Interrupt-driven I/O can respond promptly and permit idle states, but interrupt latency and handler scheduling still need measurement and a proven bound.

## Complexity

For a polling interval P, worst-case detection wait is O(P) in elapsed time and CPU cost is proportional to polling frequency. Interrupt handling cost scales with the number of events, O(I), rather than continuously polling at a fixed rate when idle.
