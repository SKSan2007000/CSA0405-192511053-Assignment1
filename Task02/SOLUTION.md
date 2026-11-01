# TASK 2 – Type of Operating System for Each Environment

## Selection and rejected alternatives

Bedside monitors should use a dedicated hard real-time embedded OS because a missed alarm deadline can create direct patient risk. A soft real-time system is insufficient if late alarms are unacceptable. Nurses’ tablets should use a handheld/mobile OS with power management, wireless roaming, application sandboxing and managed deployment. Doctors’ workstations should use a desktop OS with enterprise security and support tools.

The patient database should run on a clustered server OS with fail-over across independent nodes. A mainframe can provide centralised high-volume transaction processing, but it is not automatically a substitute for geographically or physically redundant fail-over. MRI reconstruction suits a multiprocessor server OS. The partner-hospital connection is part of a distributed system: each hospital retains local services while securely exchanging agreed records and updates.

## SMP versus AMP and database cluster

Symmetric multiprocessing (SMP) gives multiple processors equal access to shared memory and one OS instance; the scheduler distributes parallel imaging work. It is generally simpler for a multi-threaded reconstruction workload. Asymmetric multiprocessing (AMP) assigns processors different roles or runs separate control domains; it can provide isolation or specialised control but requires explicit coordination and can leave resources unevenly used.

A database cluster uses redundant nodes, replicated data and health monitoring. Fail-over should occur within a defined recovery objective, potentially seconds if the application and storage architecture support it. Quorum and fencing prevent two nodes from simultaneously acting as the active writer. Replication alone is not a backup: logical corruption can replicate, so independent backups and restore tests remain necessary.

## Alternative: one large multiprocessor database host

A single large machine may offer high throughput and simpler administration, but it remains a single point of failure for motherboard, power, OS, storage controller or maintenance outage. A cluster costs more and adds replication, quorum and operational complexity, but allows service to continue after a node failure. With p processors, ideal parallel throughput may approach O(p) scaling for perfectly parallel work, but real workloads are limited by serial sections, lock contention, memory bandwidth and I/O. Memory capacity is bounded by the host's installed RAM; adding processors does not automatically add enough memory or eliminate the single-host failure risk.

## Complexity

A conceptual throughput model is T(p)=T1/[s+(1−s)/p], where s is the serial fraction (Amdahl’s law). Memory capacity is O(M) for M bytes installed. Cluster availability depends on node, network, storage and fail-over design; it cannot be inferred from node count alone.
