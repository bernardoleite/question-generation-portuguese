import random

class FactQuestion:
    def __init__(self, fact_uuid, fact_type, fact_subtype, sent_text, tokens, fact_answer, fact_diff):
        self.fact_uuid = fact_uuid
        self.fact_type = fact_type
        self.fact_subtype = fact_subtype
        self.sent_text = sent_text
        self.tokens_question = tokens
        self.state = 'APPROVED'
        self.fact_answer = fact_answer
        self.diff = fact_diff
        self.question_text = self.tokens2string()
        self.list_string_question = self.tokens2lstring()

    def updateQuestion(self):
        self.question_text = self.tokens2string()
    
    def tokens2string(self):
        fact_question = ''
        for token in self.tokens_question:
            if token.text == '?':
                fact_question = fact_question + token.text
            else:
                fact_question = fact_question + ' ' + token.text
        return fact_question

    def tokens2lstring(self):
        question_list_string = []
        for token in self.tokens_question:
            question_list_string.append(token.text)
        return question_list_string
    
    def getQuestion(self):
        question_text = self.tokens2string()
        question_string = "\n Frase: " + self.sent_text + "\n Questão: " + question_text + "\n Resposta: " + self.fact_answer + "\n Dificuldade: " + str(self.diff) + "\n Estado: " + self.state +  "\n" 
        return question_string
