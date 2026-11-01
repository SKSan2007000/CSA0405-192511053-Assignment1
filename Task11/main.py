plan = [
("Bedside monitors","Dedicated hard RT embedded OS","Interrupt-driven sensors; watchdog; secure boot; local alarm fallback"),
("Nurses' tablets","Managed mobile OS","MDM, MFA, encryption, app sandbox, power-aware wireless"),
("Doctors' workstations","Managed desktop OS","RBAC, endpoint protection, patching, audit"),
("Patient database","Clustered server OS","Replication, quorum/fencing, redundant storage/network, tested backups"),
("MRI imaging","SMP multiprocessor server OS","Parallel compute, DMA-capable I/O, NVMe scratch storage"),
("Partner hospitals","Distributed secure services","Mutual TLS, API authorisation, audit, retry-safe synchronisation")
]
for row in plan: print(" | ".join(row))
print("\nRisks: platform diversity, patch coordination, fail-over bugs, network outage, vendor support.")
print("Mitigations: standard builds, central monitoring, change control, vulnerability management, DR and fail-over drills.")
print("\nVM alternative: virtualise suitable server workloads, but keep hard real-time bedside alarm path on dedicated validated hardware unless end-to-end RT guarantees are proven.")
