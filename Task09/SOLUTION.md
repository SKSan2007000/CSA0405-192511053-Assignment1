# TASK 9 – Evaluate the Memory Hierarchy and I/O Systems

## Memory hierarchy and data placement

Registers are the smallest and fastest CPU storage; caches are small, fast memory near the CPU; RAM holds active programs and working data; SSD/NVMe provides persistent low-latency storage; HDD and archival/object storage provide larger, slower and often cheaper capacity; network storage adds communication latency and availability dependencies. Exact access times and capacities depend on hardware and must be measured on the target system.

MRI images should be acquired into RAM/DMA buffers, processed using RAM and fast local NVMe scratch space, then stored in protected image storage and backed up to an archive. Patient records belong in a transactional database on redundant durable storage, with encrypted backups. Monitor readings should be buffered locally at the device/gateway so the alarm path remains independent of WAN/cloud availability, then forwarded to central time-series or clinical records storage.

## I/O methods and caching

Programmed I/O makes the CPU repeatedly poll device status and move data; it is simple but consumes CPU. Interrupt-driven I/O lets the device notify the CPU when service is needed, avoiding continuous polling but may create many interrupts for high-volume transfers. DMA transfers blocks between device and memory with limited CPU involvement and is suitable for high-throughput MRI data. The system needs safe DMA buffers, appropriate cache-coherency handling and IOMMU protection where available. Database caches keep frequently accessed records or index pages in RAM, reducing storage access latency, but cache invalidation, consistency and memory pressure must be managed.

## Alternative: one interrupt per word for 500 MB

Assuming decimal 500 MB = 500,000,000 bytes and a 4-byte word, one interrupt per word produces 125,000,000 interrupts. This is an enormous interrupt load and wastes CPU time on interrupt entry/exit and handler processing. DMA transfers blocks and normally needs far fewer completion interrupts, reducing CPU overhead. Interrupt-per-word I/O needs little or no large DMA buffer but imposes huge CPU service cost; DMA needs descriptors and bounded buffers but is far more efficient for bulk image transfer.

## Complexity

Transferring n bytes is O(n) data movement. With a transfer unit of w bytes, one interrupt per word requires O(n/w) interrupts. DMA reduces interrupts to roughly O(n/B) block completions for block size B, depending on device and descriptor strategy.
