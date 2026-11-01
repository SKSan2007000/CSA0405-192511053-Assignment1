requirements = {
    "Bedside monitors": [("Deterministic response", "Hard 10 ms alarm deadline"), ("Reliability", "Fault detection and safe fallback"), ("Security", "Secure boot and authenticated updates"), ("Resource footprint", "Small memory and CPU footprint"), ("Connectivity", "Local alarm must not depend on WAN")],
    "Nurses' tablets": [("Security", "MFA, encryption and managed apps"), ("Battery life", "Full-shift operation"), ("Wireless reliability", "Roaming and offline queue"), ("Usability", "Touch UI and fast access"), ("Performance", "Responsive clinical apps")],
    "Doctors' workstations": [("Security", "Role-based access and endpoint protection"), ("Availability", "Access to clinical systems"), ("Responsiveness", "Interactive UI"), ("Multitasking", "EHR and imaging apps"), ("Manageability", "Central patching")],
    "Patient database": [("Availability", "Cluster fail-over and redundant paths"), ("Integrity/durability", "Transactional storage and backups"), ("Security", "Encryption, RBAC and audit"), ("Throughput", "Concurrent clinical queries"), ("Recovery", "Tested restore and disaster recovery")],
    "MRI imaging server": [("Throughput", "Parallel image reconstruction"), ("I/O bandwidth", "High-bandwidth scanner and storage"), ("Memory capacity", "Large working sets"), ("Availability", "Recoverable processing"), ("Security", "Controlled image access")],
    "Partner-hospital link": [("Confidentiality/integrity", "Authenticated encrypted exchange"), ("Availability", "Redundant connectivity"), ("Interoperability", "Agreed data formats/APIs"), ("Auditability", "Traceable access"), ("Throughput", "Efficient record synchronisation")]
}
print("TASK 1 – Ranked requirements (highest priority first)")
for env, items in requirements.items():
    print(f"\n{env}")
    for rank,(req,why) in enumerate(items,1):
        print(f" {rank}. {req}: {why}")
print("\nAlternative: one general-purpose OS everywhere")
print("- A general-purpose scheduler does not inherently guarantee the worst-case 10 ms alarm deadline.")
print("- A common desktop image increases the monitor's memory/storage footprint and background activity.")
print("- One OS may simplify patching, but device-specific tuning and exceptions remain; fit-for-purpose systems add platform diversity.")
