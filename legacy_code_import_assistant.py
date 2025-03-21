
# legacy_code_import_assistant.py (Interactive Version)
import os
from datetime import datetime

EXCLUDE_DIRS = {'.git', '__pycache__', 'venv', '.venv', 'myenv', '.idea', '.vscode'}
EXCLUDE_FILES = {'desktop.ini'}

def scan_legacy_codebase(project_dir):
    tasks = []
    for root, dirs, files in os.walk(project_dir):
        rel_path = os.path.relpath(root, project_dir)
        if any(part in EXCLUDE_DIRS for part in rel_path.split(os.sep)):
            continue
        for f in files:
            if f in EXCLUDE_FILES or not f.endswith(('.py', '.cs', '.cpp', '.js')):
                continue
            full_path = os.path.join(root, f)
            task = {
                'file_path': full_path,
                'relative_path': os.path.relpath(full_path, project_dir),
                'module': os.path.splitext(f)[0]
            }
            tasks.append(task)
    return tasks

def generate_task_declarations(tasks, start_id=100):
    lines = []
    for i, task in enumerate(tasks, start=start_id):
        lines.append(f"TASK #{i}: Refactor Legacy Module – {task['module']}")
        lines.append(f"- Review and modularize: `{task['relative_path']}`")
        lines.append(f"- Ensure style and naming convention alignment")
        lines.append("")
    return "\n".join(lines)

def run_assistant(project_dir, output_file="progress_log.md", start_id=100):
    tasks = scan_legacy_codebase(project_dir)
    task_text = generate_task_declarations(tasks, start_id=start_id)
    output_path = os.path.join(project_dir, output_file)
    with open(output_path, "a", encoding="utf-8") as f:
        f.write(f"\n# Auto-Generated Task Declarations ({datetime.now().strftime('%Y-%m-%d %H:%M:%S')})\n")
        f.write(task_text)
    print(f"✅ Legacy tasks appended to {output_file}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="🧠 Legacy Code Import Assistant – TaskMonitorAgent")
    parser.add_argument("--project-dir", help="Target project directory path")
    parser.add_argument("--start-id", type=int, default=100, help="Starting task ID number")
    args = parser.parse_args()

    if not args.project_dir:
        args.project_dir = input("📂 Enter path to legacy project folder: ").strip()
    run_assistant(args.project_dir, start_id=args.start_id)
