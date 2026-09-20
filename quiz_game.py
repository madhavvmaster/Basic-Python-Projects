questions = [
    {"q" : "What is the capital of India?",
     "opt": ["A. Mumbai", "B. Delhi", "C. Kolkata", "D. Chennai"],
     "ans": "B"},
    {"q" : "Which language is used for web development?",
     "opt": ["A. Python", "B. Java", "C. C++", "D. HTML"],
     "ans": "D"},
    {"q" : "Which planet is known as the Red Planet?",
     "opt": ["A. Venus", "B. Mars", "C. Jupiter", "D. Mercury"],
     "ans": "B"},
    {"q" : "Which of these is a mammal?",
     "opt": ["A. Shark", "B. Dolphin", "C. Crocodile", "D. Eagle"],
     "ans": "B"},   
    {"q" : "Which is the largest ocean on Earth?",
     "opt": ["A. Atlantic Ocean", "B. Indian Ocean", "C. Pacific Ocean", "D. Arctic Ocean"],
     "ans": "C"},        
]

score = 0
for i, q in enumerate(questions):
    print(f"Q{i+1}: {q['q']}")
    for opt in q["opt"]:
        print(opt)
    user = input("Your answer (A/B/C/D): ").upper()
    if user == q["ans"]:
        print("Correct!! \n")
        score += 1
    else:
        print(f"Wrong!! Correct answer: {q['ans']}\n")

print(f"Final Score: {score}/{len(questions)}")