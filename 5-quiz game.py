questions = ("What is my father's name?",
             "What is my faculty name?",
             "What is my department name?",
             "What is my grandfather's name?",
             "What is my family name?")

answers = (
    ("A. Sabry", "B. Fawzy", "C. Yasser", "D. Hamada"),
    ("A. FCI", "B. Law", "C. Agricultural", "D. Medicine"),
    ("A. IT", "B. Law in Rights", "C. Bostins", "D. Cardiology"),
    ("A. Sabry", "B. Medhat", "C. Yasser", "D. Farrag"),
    ("A. Torky", "B. Dora", "C. Sirriys", "D. Shaheen")
)

guesses = []
right_answers = ['c', 'a', 'a', 'd', 'a']
score = 0

for counter, (question, answer) in enumerate(zip(questions, answers)):
    print(f"{counter + 1}. {question}")
    for option in answer:
        print(option)
    
    answer_of_question = input("Enter Your Answer: ").lower()
    guesses.append(answer_of_question)
    
    if answer_of_question == right_answers[counter]:
        print("Correct!")
    else:
        print("Wrong")
    print()  

for user_answer, correct_answer in zip(guesses, right_answers):
    if user_answer == correct_answer:
        score += 1

if score >= 3:
    print(f"Awesome! Your Score is: {score}/5")
else:
    print(f"Not Bad! You Got: {score}/5")