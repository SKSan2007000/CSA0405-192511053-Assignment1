image_mb = 500
word_bytes = 4
bytes_total = image_mb * 1_000_000
interrupts = bytes_total // word_bytes
print("TASK 9 – I/O and DMA calculation")
print("Memory hierarchy: registers -> cache -> RAM -> SSD/NVMe -> HDD/archive -> network/object storage.")
print("MRI: RAM working buffers, fast local NVMe for recent scans, protected archive for retention.")
print("Patient records: replicated durable SSD/NVMe database with encrypted backups.")
print("Monitor readings: local real-time buffer/gateway then central time-series storage; alarm must stay local.")
print(f"\nFor {image_mb} MB (decimal) transferred one 4-byte word per interrupt:")
print(f"Total bytes = {bytes_total:,}")
print(f"Interrupts = {bytes_total:,} / {word_bytes} = {interrupts:,}")
print("DMA transfers blocks using descriptors and typically requires far fewer completion interrupts.")
print("DMA requires safe buffer management, IOMMU protection where available and cache-coherency handling.")
