#===================PYTHON QUIZ =========================

questions = ("1. What is the capital of Kenya?",
             "2. WHat is the largest mammal?",
             "3. What is the smallest country in the world?",
             "4. what is the highest mountain in the world?",)


options = (("A. Nairobi", "B.Mombasa", "C. Kisumu", "D. Nakuru"), 
           ("A. Elephant", "B. Blue whale", "C. Giraffe", "D. Hippopotamus"),
           ("A. Vatican City", "B. Monaco", "C. Nauru", "D. Us"),
           ("A. Mount Everest","B. Mount Kilimanjaro","C. Mount Kenya","D. Mount Fuji"))
answers = ("A", "B", "A", "A")
guesses = []
score = 0

question_num = 0

for question in questions:
    print(question)
    for option in options[question_num]:
        print(option)
        
    guess = input("Enter A/ B/ C/ D: ")
    guesses.append(guess)
    if guess.upper() == answers[question_num]:
        score += 1
        print("Correct!")
    
    else:
        print("Wrong!")
        
    question_num += 1
    
print(f"You got {score}/ {len(questions)} ")    

print()

print("========Question(s) you got wrong========")
for i in range(len(questions)):
    if guesses[i] != answers[i]:
        print(questions[i])
        print(f"Your answer: {guesses[i]}")
        print(f"Correct answer: {answers[i]}")
        print()
        
# ============PYTHON GUESSING GAME====================
import random

lowest_num = 1
highest_num = 10

guesses = 0
is_running = True

guess = random.randint(lowest_num, highest_num)
print("==========PYTHON GUESSING GAME===============")
print(f"select a number between {lowest_num} and {highest_num}")

while is_running:
    choice = input("Enter your guess: ")
    guesses += 1

    if choice.isdigit():
        choice = int(choice)
        if choice < lowest_num or choice > highest_num:
            print("Number out of range")
            print(f"select a number between {lowest_num} and {highest_num}")
        elif choice < guess:
            print("Too low, try again!")
        elif choice > guess:
            print("Too high, try again!")
        else:
            print(f"{guess} is CORRECT!")
            print(f"Number of guesses: {guesses}")
            is_running = False
    else:
        print("Invalid!")
        print(f"Please select a number between {lowest_num} and {highest_num}")
        