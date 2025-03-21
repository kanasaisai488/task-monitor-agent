
# cli_tools/task_summary_exporter.py
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import argparse
import csv
import json
import os
from agent import memory_store

def export_csv(records, output_path):
    headers = ["ID", "Timestamp", "Project", "Description", "File", "Prompt Block", "Diff Text", "Status"]
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(records)
    print(f"✅ CSV Exported: {output_path}")

def export_json(records, output_path):
    keys = ["id", "timestamp", "project", "description", "file", "prompt_block", "diff_text", "status"]
    data = [dict(zip(keys, row)) for row in records]
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"✅ JSON Exported: {output_path}")

def export_markdown(records, output_path):
    lines = ["| ID | Timestamp | Project | Description | File | Status |", "|----|-----------|---------|-------------|------|--------|"]
    for row in records:
        lines.append(f"| {row[0]} | {row[1]} | {row[2]} | {row[3][:30]} | {os.path.basename(row[4])} | {row[7]} |")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"✅ Markdown Exported: {output_path}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-tag", help="Filter by project tag (optional)")
    parser.add_argument("--status", help="Filter by status (optional)")
    parser.add_argument("--output-dir", default="exports", help="Directory to save exports")
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)

    records = memory_store.fetch_all_records(args.project_tag)
    if args.status:
        records = [r for r in records if r[7] == args.status]

    export_csv(records, os.path.join(args.output_dir, "task_summary.csv"))
    export_json(records, os.path.join(args.output_dir, "task_summary.json"))
    export_markdown(records, os.path.join(args.output_dir, "task_summary.md"))

if __name__ == "__main__":
    main()
