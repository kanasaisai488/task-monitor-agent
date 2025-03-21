//User_Tutorial_FullGuide.md
# 📚 Full Tutorial – How to Use TaskMonitorAgent (Agentic Research Tool)

This guide walks you step-by-step through setup, usage, and best practices to get the most out of your agentic workflow for quant research and LLM-assisted development.

---

## 🔧 Step 1: Setup the Environment
In your project root directory:
```bash
make setup
```
This will:
- Create `myenv/` virtual environment
- Install all dependencies from `requirements.txt`

✅ Alternative:
```bash
make install
```

---

## 📂 Step 2: Initialize a New Quant Research Project
```bash
make init-project
```
You’ll be prompted:
```
📂 Enter full path where to create project: G:/My Drive/QUANT_TOOLS/
🔖 Enter new project folder name: my_strategy_01
🔗 (Optional) Enter Git remote URL: https://github.com/user/my_strategy_01.git
```

It will:
- Scaffold folders
- Create `progress_log.md` and `COLLAB_SOP.md`
- Init Git repo and link remote

---

## 👁️ Step 3: Start Monitoring the Project
```bash
make watch
```
You’ll be prompted:
```
Enter path to project folder: G:/My Drive/QUANT_TOOLS/my_strategy_01
```

Now TaskMonitorAgent will monitor all files inside this project.

---

## ✨ Step 4: Make Code Changes
Any file change triggers prompt generation → commit → logging.

You can then:
- Paste diff into LLM like Grok/Gemini
- Collect feedback
- Update the task as `success` or `needs_review`

---

## 🔁 Step 5: Review and Feedback
```bash
make feedback
```
The tool will:
- Show all tasks with `pending` status
- Ask you: Was this successful?
- Update status and optionally auto-commit/push

---

## 📊 Step 6: View Progress or Export Summary

### Task Dashboard
```bash
make dashboard
```

### Summary Report Export (CSV/JSON/Markdown)
```bash
make summary
```

---

## 💡 Optional Tools
- `batch_prompt_regenerator.py` – Re-generate prompt blocks for review
- `task_summary_exporter.py` – Export task memory DB for reporting
- `project_initializer.py` – Bootstrap new projects faster
- `human_feedback_prompt.py` – Interactive CLI for managing prompt results

---

## ✅ Best Practice Workflow Summary

| Phase | Action |
|-------|--------|
| Planning | Init project → Add SOP |
| Dev | Code change triggers prompt generation |
| Review | Paste to LLM → Run `make feedback` |
| Validation | Commit auto-tracked |
| Export | `make summary` or `make dashboard` |

---

## 🔗 Git Contribution SOP
- Use agent prefix in commits: `[SA]`, `[EM]`, `[LP]`
- Always run `make feedback` before commit
- Branch naming: `feature/<task-name>`

---

## 💬 Still Confused?
Refer to:
- `COLLAB_SOP.md`
- `Makefile_QuickRef.md`
- `README_main.md`

Happy quanting! 🚀
