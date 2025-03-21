
# cli_tools/task_dashboard_cli.py
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import argparse
from tabulate import tabulate
from agent import memory_store

def display_tasks(records, filter_status=None):
    headers = ["ID", "Timestamp", "Project", "Description", "File", "Status"]
    table = []

    for record in records:
        task_id = record[0]
        timestamp = record[1]
        project = record[2]
        description = record[3]
        file_path = record[4]
        status = record[7]

        if filter_status and status != filter_status:
            continue

        table.append([task_id, timestamp, project, description[:50], file_path.split("/")[-1], status])

    print(tabulate(table, headers=headers, tablefmt="fancy_grid"))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-tag", help="Filter by project tag (optional)")
    parser.add_argument("--status", help="Filter by task status (optional: pending, success, failed, needs_review)")
    args = parser.parse_args()

    records = memory_store.fetch_all_records(args.project_tag)
    display_tasks(records, filter_status=args.status)

if __name__ == "__main__":
    main()
