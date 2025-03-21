# Module: diff_tracker.py
import difflib
import os

def load_file_content(file_path):
    if not os.path.exists(file_path):
        return []
    with open(file_path, "r", encoding="utf-8") as f:
        return f.readlines()

def compare_files(old_path, new_path):
    old_content = load_file_content(old_path)
    new_content = load_file_content(new_path)

    diff = difflib.unified_diff(
        old_content,
        new_content,
        fromfile='OLD: ' + old_path,
        tofile='NEW: ' + new_path,
        lineterm=''
    )
    return list(diff)

def save_diff_report(diff_lines, output_path, project_tag="default"):
    full_dir = os.path.join(os.path.dirname(output_path), project_tag)
    os.makedirs(full_dir, exist_ok=True)
    full_path = os.path.join(full_dir, os.path.basename(output_path))

    with open(full_path, "w", encoding="utf-8") as f:
        f.write("\n".join(diff_lines))

    return full_path
