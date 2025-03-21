
# 📄 Makefile Quick Reference – TaskMonitorAgent

This document explains all available Makefile commands for team use.

---

## ✅ Setup & Installation

| Command | Description |
|--------|-------------|
| `make setup` | Create virtual environment `myenv/` and install required packages |
| `make install` | Install dependencies inside existing `myenv` |
| `make test` | Run full test pipeline via `main_tester.py` |

---

## 📊 Monitoring & Reporting Tools

| Command | Description |
|--------|-------------|
| `make dashboard` | Launch terminal dashboard for task overview |
| `make summary` | Export task summary reports (CSV/JSON/Markdown) |
| `make feedback` | Launch human feedback interface (interactive CLI) |

---

## 📂 Project Creation & Monitoring

| Command | Description |
|--------|-------------|
| `make init-project` | Launch `project_initializer.py` to scaffold new quant project |
| `make watch` | Start live folder monitoring (TaskMonitorAgent) for selected project |
| `make import-legacy` | Import legacy project and auto-generate task declarations inside |

💡 On `make watch`, you will be prompted:
```bash
Enter path to project folder: 
```
Just paste in the full path to your new project directory.

---

## 📎 Notes
- Run `make` from the root folder of TaskMonitorAgent project.
- You can add more CLI tools under `cli_tools/` and extend Makefile accordingly.
- Git auto-commit and push behavior are triggered after success status during feedback review.

---

## 💡 Tip for New Team Members
- Run `make init-project` when starting a new quant research idea
- Use `make feedback` after pasting LLM-generated code
- Use `make summary` before project review or reporting

