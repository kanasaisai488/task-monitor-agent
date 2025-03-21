
import os
from datetime import datetime



def generate_prompt_block(task_description, file_path, diff_lines, project_tag="default"):
    PROMPT_DIR = os.path.join(os.path.dirname(__file__), "../storage/prompt_blocks", project_tag)
    os.makedirs(PROMPT_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"prompt_{timestamp}.txt"

    output_path = os.path.join(PROMPT_DIR, filename)

    diff_text = ''.join(diff_lines)

    prompt = f"""## LLM Prompt Block – TaskMonitorAgent

    🔸 Task: {task_description}
    🔸 File Changed: {file_path}

    🔸 Diff Summary:
    \n```diff
    {diff_text}
    ```\n

    🔸 Instructions:
    Please analyze the diff and suggest improvements, refactoring, or test cases if needed.

    ## END OF PROMPT
"""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(prompt)

    return output_path, prompt
