
# human_feedback_prompt.py (Interactive CLI Version)
import os
import argparse
from agent import memory_store, feedback_collector, progress_updater, git_handler

try:
    import questionary
except ImportError:
    print("Please install 'questionary' for interactive CLI: pip install questionary")
    exit()

def select_project_tag():
    tag = questionary.text("🔖 Enter project tag (e.g., project_test):").ask()
    return tag.strip()

def select_agent_prefix():
    return questionary.select("🤖 Select LLM Agent prefix:", choices=["SA", "EM", "LP"]).ask()

def confirm_push():
    return questionary.confirm("📤 Push to remote after commit?").ask()

def select_git_project_dir():
    return questionary.path("📁 Select Git project directory:").ask()

def review_pending_tasks(project_tag, project_dir, agent_prefix, push=False):
    print(f"🔍 Reviewing pending tasks for project: {project_tag}")

    records = memory_store.fetch_all_records(project_tag)
    pending_records = [r for r in records if r[7] == "pending"]

    if not pending_records:
        print("✅ No pending tasks to review.")
        return

    for record in pending_records:
        task_id = record[0]
        timestamp = record[1]
        task_desc = record[3]
        file_path = record[4]

        print(f"\n📝 Task ID: {task_id}")
        print(f"📅 Timestamp: {timestamp}")
        print(f"📄 File: {file_path}")
        print(f"🧠 Description: {task_desc}")

        feedback = feedback_collector.collect_feedback(task_desc)
        memory_store.update_task_status(task_id, feedback["status"])

        progress_updater.update_progress_log(task_id, task_desc, file_path, feedback["status"])
        progress_updater.update_task_state_json(task_id, task_desc, file_path, feedback["status"])

        print(f"✅ Task ID {task_id} updated with status: {feedback['status']} and progress log updated.")

        if feedback["status"] == "success":
            git_handler.auto_commit(file_path, task_desc, agent_prefix, project_dir, push=push)

if __name__ == "__main__":
    print("🔧 Interactive Human Feedback Review Mode")

    project_tag = select_project_tag()
    project_dir = select_git_project_dir()
    agent_prefix = select_agent_prefix()
    push = confirm_push()

    review_pending_tasks(project_tag, project_dir, agent_prefix, push)
