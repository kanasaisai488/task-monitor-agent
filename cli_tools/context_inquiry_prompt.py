import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import argparse
from agent import prompt_generator

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-tag", required=True, help="Project tag or name")
    parser.add_argument("--task", required=True, help="Describe the task or objective")
    parser.add_argument("--project-dir", default=os.getcwd(), help="Root directory of the project")
    parser.add_argument("--output", help="Optional file to write the generated inquiry prompt")
    args = parser.parse_args()

    prompt = prompt_generator.generate_context_inquiry_prompt(
        args.project_tag,
        args.task,
        args.project_dir
    )

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(prompt)
        print(f"✅ Context inquiry prompt saved to: {args.output}")
    else:
        print("\n" + prompt)

if __name__ == "__main__":
    main()
 