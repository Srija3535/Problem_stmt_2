import subprocess
import datetime
import os

def run_backup():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Starting backup at {timestamp}...")
    cmd = [
        "rsync", "-avz", "--delete",
        f"{SOURCE_FOLDER}/",              # Source (trailing / = copy contents)
        f"{REMOTE_USER}@{REMOTE_HOST}:{REMOTE_FOLDER}"
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)

    with open(REPORT_FILE, "a") as f:
        f.write(f"\n--- Backup at {timestamp} ---\n")
        if result.returncode == 0:
            msg = "SUCCESS: Backup completed!\n"
            print("SUCCESS!")
        else:
            msg = f"FAILED: {result.stderr}\n"
            print("FAILED! See report.")

        f.write(msg)
        f.write(result.stdout + "\n")

    print(f"Check '{REPORT_FILE}' for details.\n")


if __name__ == "__main__":
    run_backup()