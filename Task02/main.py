choices = [
("Bedside monitors","Hard real-time embedded OS","General desktop OS: no inherent hard deadline guarantee"),
("Nurses' tablets","Handheld/mobile OS","Desktop OS: greater resource and battery demand"),
("Doctors' workstations","Desktop OS","Hard RTOS: not needed for interactive office applications"),
("Patient database","Clustered server OS with fail-over","Single server: single point of failure"),
("MRI imaging server","Multiprocessor OS using SMP","Single processor: less parallel capacity"),
("Partner hospitals","Distributed system","Local-only system: cannot coordinate shared records")
]
print("TASK 2 – OS type selection")
for env,choice,reject in choices: print(f"{env}: {choice}\n  Rejected alternative: {reject}")
print("\nSMP vs AMP")
print("SMP: processors share one OS image and memory; simpler parallel workload scheduling.")
print("AMP: processors may have assigned roles/OS instances; useful for isolation but adds coordination.")
print("\nDatabase alternative")
print("Single multiprocessor host: potentially strong throughput, but host/power/storage failure stops service.")
print("Cluster: extra cost and operational complexity, but redundant nodes and fail-over improve availability.")
