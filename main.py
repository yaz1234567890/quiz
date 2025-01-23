score = 0
#easy
question1 = "what is the best food"
print (question1)

user_answer = input("your answer: ")

if user_answer. lower() == "bread":
    print("correct")
    score += 1
else:
    print("nuh uh its bread")

#medium
quiz_questions = [
    "how to eat bread?",
    "where was bread first invented?",
    "what can you put on bread?"
]

quiz_answers = [
    "with your mouth",
    "Egypt",
    "butter"
]

print(f"question : {"how to eat bread?"}")
user_answer = input("answer:")
if user_answer == "with your mouth":
    print ("correct")
    score += 1
else:
        print("nuh uh you are wrong")


print(f"question : {"where was bread first invented?"}")
user_answer = input("answer here:")
if user_answer == "Egypt":
    print ("correct")
    score += 1
else:
    print("nuh uh you are wrong")


print(f"question : {"what can you put on bread?"}")
user_answer = input("answer NOW:")
if user_answer == "butter":
    print ("correct")
    score += 1
else:
    print("nuh uh you are wrong")

#hard
import random
with open('questions.txt', 'x') as file:
   f.write("what do you put in bread to make it rize?", '/n'
           "is wheat bread a type of bread?", '/n'
           "should breas come from a can?", '/n')