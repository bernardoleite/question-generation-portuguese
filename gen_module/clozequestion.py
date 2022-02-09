import random

class ClozeQuestion:
    def __init__(self, cloze_uuid, cloze_type, stat_text, cloze_question, cloze_answer, cloze_diff):
        self.cloze_uuid = cloze_uuid
        self.type = 'cloze'
        self.stat_text = stat_text
        self.cloze_question = cloze_question
        self.cloze_answer = cloze_answer
        self.cloze_diff = cloze_diff
    
    def getQuestion(self):
        question_string = "\n" + self.stat_text + "\n" + self.cloze_question + "\n"
        return question_string
