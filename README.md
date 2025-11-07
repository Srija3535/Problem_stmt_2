# Problem_stmt_2

# For System Health Monitoring

Monitors **CPU, Memory, Disk** every 5 seconds.  
Logs alerts to `system_health.log` when thresholds are crossed.

## Requirements
- Python 3.6
- pip install psutil
## Quick Start
bash:
git clone https://github.com/yourusername/system-monitor.git
cd system-monitor
pip install -r requirements.txt
python monitor.py
## Config (system_health.py)
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 90
## Files
- monitor.py – main script  
- system_health.log – alert log (auto-created)  
- .gitignore – excludes logs & cache


# For Automated Backup 
Backs up a folder to a remote server using 'rsync'.  
Reports success or failure in backup.txt.

 ## How to Use (3 Steps)
bash
mkdir auto-backup && cd auto-backup

# 1.Create files (copy-paste each above into its file)
#    - backup.py
#    - README.md
#    - .gitignore
#    - requirements.txt

# 2. Run!
python backup.py