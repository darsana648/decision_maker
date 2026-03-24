from django.shortcuts import render

# 🔥 AI LOGIC
def smart_decision(tasks, mood):
    if mood == "low":
        tasks = sorted(tasks, key=lambda x: (x['difficulty'], -x['priority']))
    else:
        tasks = sorted(tasks, key=lambda x: (-x['priority'], x['difficulty']))

    return [task['name'] for task in tasks]


# 🔥 TEXT PARSER
def parse_text(text):
    text = text.lower()

    mood = "low" if "tired" in text or "lazy" in text else "high"

    tasks = []

    if "study" in text:
        tasks.append({"name": "Study", "priority": 5, "difficulty": 3})

    if "project" in text:
        tasks.append({"name": "Build Project", "priority": 4, "difficulty": 4})

    if "workout" in text:
        tasks.append({"name": "Workout", "priority": 3, "difficulty": 2})

    if not tasks:
        tasks.append({"name": "General Task", "priority": 3, "difficulty": 2})

    return mood, tasks


# 🔥 MAIN VIEW (NO REST)
def home(request):
    result = []
    mood = None
    tasks = []

    if request.method == "POST":
        text = request.POST.get("text")

        mood, tasks = parse_text(text)
        result = smart_decision(tasks, mood)

    return render(request, "index.html", {
        "result": result,
        "mood": mood,
        "tasks": tasks
    })