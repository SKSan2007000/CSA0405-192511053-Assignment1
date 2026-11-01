# TASK 11 – Recommend and Defend the Operating-System Plan

## Complete recommended plan

Bedside monitors: dedicated hard real-time embedded OS, minimal validated services, interrupt-driven sensor I/O, watchdog, secure boot and local alarms. Nurses’ tablets: managed mobile OS with MDM, MFA, encryption, app sandbox, offline queue and power-aware wireless. Doctors’ workstations: enterprise desktop OS with RBAC, endpoint protection, patching and audit. Patient database: clustered server OS with redundant nodes, replication, quorum/fencing, encrypted durable storage, tested backups and disaster recovery. MRI imaging server: SMP multiprocessor OS with parallel reconstruction, DMA-capable I/O and fast local NVMe. Partner hospitals: secure distributed APIs with mutual TLS, identity authorisation, audit, retry-safe synchronisation and agreed data formats.

## Limitations and risks

The design has platform diversity, which increases patch coordination, staff training and support effort. Cluster fail-over can fail because of split-brain, replication lag or shared dependencies. Wireless and partner links can be unavailable. A compromised endpoint can still misuse valid credentials. Mitigations include standardised build baselines, central identity and monitoring, staged patching, least privilege, security testing, network segmentation, tested backups and regular fail-over/disaster-recovery exercises. The plan scales to three hospitals through distributed record exchange and local operation during WAN failure, subject to interoperability, governance and network capacity.

## Alternative: virtual machines on two large servers

Virtualisation can consolidate database, application and integration services, but adds hypervisor scheduling, virtual I/O and resource contention overhead. Two large servers can still share risks such as common power, network, storage or site failure. A monitor's hard real-time alarm path should not depend on a general-purpose VM or cloud network unless end-to-end latency, interrupt delivery, isolation and fail-over are formally proven and validated. Keep safety-critical monitor control on dedicated hardware; virtualise suitable non-real-time server workloads with reservations, redundancy and tested recovery.

## Evidence-based defence

The completed Task 6 program demonstrates how increasing buffer size reduces read() calls from 10,001 to 4 for a 10,000-byte file. Task 7 verifies process creation, exec and exit-status collection. Task 10 provides a repeatable process/thread benchmark, but local measurements must be substituted before final submission. These results support the principle of reducing avoidable kernel transitions and isolating safety-critical workloads, while final latency and availability claims require target-hardware tests.
