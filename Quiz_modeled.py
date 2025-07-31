questions = [
    {"question": "What is the capital of france?",
     "options": ["a) Paris", "b) London", "c) Berlin", "d) Madrid"], 
     "answer": "a"},
     {"question":"What is 249-2878?",
      "options": ["a) -2629", "b) -2628", "c) -2627", "d) -2626"],
      "answer": "a"},
      {"question": "What is the capital of India?",
       "options": ["a) New Delhi", "b) Mumbai", "c) Kolkata", "d) Chennai"],
       "answer": "a"},
       {"question": "What is the largest planet in our solar system?",
        "options": ["a) Earth", "b) Mars", "c) Jupiter", "d) Saturn"],
        "answer": "c"},
        {"question": "What is the chemical symbol for water?",
         "options": ["a) H2O", "b) CO2", "c) O2", "d) NaCl"],
         "answer": "a"
         }
]
score = 0
print("Welcome to the quiz")
for q in questions:
      print("\n?", q["question"])
      for opt in q["options"]:
            print("-", opt)
      user_ans = input("Enter your answer (a/b/c/d): ")
      if user_ans.strip().lower() == q["answer"]:
            print("Awesome correct answer")
            score += 1
      else:
            print("Wrong answer")
            print("correct answer is",q["answer"])

if score == len(questions):
    print("Congratulations! You got all answers correct!")
elif score == 0:
    print("Better luck next time!")
else:
    print(f"Good try! You scored {score} out of {len(questions)}. Keep practicing to improve your score.")
                   

