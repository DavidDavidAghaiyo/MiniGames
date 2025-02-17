questions = [

  {

    "prompt": "What is the captial of France?",
    "options": ["A. Paris", "B. Malawi", "C. Berlin", "D. Madrid"],
    "answer": "A"
  },

  {

    "prompt": "Which language is spoken in Brazil?",
    "options": ["A. English", "B. Portugese", "C. Mandarin", "D.Spanish"],
    "answer": "B"

  },

  {
    "prompt": "What is the smallest prime number",
    "options": ["A. 1", "B. 2", "C. 3", "D. 5"],
    "answer": "B"
  },

  {

    "prompt": "Who wrote 'To Kill a MockingBird' ",
    "options": ["A. Harper Lee", "B. Mark Twain", "C. JK Rowling", "D. Ernest Hemmingway"],
    "answer": "A"

  }

  
]

def run_quiz(questions):
  score = 0

  for question in questions:
    print(question["prompt"])
    for option in question["options"]:
      print(option)
    answer = input("Enter your answer (A, B, C or D): ").upper()
    if answer == question["answer"]:
      print("Correct, Hooray!!\n")
      score = score + 1

    else:
      print("Nah g, the correct answer was " , question["answer"], "\n")
  print(f"You got {score} out of {len(questions)} questions correct. ")

  if score<=2:
    print("Do better bum")
  else:
    print("Thats my guy")

    






run_quiz(questions)