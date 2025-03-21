
# cli_tools/batch_prompt_regenerator.py
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import argparse
from agent import memory_store, prompt_generator

def regenerate_prompts(project_tag=None, status_filter="needs_review", overwrite=False):
    records = memory_store.fetch_all_records(project_tag)
    selected_records = [r for r in records if r[7] == status_filter]

    if not selected_records:
        print(f"✅ No tasks with status '{status_filter}' found.")
        return

    for record in selected_records:
        task_id = record[0]
        task_desc = record[3]
        file_path = record[4]
        diff_text = record[5]

        diff_lines = diff_text.splitlines() if diff_text else []

        print(f"🔁 Regenerating prompt for Task ID: {task_id} — {task_desc[:40]}")

        prompt_path, new_prompt_block = prompt_generator.generate_prompt_block(
            task_desc, file_path, diff_lines, project_tag
        )

        if overwrite:
            memory_store.update_prompt_block(task_id, new_prompt_block)
            print(f"✅ Prompt block regenerated and updated in DB.")
        else:
            print(f"📝 Prompt block regenerated (not updated in DB). Saved to: {prompt_path}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-tag", help="Filter by project tag (optional)")
    parser.add_argument("--status", default="needs_review", help="Filter tasks by status (default: needs_review)")
    parser.add_argument("--overwrite", action="store_true", help="Update DB with new prompt block")
    args = parser.parse_args()

    regenerate_prompts(args.project_tag, args.status, args.overwrite)

if __name__ == "__main__":
    main()
