from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

question_bank = []
for question in question_data:
    #print(question['text'] + ' ' + question['answer'])
    new_question = Question(question['text'], question['answer'])
    question_bank.append(new_question)

# print(question_bank[11].text)
quiz = QuizBrain(question_bank)
# quiz.next_question()
# quiz.still_has_question()

while quiz.still_has_question():
    quiz.next_question()

if not quiz.still_has_question():
    print("================================")
    print("You've completed the quiz")
    quiz.final_score()
