

print(" Welcome to Mind building Quiz game.")
print()

uc =int( input(''' Do you want to play?
1. Yes
2. No \n'''))

if uc == 1:
    int(input('''In which subject?
   1. Science
   2. GK \n'''))
if uc == 1:
    print(" Here are the Science questions...")

questions = ("1. How many elements are there in periodic table?",
             "2. Which animal lays the largest eggs?",
             "3. Which is the most abundant gas in the Earth's atmosphere?",
             "4. How many bones are there in the human body?",
             "5. Which planet in the solar system is the hottest?")

options = (("a. 116", "b. 117", "c. 118", "d. 119"),
           ("a. whale ", "b. crocodile", "c. elephant", "d. ostrich"),
           ("a. nitrogen", "b. oxygen", "c. helium", "d. carbon-dioxide"),
           ("a. 206", "b. 207", "c. 208", "d.209"),
           ("a. mercury", "b. venus", "c. jupiter", "d. earth"))

answers = ("c", "d", "a", "a", "b")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("_____________________________")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter (a,b,c,d) :-")
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT")
    else:
        print("INCORRECT")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("_____________________")
print("   RESULTS       ")
print("_____________________")

print(" answers: ", end="")
for answer in answers:
    print(answer, end="")
print()

print(" guesses: ", end="")
for guess in guesses:
    print(guess, end="")
print()

score = int(score / len(questions) * 100)
print(f"Your score is:{score}%")
breakpoint()

if uc == 2:
    print("Here are the GK Questions...")

questions = ("1. Who is Known as Iron Man of India?",
             "2. What is Capital of India?",
             "3. In which state 'statue of unity' established?",
             "4. Which state is known as 'land of rising sun'?",
             "5. Name the national bird of India?")

options = (("a. Mahatma Gandhi", "b. Sardar Vallabhbhai patel", "c. Jawahar Lal Nehru", "d. Bhagat singh"),
           ("a. Delhi ", "b. Mumbai", "c. Kerala", "d. Gujrat"),
           ("a. Rajasthan", "b. Maharashtra", "c. Gujarat", "d. Uttar Pradesh"),
           ("a. Arunanchal Pradesh", "b. Rajasthan", "c. West bengal", "d.Jammu kashmir"),
           ("a. Elephant", "b. Lion", "c. Kingfisher", "d.Peacock "))

answers = ("b", "a", "c", "a", "d")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("_____________________________")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter (a,b,c,d) :-")
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT")
    else:
        print("INCORRECT")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("_____________________")
print("   RESULTS       ")
print("_____________________")

print(" answers: ", end="")
for answer in answers:
    print(answer, end="")
print()

print(" guesses: ", end="")
for guess in guesses:
    print(guess, end="")
print()

score = int(score / len(questions) * 100)
print(f"Your score is:{score}%")

print(" Thank You For Playing The Game!!😊")


