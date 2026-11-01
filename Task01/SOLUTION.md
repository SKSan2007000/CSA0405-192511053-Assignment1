# TASK 1 – Requirements of Each Computing Environment

## Evaluation and ranking

The hospital has six distinct computing environments, so one operating-system profile cannot satisfy every requirement equally. The bedside monitor is safety-critical: deterministic response and reliability rank first, followed by sensor I/O integrity, security and a small footprint. A 10 ms alarm deadline must be guaranteed by a validated end-to-end design, not assumed from average response time.

For nurses’ tablets, security and all-shift battery life rank first, followed by wireless reliability, usability and responsive access to the electronic health record. Offline queuing is needed so temporary Wi-Fi loss does not silently discard readings or clinical notes. Doctors’ workstations prioritise confidentiality, availability and responsiveness, then multitasking and central manageability.

The patient-record database prioritises availability, integrity/durability and access control, followed by throughput and recoverability. MRI imaging prioritises processor throughput, memory capacity and high-bandwidth I/O; availability and access security remain essential. The partner-hospital link prioritises confidentiality, integrity and availability, then interoperability, auditability and throughput.

## Ranked requirements table

Monitor: (1) deterministic alarm response ≤10 ms, (2) reliability/fail-safe behaviour, (3) sensor I/O correctness, (4) security and authenticated updates, (5) low memory/power footprint. Tablets: (1) security, (2) full-shift battery, (3) reliable roaming/connectivity, (4) usability, (5) responsive application performance. Workstations: (1) security/RBAC, (2) availability, (3) interactive response, (4) multitasking, (5) central management. Database: (1) availability/fail-over, (2) transactional integrity/durability, (3) security/audit, (4) concurrent throughput, (5) backup/recovery. MRI server: (1) parallel throughput, (2) I/O bandwidth, (3) memory capacity, (4) recoverability, (5) controlled access. Partner link: (1) confidentiality/integrity, (2) availability, (3) interoperability, (4) auditability, (5) throughput.

## Conflicts, safety and OS history

Fast deterministic response can conflict with high utilisation and many competing processes; a monitor must reserve CPU time and avoid unbounded blocking. Security controls can add latency, so they must be lightweight and measured rather than removed. High throughput on the imaging server may compete with predictable latency for other workloads, which is another reason to isolate it from monitor processing. Battery saving can conflict with continuous connectivity on tablets, requiring carefully managed radio sleep and reconnection.

Patient-safety-critical functions are the monitor’s alarm path, reliable delivery of clinical observations, database integrity/availability and controlled access to correct patient records. Batch OS lessons apply to scheduled backups and large image-processing queues. Time-sharing applies to shared database and workstation access, but interactive fairness cannot replace real-time guarantees. Personal-computer OS ideas suit doctor workstations. Mobile OS power management, sandboxing and wireless roaming suit nurses’ tablets.

## Alternative: one general-purpose OS everywhere

A general-purpose OS may have an unbounded worst-case scheduling delay under ordinary configuration; its average latency is not a proof of a 10 ms deadline. A hard real-time OS with analysed worst-case execution and interrupt latency can offer a bounded response when the hardware, drivers, workload and application are validated together. One desktop OS image also consumes more RAM/storage and background CPU on small monitors than a compact embedded RTOS. A common OS can simplify some administration and staff training, but does not eliminate device-specific security, patching, testing and support. The recommended design is a managed family of fit-for-purpose platforms with common identity, monitoring and update governance.

## Complexity

For E environments and R ranked requirements, preparing and reviewing the requirement matrix is O(E×R) time and O(E×R) space if all entries are stored. The key conclusion is architectural: real-time response, mobile power efficiency, desktop usability, database availability and imaging throughput are different optimisation goals.
