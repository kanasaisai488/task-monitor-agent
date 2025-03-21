
# code_reference_loader.py
import os
import ast

def extract_code_reference(file_path, max_lines=40):
    """
    Extract top-level classes or functions from the file.
    If file is short, return top N lines instead.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        if len(lines) <= max_lines:
            return "".join(lines).strip()

        with open(file_path, "r", encoding="utf-8") as f:
            tree = ast.parse(f.read())

        result_blocks = []
        for node in tree.body:
            if isinstance(node, (ast.ClassDef, ast.FunctionDef)):
                block = ast.get_source_segment("".join(lines), node)
                result_blocks.append(block)

        if not result_blocks:
            return "".join(lines[:max_lines])
        return "\n\n".join(result_blocks[:3])  # Return top 3 definitions max

    except Exception as e:
        return f"# Error extracting code reference: {e}"
