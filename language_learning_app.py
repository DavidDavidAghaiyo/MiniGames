import random

words = [
   {"spanish": "hola", "english": "hello"},
   {"spanish": "adiós", "english": "goodbye"},
   {"spanish": "gracias", "english": "thank you"},
   {"spanish": "por favor", "english": "please"},
   {"spanish": "sí", "english": "yes"},
   {"spanish": "no", "english": "no"},
   {"spanish": "buenos días", "english": "good morning"},
   {"spanish": "buenas tardes", "english": "good afternoon"},
   {"spanish": "buenas noches", "english": "good night"},
   {"spanish": "lo siento", "english": "I'm sorry"},
   {"spanish": "perdón", "english": "excuse me"},
   {"spanish": "salud", "english": "bless you"},
   {"spanish": "bien", "english": "well"},
   {"spanish": "mal", "english": "bad"},
   {"spanish": "así así", "english": "so-so"},
   {"spanish": "amigo", "english": "friend"},
   {"spanish": "familia", "english": "family"},
   {"spanish": "amor", "english": "love"},
   {"spanish": "feliz", "english": "happy"},
   {"spanish": "triste", "english": "sad"},
   {"spanish": "hermoso", "english": "beautiful"},
   {"spanish": "feo", "english": "ugly"},
   {"spanish": "pequeño", "english": "small"},
   {"spanish": "grande", "english": "big"},
   {"spanish": "nuevo", "english": "new"},
   {"spanish": "viejo", "english": "old"},
   {"spanish": "rápido", "english": "fast"},
   {"spanish": "lento", "english": "slow"},
   {"spanish": "fácil", "english": "easy"},
   {"spanish": "difícil", "english": "difficult"},
   {"spanish": "caro", "english": "expensive"},
   {"spanish": "barato", "english": "cheap"},
   {"spanish": "caliente", "english": "hot"},
   {"spanish": "frío", "english": "cold"},
   {"spanish": "día", "english": "day"},
   {"spanish": "noche", "english": "night"},
   {"spanish": "mañana", "english": "morning/tomorrow"},
   {"spanish": "ayer", "english": "yesterday"},
   {"spanish": "hoy", "english": "today"},
   {"spanish": "ahora", "english": "now"},
   {"spanish": "después", "english": "later"},
   {"spanish": "nunca", "english": "never"},
   {"spanish": "siempre", "english": "always"},
   {"spanish": "a veces", "english": "sometimes"},
   {"spanish": "antes", "english": "before"},
   {"spanish": "yo", "english": "I"},
   {"spanish": "tú", "english": "you"},
   {"spanish": "él", "english": "he"},
   {"spanish": "ella", "english": "she"},
   {"spanish": "nosotros", "english": "we"},
   {"spanish": "vosotros", "english": "you all (Spain)"},
   {"spanish": "ellos", "english": "they"},
   {"spanish": "usted", "english": "you (formal)"},
   {"spanish": "ustedes", "english": "you all (formal)"},
   {"spanish": "tener", "english": "to have"},
   {"spanish": "ser", "english": "to be (permanent)"},
   {"spanish": "estar", "english": "to be (temporary)"},
   {"spanish": "hacer", "english": "to do/make"},
   {"spanish": "poder", "english": "to be able to"},
   {"spanish": "ir", "english": "to go"},
   {"spanish": "ver", "english": "to see"},
   {"spanish": "hablar", "english": "to speak"},
   {"spanish": "comer", "english": "to eat"},
   {"spanish": "beber", "english": "to drink"},
   {"spanish": "dormir", "english": "to sleep"},
   {"spanish": "trabajar", "english": "to work"},
   {"spanish": "jugar", "english": "to play"},
   {"spanish": "vivir", "english": "to live"},
   {"spanish": "venir", "english": "to come"},
   {"spanish": "querer", "english": "to want"},
   {"spanish": "necesitar", "english": "to need"},
   {"spanish": "pensar", "english": "to think"},
   {"spanish": "entender", "english": "to understand"},
   {"spanish": "saber", "english": "to know (a fact)"},
   {"spanish": "conocer", "english": "to know (someone)"},
   {"spanish": "gustar", "english": "to like"},
   {"spanish": "comprar", "english": "to buy"},
   {"spanish": "leer", "english": "to read"},
   {"spanish": "escribir", "english": "to write"},
   {"spanish": "estudiar", "english": "to study"},
   {"spanish": "preguntar", "english": "to ask"},
   {"spanish": "contestar", "english": "to answer"},
   {"spanish": "escuchar", "english": "to listen"},
   {"spanish": "mirar", "english": "to look at"},
   {"spanish": "esperar", "english": "to wait"},
   {"spanish": "abrir", "english": "to open"},
   {"spanish": "cerrar", "english": "to close"},
   {"spanish": "entrar", "english": "to enter"},
   {"spanish": "salir", "english": "to leave"},
   {"spanish": "llamar", "english": "to call"},
   {"spanish": "ayudar", "english": "to help"},
   {"spanish": "viajar", "english": "to travel"},
   {"spanish": "caminar", "english": "to walk"},
   {"spanish": "correr", "english": "to run"},
   {"spanish": "sentarse", "english": "to sit"},
   {"spanish": "levantarse", "english": "to get up"},
   {"spanish": "encontrar", "english": "to find"},
   {"spanish": "perder", "english": "to lose"},
   {"spanish": "recordar", "english": "to remember"},
   {"spanish": "olvidar", "english": "to forget"},
   {"spanish": "empezar", "english": "to start"},
   {"spanish": "terminar", "english": "to finish"},
   {"spanish": "buscar", "english": "to search"},
   {"spanish": "llegar", "english": "to arrive"},
   {"spanish": "decir", "english": "to say"},
   {"spanish": "dar", "english": "to give"}
]


def quiz_user(words):
  random.shuffle(words)
  score = 0

  for index, word in enumerate(words):
    if index == 5:
      break
    print(f" What is the English translation of '{word['spanish']}'?")
    user_answer = input("Your answer: ").strip().lower()
    correct_answer = word['english'].lower()

    if user_answer == correct_answer:
      print("Type shittt \n")
      score = score + 1
    else:
      print(f"You fool, The correct answer is '{word['english']}'.\n")
  print(f"Quiz complete. Your score: {score}/15")





def main():
  print("Welcome to the Agzy LL Flashcards App")
  input("Press Enter to start the quiz...")
  quiz_user(words)

if __name__ == '__main__':
  main()