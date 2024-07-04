from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    new_question = Question(question["question"], question["correct_answer"])
    question_bank.append(new_question)

game = QuizBrain(question_bank)
while game.still_has_question():
    game.next_question()

print("You have completed the quiz")
print(f"Your final score is: {game.score}/{game.question_num}")
