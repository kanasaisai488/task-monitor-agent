
# Module: feedback_collector.py

try:
    import questionary
    USE_QUESTIONARY = True
except ImportError:
    USE_QUESTIONARY = False

def collect_feedback(task_description):
    print(f"\n🔍 Task Feedback Collection")
    print(f"📄 Task: {task_description}")

    if USE_QUESTIONARY:
        status = questionary.select(
            "Was this task successful?",
            choices=["success", "failed", "needs_review"]
        ).ask()

        rating = questionary.select(
            "Rate the output quality (1 = poor, 5 = excellent):",
            choices=["1", "2", "3", "4", "5"]
        ).ask()

        notes = questionary.text("Any additional notes or comments?").ask()

    else:
        status = input("Was this task successful? (success/failed/needs_review): ").strip()
        rating = input("Rate the output quality (1-5): ").strip()
        notes = input("Any additional notes? ").strip()

    return {
        "status": status,
        "rating": rating,
        "notes": notes
    }
