
# Module: progress_updater.py

import os
from datetime import datetime

PROGRESS_LOG_PATH = os.path.join(os.path.dirname(__file__), "../progress_log.md")
TASK_STATE_PATH = os.path.join(os.path.dirname(__file__), "../storage/task_state.json")

def update_progress_log(task_id, task_description, file_path, status):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"- [{status.upper()}] Task ID: {task_id} | {task_description} | {file_path} | {timestamp}\n"

    os.makedirs(os.path.dirname(PROGRESS_LOG_PATH), exist_ok=True)
    with open(PROGRESS_LOG_PATH, "a", encoding="utf-8") as f:
        f.write(entry)

def update_task_state_json(task_id, task_description, file_path, status):
    import json

    os.makedirs(os.path.dirname(TASK_STATE_PATH), exist_ok=True)

    if os.path.exists(TASK_STATE_PATH):
        with open(TASK_STATE_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = {"tasks": []}

    data["tasks"].append({
        "task_id": task_id,
        "description": task_description,
        "file": file_path,
        "status": status,
        "timestamp": datetime.now().isoformat()
    })

    with open(TASK_STATE_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
