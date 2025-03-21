
# main_project_runner.py
import argparse
import os
from agent.watcher import FileWatcher
from agent import diff_tracker, prompt_generator, memory_store

def handle_file_event(event_type, file_path, project_tag):
    print(f"[EVENT] {event_type.upper()} → {file_path}")
    diff = diff_tracker.compare_files(file_path, file_path)
    diff_tracker.save_diff_report(diff, "reports/latest_diff.txt", project_tag)

    task_description = f"Detected {event_type} on {file_path}"
    prompt_path, prompt_block = prompt_generator.generate_prompt_block(task_description, file_path, diff, project_tag)
    memory_store.store_task_record(project_tag, task_description, file_path, "\n".join(diff), prompt_block)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-dir", required=True, help="Absolute path to the project root directory")
    parser.add_argument("--project-tag", required=True, help="Unique tag for this project (e.g., 'quant_research')")
    args = parser.parse_args()

    base_dir = os.path.abspath(args.project_dir)
    project_tag = args.project_tag

    # Initialize memory DB with project tag support
    memory_store.init_memory_db()

    watch_paths = [
        os.path.join(base_dir, "agents"),
        os.path.join(base_dir, "core"),
        os.path.join(base_dir, "templates"),
        os.path.join(base_dir, "config"),
    ]

    print(f"[✔] Monitoring Project: {base_dir} (Tag: {project_tag})")

    def wrapped_callback(event_type, file_path):
        handle_file_event(event_type, file_path, project_tag)

    watcher = FileWatcher(watch_paths, wrapped_callback)
    watcher.start()
