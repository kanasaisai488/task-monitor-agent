
# human_feedback_prompt.py
import argparse
from agent import memory_store, feedback_collector, progress_updater, git_handler

def review_pending_tasks(project_tag=None, project_dir=".", agent_prefix="SA", push=False):
    print(f"🔍 Reviewing pending tasks for project: {project_tag or 'ALL'}")

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
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-tag", help="Filter review by project tag (optional)")
    parser.add_argument("--project-dir", default=".", help="Path to Git project root")
    parser.add_argument("--agent-prefix", default="SA", help="Prefix in Git commit message (e.g., SA, EM, LP)")
    parser.add_argument("--push", action="store_true", help="Auto push commit to remote if set")
    args = parser.parse_args()

    review_pending_tasks(args.project_tag, args.project_dir, args.agent_prefix, args.push)
