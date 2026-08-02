import os
import datetime

# File to update
log_file = "daily_activity.txt"

# Get current time
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Append timestamp to file
with open(log_file, "a") as f:
    f.write(f"Commit log entry at: {now}\n")

# Run git commands
os.system("git add .")
os.system(f'git commit -m "Auto commit: {now}"')
os.system("git push")

print("Successfully committed and pushed to GitHub!")