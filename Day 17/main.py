from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question['text']
    question_answer = question['answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# for question in question_data:
#     for v in question.values():
#         question_bank.append(Question(v))

# print(question_bank[0].answer)
quiz = QuizBrain(question_bank)
quiz.next_question()