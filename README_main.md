
# main.py – Agentic Project Monitor CLI

## 📌 Purpose
Watches a quant project folder for file changes and triggers the TaskMonitorAgent pipeline.

## 🚀 Usage
```bash
python main.py --watch-folder "G:/My Drive/QUANT_TOOLS/my_alpha_strategy"
```

## 🧠 Tip
You can integrate this into the Makefile:
```bash
make watch
```
… and dynamically select a folder each time.

## 📂 Recommendation
- Keep `main.py` at project root
- Use `Makefile` to simplify CLI use
- Extend this watcher to include auto diff, prompt, commit pipeline hooks
