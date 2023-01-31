from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    q_text = question["question"]
    q_answer = question["correct_answer"]
    new_q = Question(q_text, q_answer)
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)

# if quiz still has questions remaining
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz 😀")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")

