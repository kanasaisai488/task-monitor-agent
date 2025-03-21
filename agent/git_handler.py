
# Module: git_handler.py

import subprocess
import os

def run_git_command(args, cwd=None):
    try:
        result = subprocess.run(
            ["git"] + args,
            cwd=cwd,
            text=True,
            capture_output=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"❌ Git Error: {e.stderr.strip()}")
        return None

def is_git_repo(project_dir="."):
    return os.path.isdir(os.path.join(project_dir, ".git"))

def auto_commit(file_path, task_description, agent_prefix="SA", project_dir=".", push=False):
    if not is_git_repo(project_dir):
        print(f"⚠️ Skipping commit: {project_dir} is not a Git repository.")
        return

    rel_path = os.path.relpath(file_path, start=project_dir)
    commit_msg = f"[{agent_prefix}] {task_description}"

    run_git_command(["add", rel_path], cwd=project_dir)
    run_git_command(["commit", "-m", commit_msg], cwd=project_dir)
    print(f"✅ Auto committed {rel_path} with message: {commit_msg}")

    if push:
        run_git_command(["push"], cwd=project_dir)
        print("📤 Auto pushed to remote.")

def auto_tag(version_label, tag_message=None, project_dir="."):
    if not is_git_repo(project_dir):
        print(f"⚠️ Skipping tag: {project_dir} is not a Git repository.")
        return

    args = ["tag", version_label]
    if tag_message:
        args += ["-m", tag_message]
    run_git_command(args, cwd=project_dir)
    print(f"🏷️ Tag '{version_label}' created.")
