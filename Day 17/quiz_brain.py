from data import question_data

#TODO:asking the questions
#TODO:checking if the answer was correct
#TODO:checking if we're the end of the quiz

class QuizBrain:
    def __init__(self,q_list):
        self.question_number = 0
        self.questions_list =  q_list
        self.score = 0

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number} : {current_question.text}  : (True/False):\t")
        self.check_answer(user_answer,current_question.answer)

    def still_has_questions(self):
        if(self.question_number < len(question_data)):
            return True
        return False

    def check_answer(self,user_answer, correct_answer):
        if( user_answer.lower() == correct_answer.lower() ):
            print("You got it right!")
            self.score += 1
        else:
            print("That's Wrong.")
        print(f"The Correct Answer is {correct_answer}")
        print(f"Your Current Score {self.score} / {self.question_number}")
        print("\n")