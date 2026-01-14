log_data = [
    "INFO User admin logged in",
    "WARNING Failed login attempt from IP 192.168.1.10",
    "WARNING Failed login attempt from IP 192.168.1.10",
    "WARNING Failed login attempt from IP 192.168.1.10",
    "INFO User guest logged out",
    "ERROR Unauthorized access attempt detected",
]

failed_logins = 0
suspicious_events = []

for entry in log_data:
    if "Failed login" in entry:
        failed_logins += 1
    if "ERROR" in entry or "Unauthorized" in entry:
        suspicious_events.append(entry)

print("=== Incident Log Analysis Summary ===")
print(f"Total failed login attempts: {failed_logins}")

print("\nSuspicious Events:")
for event in suspicious_events:
    print("-", event)

if failed_logins >= 3:
    print("\n⚠️ Alert: Possible brute-force attack detected")
