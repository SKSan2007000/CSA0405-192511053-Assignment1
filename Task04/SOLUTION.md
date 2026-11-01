# TASK 4 – Operating-System Services

## Service requirements

All environments need program execution, I/O, error detection, resource allocation, protection and security, but the implementation differs. Monitors need a minimal user interface, deterministic program execution, sensor I/O, a small controlled file/log store, essential communication, watchdog/error handling, fixed-priority scheduling and secure boot/update. Unnecessary desktop shell, printing, media services, app stores and unrelated network listeners should be removed to reduce attack surface and resource use.

Tablets need a touch interface, managed app execution, radio and device I/O, encrypted app storage, hospital communication, error reporting, power-aware resource allocation, audit logs, sandboxing and MDM/MFA. Workstations need a full GUI, clinical application execution, peripherals, managed file systems, hospital networking, endpoint error monitoring, user accounting, RBAC and endpoint security. The database requires storage/file services, networking, error handling, resource allocation, transaction and audit logging, access protection, encryption and backup/restore services.

## Protecting patient records

Use authenticated user identities, role-based access control and least privilege. A nurse should access records required for assigned care, not unrestricted administrative data. Database accounts should be separate from application and operating-system accounts. Process isolation and virtual memory prevent ordinary processes from reading one another’s address spaces; database authorisation protects rows/tables and actions. Encrypt data in transit and at rest, log access, rotate credentials and review privileged actions. Emergency “break-glass” access should be justified, time-limited and audited.

## Alternative: full desktop OS on tablets

A full desktop OS typically brings extra services, background processes, drivers and storage use. These increase memory/storage demand and can increase startup time. More background CPU and radio activity can reduce battery life. A mobile OS is designed around power states, app lifecycle and wireless use. The alternative can improve compatibility with desktop software, but should be accepted only if its memory, boot and full-shift battery measurements meet clinical requirements.

## Complexity

Service configuration can be modelled as a matrix of S services across E environments, requiring O(S×E) review effort. Removing nonessential services reduces attack surface, but safety-critical I/O, error detection, watchdog and security controls must remain.
