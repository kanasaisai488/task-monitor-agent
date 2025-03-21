import argparse
import os
import sys
import zlib
import base64
from datetime import datetime

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from agent import code_reference_loader, prompt_generator, memory_store
from agent.log_utils import append_progress_log


def find_file_for_component(component_name, project_root):
    matches = []
    for root, dirs, files in os.walk(project_root):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()
                        if component_name in content:
                            matches.append(file_path)
                except:
                    continue
    return matches


def dispatch_context(components, project_root, include_summary=False):
    context_blocks = []

    for comp in components:
        files = find_file_for_component(comp, project_root)
        if not files:
            context_blocks.append(f"# ⚠️ Component '{comp}' not found in project files.\n")
            continue

        for path in files:
            ref = code_reference_loader.extract_code_reference(path)

            # AGENT NOTE tagging
            note = f"# AGENT_NOTE: This block was retrieved via context_dispatcher for component '{comp}'.\n# Source: {path}"
            context_blocks.append(f"\n{note}\n\n# 🔍 Context for '{comp}' in {path}:\n\n" + ref.strip() + "\n")

            # Log in memory store
            memory_store.log_dispatched_context(comp, ref.strip())

            # Log in progress log
            append_progress_log(
                task_description=f"Dispatched context for component '{comp}'",
                status="dispatched",
                related_files=[path]
            )

    if include_summary:
        summary = prompt_generator.generate_directory_summary(project_root)
        context_blocks.append("\n# 📂 Project Directory Summary:\n" + summary + "\n")

    return "\n".join(context_blocks)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--request", required=True, help="Comma-separated list of components/classes to fetch context for")
    parser.add_argument("--project-root", default=os.getcwd(), help="Project root directory")
    parser.add_argument("--output", help="Optional output file path")
    parser.add_argument("--include-summary", action="store_true", help="Include directory summary")
    parser.add_argument("--compress", action="store_true", help="Compress the output context block")

    args = parser.parse_args()
    components = [c.strip() for c in args.request.split(",") if c.strip()]

    context_output = dispatch_context(components, args.project_root, args.include_summary)

    if args.compress:
        compressed_bytes = zlib.compress(context_output.encode("utf-8"))
        context_output = base64.b64encode(compressed_bytes).decode("utf-8")
        context_output = "# 📦 Compressed Output (Base64 Encoded)\n" + context_output

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(context_output)
        print(f"✅ Context dispatched to: {args.output}")
    else:
        print("\n" + context_output)


if __name__ == "__main__":
    main()
