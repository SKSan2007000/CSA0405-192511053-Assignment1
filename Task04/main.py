services = ["UI","Program execution","I/O","File system","Communication","Error detection","Resource allocation","Accounting/logging","Protection","Security"]
matrix = {
"Monitor":["Minimal display/alarm","Validated tasks only","Sensor I/O","Small controlled config/logs","Deterministic device links","Watchdog/sensor fault","Fixed-priority scheduling","Safety event log","Process/device isolation","Secure boot/signed updates"],
"Tablet":["Touch UI","Clinical apps","Touch/radio","Encrypted app storage","Wi-Fi/API","App/radio errors","Power-aware","Device/audit logs","App sandbox","MDM/MFA/encryption"],
"Workstation":["Full GUI","Clinical apps","Keyboard/display/network","Managed files","Hospital LAN","OS/app monitoring","General scheduler","User audit","RBAC","EDR/MFA/patching"],
"Database":["Minimal admin UI","DB engine","Storage/network","Durable DB files","Cluster replication","DB/storage fault","CPU/RAM/I/O controls","Transaction audit","DB roles","Encryption/backups"]
}
print("TASK 4 – Operating-system services matrix")
print("Service | " + " | ".join(matrix))
for i,s in enumerate(services):
    print(s+" | "+" | ".join(matrix[e][i] for e in matrix))
print("\nMonitor services to minimise: desktop shell, printing, media, unrelated daemons, unnecessary network listeners.")
print("Never remove essential sensor I/O, watchdog, error detection, security, secure update or safety logging.")
print("Database essentials: program execution, file/storage I/O, communication, error detection, resource allocation, audit, protection and security.")
