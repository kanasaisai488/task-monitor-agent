
# 🧠 TaskMonitorAgent – Agentic Research Automation Framework

A modular, intelligent agentic framework designed to assist with quantitative research workflows, file monitoring, LLM-based prompt generation, git integration, and collaborative task tracking.

---

## 🚀 Key Features
- ✅ Live file monitoring with diff tracker
- 🤖 LLM prompt generator (modular and agentic)
- 📊 Task memory database (SQLite-based)
- 🔁 Human feedback collection and git auto-commit
- 📤 Task summary export (CSV, JSON, Markdown)
- 📂 Multi-project support with tagging and SOPs
- 🔧 CLI tools and Makefile-driven automation

---

## 📁 Project Structure

```
quant_agentic_research/
├── agents/                  # Modular AI agent logic
├── core/                    # Orchestrators and handlers
├── config/                  # Config files
├── templates/               # Code prompt templates
├── cli_tools/               # Dashboard, exporter, batch tools
├── storage/                 # Prompt blocks, logs
├── data/, reports/, tests/  # Supporting folders
├── main.py                  # Live watcher
├── project_initializer.py   # New project scaffolder
├── Makefile                 # CLI automation commands
├── progress_log.md
├── COLLAB_SOP.md
├── Makefile_QuickRef.md
├── User_Tutorial_FullGuide.md
└── README.md
```

---

## 🧑‍💻 Getting Started

### 🔧 Setup Environment
```bash
make setup
```

### 📂 Create New Project
```bash
make init-project
```

### 👁️ Start Monitoring
```bash
make watch
```

### 🔁 Provide Feedback
```bash
make feedback
```

### 📊 Dashboard & Summary
```bash
make dashboard
make summary
```

---

## 📎 Collaboration SOP
- Follow `COLLAB_SOP.md` for human-LLM interaction flow
- Use `[SA]`, `[EM]`, `[LP]` git commit prefixes
- Update `progress_log.md` on each task

---

## 📤 Export Reports
```bash
make summary
```
Exports are stored in `/exports/`.

---

## 📚 Documentation
- `User_Tutorial_FullGuide.md` – Full user guide
- `Makefile_QuickRef.md` – Makefile usage reference
- `COLLAB_SOP.md` – LLM/human collaboration standard
- `context_dispatcher.py` – Extract modular code blocks for LLM
- `context_inquiry_prompt.py` – Kickstart an LLM-led code request session
---

## 📌 License
MIT (or insert your own license here)

---

## ✨ Built by Quant Minds. Powered by LLMs.
