class Quiz:
    def __init__(self,Question_list):
        self.Question_Number = 0
        self.Question_list = Question_list
        score = 0 
    def question_still_has(self):
       if  self.Question_number > len(self.Question_list):
        return True
       else:
           return False


    def question_next(self):
        question_ask = self.Question_list[self.Question_Number]
        self.Question_Number += 1
        user_answer = input(f"Q.{self.Question_Number}: {question_ask.text}true or false")
         self.answer_check(user_answer, questio n_current.answer)

def question_check(self, user_answer, correct_answer):
    if user_answer.lower() == correct_answer():
        print("right")
        score += 1
    else:
        print("wrong")    
 print(f" the correct answer is was{correct_answer}")
 print(f"your currecnt score is {score})
 print("\n")