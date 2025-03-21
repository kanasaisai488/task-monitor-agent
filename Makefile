
# Makefile – TaskMonitorAgent CLI Shortcuts

setup:
	@echo "🔧 Setting up virtual environment..."
	python -m venv myenv
	myenv/Scripts/pip install -r requirements.txt

install:
	@echo "📦 Installing dependencies..."
	myenv/Scripts/pip install -r requirements.txt

test:
	@echo "🧪 Running main_tester..."
	myenv/Scripts/python main_tester.py

dashboard:
	@echo "📊 Launching dashboard CLI..."
	myenv/Scripts/python cli_tools/task_dashboard_cli.py

summary:
	@echo "📤 Exporting summary report..."
	myenv/Scripts/python cli_tools/task_summary_exporter.py

feedback:
	@echo "🔁 Running interactive human feedback reviewer..."
	myenv/Scripts/python human_feedback_prompt.py

init-project:
	@echo "📂 Bootstrap new quant project..."
	python project_initializer.py

import-legacy:
	@echo "📥 Importing legacy codebase and generating task list..."
	myenv/Scripts/python legacy_code_import_assistant.py

watch:
	@echo "👁️ Launch TaskMonitorAgent for selected project folder..."
	@read -p 'Enter path to project folder: ' folder && myenv/Scripts/python main.py --watch-folder "$$folder"

inquiry:
	@echo "📩 Generating context inquiry prompt..."
	myenv/Scripts/python cli_tools/context_inquiry_prompt.py --project-tag "$(TAG)" --task "$(TASK)" --output inquiry_prompt.txt
