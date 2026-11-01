# Simple deterministic comparison of polling and interrupt detection.
deadline_ms = 10.0
poll_intervals_ms = [1, 5, 10, 20]
interrupt_latency_ms = 0.25  # illustrative assumption, not measured hardware data
print("TASK 8 – Detection latency model (illustrative assumptions)")
print(f"Required alarm deadline: {deadline_ms:.2f} ms")
print(f"Assumed interrupt latency: {interrupt_latency_ms:.2f} ms")
for p in poll_intervals_ms:
    worst=p
    status="within 10 ms only if other processing/scheduling delay leaves margin" if worst < deadline_ms else "does not meet 10 ms worst-case before other delays"
    print(f"Polling interval {p:>2} ms: worst detection wait up to {worst:.2f} ms; {status}")
print("Interrupt-driven: approximate detection latency is interrupt latency plus handler, scheduling and processing time.")
print("Conclusion: interrupts avoid repeated polling and can reduce power, but the complete end-to-end path must be bounded and validated.")
