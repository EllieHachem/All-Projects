#create a model for our question in our quize (what attribute it should have ) like text attribute and hold an answer 
# so true and false AttributeError
#120 charachter is bad as well as try to intendent list good idea training 
#save project to dictonary to rid  of all problems in pycharm 


from question_model import Question
from data import question_data
from quiz_brain import Quiz
question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    question_new = Question(question_text,question_answer)
    question_bank.append(question_new)

#always start with variable name(fully) then the edit wwith _ make it easy to read + use 
quiz = Quiz(question_bank)

while quiz.question_still_has:
    quiz.question_next()