class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list

    def next_question(self):
        self.current_question = self.question_list[self.question_number].text
        self.response = input(f"Q{self.question_number + 1}: {self.current_question} (True/False)? ").lower()



