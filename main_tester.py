
# main_tester.py – Full flow tester with Git commit and optional push
import os
from agent import diff_tracker, prompt_generator, memory_store, feedback_collector, progress_updater, git_handler

project_tag = "project_test"
project_dir = "."  # Git root
agent_prefix = "SA"
memory_store.init_memory_db()

test_file_path = os.path.abspath("core/test_sample.py")
with open(test_file_path, "w", encoding="utf-8") as f:
    f.write("# Initial content\n")

with open(test_file_path, "w", encoding="utf-8") as f:
    f.write("# Initial content\n# New line added\n")

diff = diff_tracker.compare_files(test_file_path, test_file_path)
diff_output_path = diff_tracker.save_diff_report(diff, "reports/test_diff_output.txt", project_tag)

task_description = "Full test with Git commit + optional push"
prompt_path, prompt_block = prompt_generator.generate_prompt_block(task_description, test_file_path, diff, project_tag)

memory_store.store_task_record(project_tag, task_description, test_file_path, "\n".join(diff), prompt_block, status="pending")

print("\n🗂 DB Records Before Feedback:")
records = memory_store.fetch_all_records(project_tag)
for row in records:
    print(row)

last_task_id = records[-1][0] if records else None
if last_task_id:
    feedback = feedback_collector.collect_feedback(task_description)
    memory_store.update_task_status(last_task_id, feedback["status"])

    progress_updater.update_progress_log(last_task_id, task_description, test_file_path, feedback["status"])
    progress_updater.update_task_state_json(last_task_id, task_description, test_file_path, feedback["status"])

    if feedback["status"] == "success":
        git_handler.auto_commit(test_file_path, task_description, agent_prefix, project_dir, push=True)

    print(f"✅ Task ID {last_task_id} updated with status: {feedback['status']} and progress log updated.")

print("\n✅ DB Records After Feedback:")
records = memory_store.fetch_all_records(project_tag)
for row in records:
    print(row)
