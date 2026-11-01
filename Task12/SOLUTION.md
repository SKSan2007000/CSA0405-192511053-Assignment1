# TASK 12 – Day-4 Design Challenge: Remote Monitoring and Cloud Records

## A. Impact analysis

Home monitoring adds untrusted networks, remote device identity, variable latency, intermittent connectivity and a larger attack surface. The device OS must support secure boot, signed firmware, authenticated updates, encrypted local storage, certificate lifecycle and safe offline operation. Cloud records affect the database's deployment model, identity, access control, data residency, audit, backup, disaster recovery and distributed-system consistency. A bedside/home alarm must not rely on a round trip to a cloud service.

## B. Evaluation of original design

The original local real-time monitor design remains suitable for immediate alarm decisions because it can operate without internet access. It is not sufficient by itself for home telemetry and shared cloud records: secure device onboarding, remote update, store-and-forward, identity federation, API security and cloud resilience must be added. Cloud records can improve cross-hospital access and scale, but introduce provider dependency, network outage, privacy and configuration risks.

## C. Adaptation or redesign

Decision: MODIFY the original design, rather than discard its real-time foundation. Retain a local embedded hard real-time OS and local alarm path on bedside and home devices. Add a secure gateway or device agent that timestamps readings, authenticates to the service, encrypts data in transit and queues telemetry during outages. Use a message broker/API gateway with schema validation, rate limiting, device identity, retry-safe delivery and audit. Move shared records to a distributed cloud records service with tenant isolation, RBAC, encryption at rest/in transit, multi-zone availability, independent backups and tested restore. Hospitals retain local caching and a safe degraded mode when cloud connectivity is lost.

## D. Evidence-based defence

The decision retains the original strongest safety property: a local alarm does not wait for internet or cloud processing. It modifies connectivity and record services to support remote devices and cross-hospital access. The trade-off is greater security, integration and operational complexity, but it avoids making patient alarms dependent on WAN latency. The design must be validated through latency tests, offline/reconnect tests, penetration testing, fail-over drills, backup restoration and audit review.

## Complexity

For D devices producing r readings per second, ingestion volume is O(D×r) readings per second. Queue storage for an offline interval t is O(D×r×t×s), where s is average bytes per reading including metadata. Capacity planning must include bursts, retries, retention and encryption overhead.
