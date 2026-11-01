# TASK 3 – Operating-System Structures

## Structure comparison

A monolithic kernel places many OS services in kernel space. It can provide low service-call overhead, but a faulty kernel driver can compromise the whole kernel. A layered design separates responsibilities behind defined interfaces and is easier to reason about, although strict layer crossings can add overhead. A microkernel keeps a small set of mechanisms in kernel mode and moves services/drivers to isolated user-space servers; this improves fault containment but requires inter-process communication and context switches.

A modular kernel supports loadable modules, making features and drivers easier to add or update, but a faulty module loaded into kernel space can still crash or corrupt the kernel. A hybrid structure combines ideas to balance performance, compatibility and modularity, but typically retains a larger trusted kernel than a minimal microkernel.

## Hospital choices and OS examples

For bedside monitors, select a small, certified real-time OS with a minimal, controlled kernel and carefully isolated components. A microkernel-style architecture is attractive for driver/server fault isolation, provided IPC overhead is measured and the complete alarm path still meets the 10 ms deadline. For the database, a supported modular Linux server kernel or enterprise hybrid OS is appropriate because mature storage, networking, multiprocessor and clustering support matter.

Linux is commonly described as a modular monolithic kernel. Windows NT is commonly described as hybrid. Android uses the Linux kernel with Android-specific user-space layers and services. QNX is a microkernel real-time OS. FreeRTOS is a small real-time kernel rather than a general desktop OS.

## Alternative: monolithic monitor kernel

A direct system call in a monolithic kernel generally crosses into kernel mode and returns, while a microkernel service may require message passing to a user-space server and back. The microkernel path can involve additional IPC/context-switch cost, but its driver fault isolation may reduce the impact of a failure. A monolithic kernel can use fewer separate service processes and less IPC memory, but it includes more code in the privileged fault domain. A defective monolithic driver can crash the entire monitor; an isolated user-space driver may be restarted, subject to validated safety behaviour.

## Complexity

If a service request requires k IPC exchanges, the communication overhead grows with O(k) messages; a direct system call has a bounded transition cost but the actual time is hardware/kernel dependent. Kernel memory is O(K) for kernel image and resident structures. A structure must be chosen using measured worst-case latency and fault-injection evidence, not a generic claim that one kernel type is always faster.
