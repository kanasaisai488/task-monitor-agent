
# 📘 Prompt Crafting Guide – TaskMonitorAgent Workflow

This cheat sheet helps humans and agents craft effective prompts and inject special instructions in an automated loop.

---

## ✅ Task Declaration Format
Write tasks clearly in `progress_log.md` or a markdown doc:
```
TASK #001: Build Binance Data Pipeline
- Connect WebSocket + REST API
- Normalize OHLCV
- Store into TimescaleDB
```

## ✅ Code Placement
Edit files under proper folders (`/core/`, `/agents/`, `/cli_tools/`, etc.)
Save = auto-trigger prompt block.

---

## 📂 Auto-Prompt Block Includes:
- Timestamp
- Project folder structure
- File changed
- Code diff (auto-detected)
- Task title
- Special constraints (optional memory injection)

---

## 💡 Adding Special Instructions (e.g., C#5 compatibility)
You can pass a `special_instructions.txt` in project root. Example content:
```
- Target framework is C# 5. Avoid using 'out', tuples, or modern collection initializers.
- Use only syntax compatible with Visual Studio 2013.
```

This is auto-injected into every prompt block when available.

---

## 🔁 Review Flow
1. TaskPlan → Edit Code → Prompt auto-generated
2. Paste prompt block into Grok/Gemini
3. Paste response → Save → Next prompt generated
4. Finalize using `make feedback`
