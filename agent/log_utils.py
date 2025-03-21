import os
from datetime import datetime

def append_progress_log(task_description, status="in_progress", related_files=None, log_path="progress_log.md"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if related_files is None:
        related_files = []

    files_str = ", ".join(related_files) if related_files else "N/A"

    log_entry = f"""### 🗂️ Task Entry – {timestamp}
- **Task Description**: {task_description}
- **Status**: {status}
- **Related Files**: {files_str}

"""

    try:
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(log_entry)
        print(f"📝 Progress log updated: {log_path}")
    except Exception as e:
        print(f"⚠️ Failed to write to progress_log.md: {e}")
