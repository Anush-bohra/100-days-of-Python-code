questions = [
    {
        "question": "What is the capital of France?",
        "options": ["a) Paris", "b) London", "c) Rome"],
        "answer": "a"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["a) Earth", "b) Mars", "c) Jupiter"],
        "answer": "b"
    },
    {
        "question": "Who developed Python?",
        "options": ["a) Dennis Ritchie", "b) Guido van Rossum", "c) James Gosling"],
        "answer": "b"
    }
]

score = 0

print("Welcome to the Quiz App!\n")

for q in questions:
    print(q["question"])
    for option in q["options"]:
        print(option)
    answer = input("Enter your answer (a/b/c): ").lower()

    if answer == q["answer"]:
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong! The correct answer was {q['answer']}.\n")

print(f"Your final score is {score}/{len(questions)} 🎉")
