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

  },

  {
        "prompt": "Who wrote 'Romeo and Juliet'?",
        "options": ["A. William Shakespeare", "B. Charles Dickens", "C. Mark Twain", "D. Jane Austen"],
        "answer": "A"
  },

  {
        "prompt": "What is the chemical symbol for gold?",
        "options": ["A. Au", "B. Ag", "C. Pb", "D. Fe"],
        "answer": "A"
  },


  {
        "prompt": "How many continents are there on Earth?",
        "options": ["A. 5", "B. 6", "C. 7", "D. 8"],
        "answer": "C"
  },
    
  {
        "prompt": "Which planet is known as the Red Planet?",
        "options": ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"],
        "answer": "B"
  },

  {
        "prompt": "What is the largest ocean on Earth?",
        "options": ["A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean"],
        "answer": "D"
  },

  {
        "prompt": "Who painted the Mona Lisa?",
        "options": ["A. Leonardo da Vinci", "B. Vincent van Gogh", "C. Pablo Picasso", "D. Michelangelo"],
        "answer": "A"
  },

  {
        "prompt": "Which gas do plants absorb from the atmosphere?",
        "options": ["A. Oxygen", "B. Carbon Dioxide", "C. Nitrogen", "D. Hydrogen"],
        "answer": "B"
  },

  {
        "prompt": "How many sides does a hexagon have?",
        "options": ["A. 5", "B. 6", "C. 7", "D. 8"],
        "answer": "B"
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

  if score<=8:
    print("Do better bum")
  else:
    print("Thats my guy")

    






run_quiz(questions)