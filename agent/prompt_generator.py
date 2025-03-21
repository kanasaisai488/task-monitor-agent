
# prompt_generator.py
import os
from datetime import datetime
from agent import code_reference_loader

EXCLUDE_DIRS = {'.git', '__pycache__', 'venv', '.venv', 'myenv', '.idea', '.vscode'}
EXCLUDE_FILES = {'desktop.ini'}

def generate_directory_summary(project_dir):
    summary_lines = []
    for root, dirs, files in os.walk(project_dir):
        if any(excluded in root.split(os.sep) for excluded in EXCLUDE_DIRS):
            continue
        level = root.replace(project_dir, '').count(os.sep)
        indent = '    ' * level
        folder_name = os.path.basename(root)
        summary_lines.append(f"{indent}/" + folder_name + "/")
        subindent = '    ' * (level + 1)
        for f in files:
            if f in EXCLUDE_FILES:
                continue
            summary_lines.append(f"{subindent}- {f}")
    return "\n".join(summary_lines)

def load_special_instructions(project_dir):
    instruction_path = os.path.join(project_dir, "special_instructions.txt")
    if os.path.exists(instruction_path):
        with open(instruction_path, "r", encoding="utf-8") as f:
            return f.read().strip()
    return None

def generate_prompt_block(project_tag, file_path, diff_text, task_description, include_code_reference=True):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    project_dir = os.path.abspath(os.path.join(file_path, "..", ".."))  # infer root from file location
    folder_summary = generate_directory_summary(project_dir)
    special_instructions = load_special_instructions(project_dir)
    code_reference = code_reference_loader.extract_code_reference(file_path)

    if isinstance(diff_text, list):
        diff_text = "\n".join(diff_text[:80])  # Limit for safety

    prompt = f"""## LLM Prompt Block – TaskMonitorAgent

🔸 Timestamp: {timestamp}
🔸 Project Tag: {project_tag}
🔸 Task: {task_description}
🔸 File Changed: {file_path}

🔸 Project Folder Structure:
{folder_summary}
"""

    if include_code_reference and code_reference:
        prompt += f"""

🔸 Code Reference (Top Level Class/Function):
```python
{code_reference.strip()}
```"""

    prompt += f"""

🔸 Diff Summary:
```diff
{diff_text.strip()}
```

🔸 Instructions:
Please analyze the code change above and suggest improvements, refactoring ideas, or modularization strategies.
"""

    if special_instructions:
        prompt += f"""
🔸 Additional Project Constraints:
{special_instructions}
"""

    prompt += "\n## END OF PROMPT"
    return prompt



def generate_context_inquiry_prompt(project_tag, task_description, project_dir=None):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if project_dir is None:
        project_dir = os.getcwd()

    folder_summary = generate_directory_summary(project_dir)
    special_instructions = load_special_instructions(project_dir)

    prompt = f"""## LLM Context Inquiry – TaskMonitorAgent

🔸 Timestamp: {timestamp}
🔸 Project Tag: {project_tag}
🔸 Task: {task_description}

🔸 Project Folder Structure:
{folder_summary}
"""

    if special_instructions:
        prompt += f"""

🔸 Additional Project Constraints:
{special_instructions}
"""

    prompt += """
🔸 Instructions:
You are preparing to assist with a complex system. Please specify exactly what classes, modules, or functions you want context for.

You may reply with: “Please provide context for DatabaseConnector and ProgressUpdater.”

## END OF PROMPT
"""
    return prompt
