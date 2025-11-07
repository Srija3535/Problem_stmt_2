import psutil
import time

CPU_THRESHOLD = 80  
MEMORY_THRESHOLD = 80 
DISK_THRESHOLD = 90  

def check_system_health():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    print(f"CPU Usage: {cpu}%")
    print(f"Memory Usage: {memory}%")
    print(f"Disk Usage: {disk}%")

    alerts = []
    if cpu > CPU_THRESHOLD:
        alerts.append(f"⚠️ High CPU usage: {cpu}%")
    if memory > MEMORY_THRESHOLD:
        alerts.append(f"⚠️ High Memory usage: {memory}%")
    if disk > DISK_THRESHOLD:
        alerts.append(f"⚠️ Low Disk Space: {disk}%")

    if alerts:
        print("\nALERTS:")
        for alert in alerts:
            print(alert)
        with open("system_health.log", "a", encoding="utf-8") as log_file:
            log_file.write("\n".join(alerts) + "\n")
    else:
        print("✅ System health is good.\n")

while True:
    check_system_health()
    time.sleep(5)
