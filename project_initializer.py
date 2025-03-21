
# project_initializer.py – Bootstrap a new quant project directory (Git-ready)

import os
import subprocess

DEFAULT_STRUCTURE = [
    "agents",
    "core",
    "config",
    "templates",
    "interface",
    "reports",
    "data/raw",
    "data/processed",
    "experiments",
    "tests",
    "storage",
    "cli_tools",
    "exports"
]

def create_project_structure(base_path):
    for folder in DEFAULT_STRUCTURE:
        path = os.path.join(base_path, folder)
        os.makedirs(path, exist_ok=True)
        print(f"✅ Created: {path}")

    with open(os.path.join(base_path, "progress_log.md"), "w") as f:
        f.write("# 📈 Progress Log\n\n")

    with open(os.path.join(base_path, "COLLAB_SOP.md"), "w") as f:
        f.write("# 🤝 Collaboration SOP\n\n")

def init_git_repo(base_path):
    try:
        subprocess.run(["git", "init"], cwd=base_path, check=True)
        print("📁 Git repository initialized.")

        remote_url = input("🔗 (Optional) Enter Git remote URL (leave blank to skip): ").strip()
        if remote_url:
            subprocess.run(["git", "remote", "add", "origin", remote_url], cwd=base_path, check=True)
            print(f"✅ Git remote added: {remote_url}")
    except Exception as e:
        print(f"⚠️ Git init error: {e}")

if __name__ == "__main__":
    print("🚀 Quant Project Bootstrap Tool")

    target_path = input("📂 Enter full path where to create project: ").strip()
    if not os.path.exists(target_path):
        os.makedirs(target_path)
        print(f"📁 Directory created: {target_path}")

    project_name = input("🔖 Enter new project folder name: ").strip()
    if not project_name:
        print("⚠️ Invalid name. Aborting.")
        exit()

    base_path = os.path.join(target_path, project_name)
    os.makedirs(base_path, exist_ok=True)

    create_project_structure(base_path)
    init_git_repo(base_path)

    print(f"🎉 Project '{project_name}' ready at: {base_path}")
