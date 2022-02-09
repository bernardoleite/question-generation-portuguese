
class MySentenceStats:
    def __init__(self):
        self.DET = {'qty': 0, 'indexes': []}
        self.DET_ARTICLE_DEFINITE = {'qty': 0, 'indexes': []}
        self.DET_ARTICLE_INDEFINITE = {'qty': 0, 'indexes': []}
        self.DET_POSSESSIVE = {'qty': 0, 'indexes': []}
        self.DET_DEMONSTRATIVE = {'qty': 0, 'indexes': []}
        self.DET_INDEFINITE = {'qty': 0, 'indexes': []}
        self.DET_RELATIVE = {'qty': 0, 'indexes': []}
        self.DET_INTERROGATIVE = {'qty': 0, 'indexes': []}

        self.PRON = {'qty': 0, 'indexes': []}
        self.PRON_PERSONAL = {'qty': 0, 'indexes': []}
        self.PRON_POSSESSIVE = {'qty': 0, 'indexes': []}
        self.PRON_DEMONSTRATIVE = {'qty': 0, 'indexes': []}
        self.PRON_INDEFINITE = {'qty': 0, 'indexes': []}
        self.PRON_RELATIVE = {'qty': 0, 'indexes': []}
        self.PRON_INTERROGATIVE = {'qty': 0, 'indexes': []}

        self.ADV = {'qty': 0, 'indexes': []}
        self.ADV_MODE = {'qty': 0, 'indexes': []}
        self.ADV_TIME = {'qty': 0, 'indexes': []}
        self.ADV_LOCAL = {'qty': 0, 'indexes': []}
        self.ADV_DEGREE = {'qty': 0, 'indexes': []}
        self.ADV_AFFIRMATION = {'qty': 0, 'indexes': []}
        self.ADV_NEGATION = {'qty': 0, 'indexes': []}
        self.ADV_INCLUSION = {'qty': 0, 'indexes': []}
        self.ADV_EXCLUSION = {'qty': 0, 'indexes': []}
        self.ADV_DOUBT = {'qty': 0, 'indexes': []}
        self.ADV_DESIGNATION = {'qty': 0, 'indexes': []}
        self.ADV_INTERROGATIVE = {'qty': 0, 'indexes': []}
        self.ADV_CONNECTIVE = {'qty': 0, 'indexes': []}
        self.ADV_RELATIVE = {'qty': 0, 'indexes': []}

        self.CONJ = {'qty': 0, 'indexes': []}

        self.CCONJ = {'qty': 0, 'indexes': []}
        self.CCONJ_COPULATIVE = {'qty': 0, 'indexes': []}
        self.CCONJ_ADVERSATIVE = {'qty': 0, 'indexes': []}
        self.CCONJ_DISJUNCTIVE = {'qty': 0, 'indexes': []}
        self.CCONJ_CONCLUSIVE = {'qty': 0, 'indexes': []}
        self.CCONJ_EXPLICATIVE = {'qty': 0, 'indexes': []}

        self.SCONJ = {'qty': 0, 'indexes': []}
        self.SCONJ_COMPLETIVE = {'qty': 0, 'indexes': []}
        self.SCONJ_CAUSAL = {'qty': 0, 'indexes': []}
        self.SCONJ_FINAL = {'qty': 0, 'indexes': []}
        self.SCONJ_TEMPORAL = {'qty': 0, 'indexes': []}
        self.SCONJ_CONCESSIVE = {'qty': 0, 'indexes': []}
        self.SCONJ_CONDITIONAL = {'qty': 0, 'indexes': []}
        self.SCONJ_COMPARATIVE = {'qty': 0, 'indexes': []}
        self.SCONJ_CONSECUTIVE = {'qty': 0, 'indexes': []}

        self.NOUN = {'qty': 0, 'indexes': []}
        self.NOUN_PROPER = {'qty': 0, 'indexes': []}
        self.NOUN_COMMON = {'qty': 0, 'indexes': []}
        self.NOUN_COLLECTIVE = {'qty': 0, 'indexes': []}

        self.VERB = {'qty': 0, 'indexes': []}
        self.VERB_MAIN = {'qty': 0, 'indexes': []}
        self.VERB_COPULATIVE = {'qty': 0, 'indexes': []}
        self.VERB_AUXILIARY = {'qty': 0, 'indexes': []}

        self.ADJ = {'qty': 0, 'indexes': []}
        self.ADJ_NUMERAL = {'qty': 0, 'indexes': []}
        self.ADJ_QUALIFICATIVE = {'qty': 0, 'indexes': []}

        self.PREP = {'qty': 0, 'indexes': []}
        self.PREP_SIMPLE = {'qty': 0, 'indexes': []}
        self.PREP_CONTRACTED = {'qty': 0, 'indexes': []}

        self.INTJ = {'qty': 0, 'indexes': []}

        self.NR_a = {'qty': 0, 'type': [], 'indexes':[]}

        self.PUNCT = {'qty': 0, 'indexes': []}
        self.PUNCT_FINAL = {'qty': 0, 'indexes': []}
        self.PUNCT_QUESTION = {'qty': 0, 'indexes': []}
        self.PUNCT_EXCLAMATIVE = {'qty': 0, 'indexes': []}
        self.PUNCT_COMMA = {'qty': 0, 'indexes': []}
        self.PUNCT_DASH = {'qty': 0, 'indexes': []}
        self.PUNCT_TWOPOINTS = {'qty': 0, 'indexes': []}
        self.PUNCT_SEMICOLON = {'qty': 0, 'indexes': []}
        self.PUNCT_QUOTATION = {'qty': 0, 'indexes': []}
        self.PUNCT_PARENTHESES = {'qty': 0, 'indexes': []}

        self.NUM = {'qty': 0, 'indexes': []}
        
        #nr of adverbs
        self.DIFFERENT_DEPENDENCIES = {'qty': 0, 'indexes': []}
        self.DIFFERENT_TOKENS = {'qty': 0, 'indexes': []}
        #nr of words

    def addStats(self, sent_tagPtList, sent_depEngList, token, index):
        if token.tag == 'NUM':
            self.NUM['qty'] += 1
            self.NUM['indexes'].append(index)

        elif token.tag == 'ADJ':
            self.ADJ['qty'] += 1
            self.ADJ['indexes'].append(index)
            if token.sub_tag == 'ADJ_QUALIFICATIVE':
                self.ADJ_QUALIFICATIVE['qty'] += 1
                self.ADJ_QUALIFICATIVE['indexes'].append(index)
            elif token.sub_tag == 'ADJ_NUMERAL':
                self.ADJ_NUMERAL['qty'] += 1
                self.ADJ_NUMERAL['indexes'].append(index)
            else:
                pass

        elif token.tag == 'PUNCT':
            self.PUNCT['qty'] += 1
            self.PUNCT['indexes'].append(index)
            if token.sub_tag == 'PUNCT_FINAL':
                self.PUNCT_FINAL['qty'] += 1
                self.PUNCT_FINAL['indexes'].append(index)
            elif token.sub_tag == 'PUNCT_QUESTION':
                self.PUNCT_QUESTION['qty'] += 1
                self.PUNCT_QUESTION['indexes'].append(index)
            elif token.sub_tag == 'PUNCT_EXCLAMATIVE':
                self.PUNCT_EXCLAMATIVE['qty'] += 1
                self.PUNCT_EXCLAMATIVE['indexes'].append(index)
            elif token.sub_tag == 'PUNCT_COMMA':
                self.PUNCT_COMMA['qty'] += 1
                self.PUNCT_COMMA['indexes'].append(index)
            elif token.sub_tag == 'PUNCT_DASH':
                self.PUNCT_DASH['qty'] += 1
                self.PUNCT_DASH['indexes'].append(index)
            elif token.sub_tag == 'PUNCT_TWOPOINTS':
                self.PUNCT_TWOPOINTS['qty'] += 1
                self.PUNCT_TWOPOINTS['indexes'].append(index)
            elif token.sub_tag == 'PUNCT_SEMICOLON':
                self.PUNCT_SEMICOLON['qty'] += 1
                self.PUNCT_SEMICOLON['indexes'].append(index)
            elif token.sub_tag == 'PUNCT_QUOTATION':
                self.PUNCT_QUOTATION['qty'] += 1
                self.PUNCT_QUOTATION['indexes'].append(index)
            elif token.sub_tag == 'PUNCT_QUESTION':
                self.PUNCT_QUESTION['qty'] += 1
                self.PUNCT_QUESTION['indexes'].append(index)
            elif token.sub_tag == 'PUNCT_PARENTHESES':
                self.PUNCT_PARENTHESES['qty'] += 1
                self.PUNCT_PARENTHESES['indexes'].append(index)
            else:
                pass

        elif token.tag == 'VERB':
            self.VERB['qty'] += 1
            self.VERB['indexes'].append(index)
            if token.sub_tag == 'VERB_MAIN':
                self.VERB_MAIN['qty'] += 1
                self.VERB_MAIN['indexes'].append(index)
            elif token.sub_tag == 'VERB_AUXILIARY':
                self.VERB_AUXILIARY['qty'] += 1
                self.VERB_AUXILIARY['indexes'].append(index)
            elif token.sub_tag == 'VERB_COPULATIVE':
                self.VERB_COPULATIVE['qty'] += 1
                self.VERB_COPULATIVE['indexes'].append(index)
            else:
                pass
            if len(token.words) > 1:
                if any(d.text == 'a' and d.upos =='PRON' for d in token.words):
                    self.NR_a['qty'] += 1
                    self.NR_a['type'].append('PRON_CLITIC')
                    self.NR_a['indexes'].append(index)

        elif token.tag == 'PREP':
            self.PREP['qty'] += 1
            self.PREP['indexes'].append(index)
            if token.sub_tag == 'PREP_SIMPLE':
                self.PREP_SIMPLE['qty'] += 1
                self.PREP_SIMPLE['indexes'].append(index)
            elif token.sub_tag == 'PREP_CONTRACTED':
                self.PREP_CONTRACTED['qty'] += 1
                self.PREP_CONTRACTED['indexes'].append(index)
            else:
                pass

        elif token.tag == 'INTJ':
            self.INTJ['qty'] += 1
            self.INTJ['indexes'].append(index)

        elif token.tag == 'DET':
            self.DET['qty'] += 1
            self.DET['indexes'].append(index)
            if token.sub_tag == 'DET_ARTICLE_DEFINITE':
                self.DET_ARTICLE_DEFINITE['qty'] += 1
                self.DET_ARTICLE_DEFINITE['indexes'].append(index)
            elif token.sub_tag == 'DET_ARTICLE_INDEFINITE':
                self.DET_ARTICLE_INDEFINITE['qty'] += 1
                self.DET_ARTICLE_INDEFINITE['indexes'].append(index)
            elif token.sub_tag == 'DET_POSSESSIVE':
                self.DET_POSSESSIVE['qty'] += 1
                self.DET_POSSESSIVE['indexes'].append(index)
            elif token.sub_tag == 'DET_DEMONSTRATIVE':
                self.DET_DEMONSTRATIVE['qty'] += 1
                self.DET_DEMONSTRATIVE['indexes'].append(index)
            elif token.sub_tag == 'DET_INDEFINITE':
                self.DET_INDEFINITE['qty'] += 1
                self.DET_INDEFINITE['indexes'].append(index)
            elif token.sub_tag == 'DET_RELATIVE':
                self.DET_RELATIVE['qty'] += 1
                self.DET_RELATIVE['indexes'].append(index)
            elif token.sub_tag == 'DET_INTERROGATIVE':
                self.DET_INTERROGATIVE['qty'] += 1
                self.DET_INTERROGATIVE['indexes'].append(index)
            else:
                pass

        elif token.tag == 'PRON':
            self.PRON['qty'] += 1
            self.PRON['indexes'].append(index)
            if token.sub_tag == 'PRON_PERSONAL':
                self.PRON_PERSONAL['qty'] += 1
                self.PRON_PERSONAL['indexes'].append(index)
            elif token.sub_tag == 'PRON_POSSESSIVE':
                self.PRON_POSSESSIVE['qty'] += 1
                self.PRON_POSSESSIVE['indexes'].append(index)
            elif token.sub_tag == 'PRON_DEMONSTRATIVE':
                self.PRON_DEMONSTRATIVE['qty'] += 1
                self.PRON_DEMONSTRATIVE['indexes'].append(index)
            elif token.sub_tag == 'PRON_INDEFINITE':
                self.PRON_INDEFINITE['qty'] += 1
                self.PRON_INDEFINITE['indexes'].append(index)
            elif token.sub_tag == 'PRON_RELATIVE':
                self.PRON_RELATIVE['qty'] += 1
                self.PRON_RELATIVE['indexes'].append(index)
            elif token.sub_tag == 'PRON_INTERROGATIVE':
                self.PRON_INTERROGATIVE['qty'] += 1
                self.PRON_INTERROGATIVE['indexes'].append(index)
            else:
                pass

        elif token.tag == 'CONJ':
            self.CONJ['qty'] += 1
            self.CONJ['indexes'].append(index)
            if token.sub_tag == 'CCONJ_COPULATIVE':
                self.CCONJ_COPULATIVE['qty'] += 1
                self.CCONJ_COPULATIVE['indexes'].append(index)
                self.CCONJ['qty'] += 1
                self.CCONJ['indexes'].append(index)
            elif token.sub_tag == 'CCONJ_ADVERSATIVE':
                self.CCONJ_ADVERSATIVE['qty'] += 1
                self.CCONJ_ADVERSATIVE['indexes'].append(index)
                self.CCONJ['qty'] += 1
                self.CCONJ['indexes'].append(index)
            elif token.sub_tag == 'CCONJ_DISJUNCTIVE':
                self.CCONJ_DISJUNCTIVE['qty'] += 1
                self.CCONJ_DISJUNCTIVE['indexes'].append(index)
                self.CCONJ['qty'] += 1
                self.CCONJ['indexes'].append(index)
            elif token.sub_tag == 'CCONJ_CONCLUSIVE':
                self.CCONJ_CONCLUSIVE['qty'] += 1
                self.CCONJ_CONCLUSIVE['indexes'].append(index)
                self.CCONJ['qty'] += 1
                self.CCONJ['indexes'].append(index)
            elif token.sub_tag == 'CCONJ_EXPLICATIVE':
                self.CCONJ_EXPLICATIVE['qty'] += 1
                self.CCONJ_EXPLICATIVE['indexes'].append(index)
                self.CCONJ['qty'] += 1
                self.CCONJ['indexes'].append(index)
            elif token.sub_tag == 'SCONJ_COMPLETIVE':
                self.SCONJ_COMPLETIVE['qty'] += 1
                self.SCONJ_COMPLETIVE['indexes'].append(index)
                self.SCONJ['qty'] += 1
                self.SCONJ['indexes'].append(index)
            elif token.sub_tag == 'SCONJ_CAUSAL':
                self.SCONJ_CAUSAL['qty'] += 1
                self.SCONJ_CAUSAL['indexes'].append(index)
                self.SCONJ['qty'] += 1
                self.SCONJ['indexes'].append(index)
            elif token.sub_tag == 'SCONJ_FINAL':
                self.SCONJ_FINAL['qty'] += 1
                self.SCONJ_FINAL['indexes'].append(index)
                self.SCONJ['qty'] += 1
                self.SCONJ['indexes'].append(index)
            elif token.sub_tag == 'SCONJ_TEMPORAL':
                self.SCONJ_TEMPORAL['qty'] += 1
                self.SCONJ_TEMPORAL['indexes'].append(index)
                self.SCONJ['qty'] += 1
                self.SCONJ['indexes'].append(index)
            elif token.sub_tag == 'SCONJ_CONCESSIVE':
                self.SCONJ_CONCESSIVE['qty'] += 1
                self.SCONJ_CONCESSIVE['indexes'].append(index)
                self.SCONJ['qty'] += 1
                self.SCONJ['indexes'].append(index)
            elif token.sub_tag == 'SCONJ_CONDITIONAL':
                self.SCONJ_CONDITIONAL['qty'] += 1
                self.SCONJ_CONDITIONAL['indexes'].append(index)
                self.SCONJ['qty'] += 1
                self.SCONJ['indexes'].append(index)
            elif token.sub_tag == 'SCONJ_COMPARATIVE':
                self.SCONJ_COMPARATIVE['qty'] += 1
                self.SCONJ_COMPARATIVE['indexes'].append(index)
                self.SCONJ['qty'] += 1
                self.SCONJ['indexes'].append(index)
            elif token.sub_tag == 'SCONJ_CONSECUTIVE':
                self.SCONJ_CONSECUTIVE['qty'] += 1
                self.SCONJ_CONSECUTIVE['indexes'].append(index)
                self.SCONJ['qty'] += 1
                self.SCONJ['indexes'].append(index)
            else:
                pass

        elif token.tag == 'ADV':
            self.ADV['qty'] += 1
            self.ADV['indexes'].append(index)
            if token.sub_tag == 'ADV_MODE':
                self.ADV_MODE['qty'] += 1
                self.ADV_MODE['indexes'].append(index)
            elif token.sub_tag == 'ADV_TIME':
                self.ADV_TIME['qty'] += 1
                self.ADV_TIME['indexes'].append(index)
            elif token.sub_tag == 'ADV_LOCAL':
                self.ADV_LOCAL['qty'] += 1
                self.ADV_LOCAL['indexes'].append(index)
            elif token.sub_tag == 'ADV_DEGREE':
                self.ADV_DEGREE['qty'] += 1
                self.ADV_DEGREE['indexes'].append(index)
            elif token.sub_tag == 'ADV_AFFIRMATION':
                self.ADV_AFFIRMATION['qty'] += 1
                self.ADV_AFFIRMATION['indexes'].append(index)
            elif token.sub_tag == 'ADV_NEGATION':
                self.ADV_NEGATION['qty'] += 1
                self.ADV_NEGATION['indexes'].append(index)
            elif token.sub_tag == 'ADV_INCLUSION':
                self.ADV_INCLUSION['qty'] += 1
                self.ADV_INCLUSION['indexes'].append(index)
            elif token.sub_tag == 'ADV_EXCLUSION':
                self.ADV_EXCLUSION['qty'] += 1
                self.ADV_EXCLUSION['indexes'].append(index)
            elif token.sub_tag == 'ADV_DOUBT':
                self.ADV_DOUBT['qty'] += 1
                self.ADV_DOUBT['indexes'].append(index)
            elif token.sub_tag == 'ADV_DESIGNATION':
                self.ADV_DESIGNATION['qty'] += 1
                self.ADV_DESIGNATION['indexes'].append(index)
            elif token.sub_tag == 'ADV_INTERROGATIVE':
                self.ADV_INTERROGATIVE['qty'] += 1
                self.ADV_INTERROGATIVE['indexes'].append(index)
            elif token.sub_tag == 'ADV_CONNECTIVE':
                self.ADV_CONNECTIVE['qty'] += 1
                self.ADV_CONNECTIVE['indexes'].append(index)
            elif token.sub_tag == 'ADV_RELATIVE':
                self.ADV_RELATIVE['qty'] += 1
                self.ADV_RELATIVE['indexes'].append(index)
            else:
                pass

        if token.text == 'a':
            if token.tag == 'DET': 
                self.NR_a['qty'] += 1
                self.NR_a['type'].append('DET')
                self.NR_a['indexes'].append(index)
            elif token.tag == 'PREP':
                self.NR_a['qty'] += 1
                self.NR_a['type'].append('PREP')
                self.NR_a['indexes'].append(index)
            elif token.tag == 'PRON':
                self.NR_a['qty'] += 1
                self.NR_a['type'].append('PRON_ATOM')
                self.NR_a['indexes'].append(index)
            else:
                pass
        
        if token.text not in sent_tagPtList:
            self.DIFFERENT_TOKENS['qty'] += 1
            self.DIFFERENT_TOKENS['indexes'].append(index)

        if token.words[0].dependency_relation not in sent_depEngList:
            self.DIFFERENT_DEPENDENCIES['qty'] += 1
            self.DIFFERENT_DEPENDENCIES['indexes'].append(index)