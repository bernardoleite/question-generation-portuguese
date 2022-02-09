
class MyTextStats:
    def __init__(self):
        self.DET = [0, []]
        self.DET_ARTICLE_DEFINITE = [0, []]
        self.DET_ARTICLE_INDEFINITE = [0, []]
        self.DET_POSSESSIVE = [0, []]
        self.DET_DEMONSTRATIVE = [0, []]
        self.DET_INDEFINITE = [0, []]
        self.DET_RELATIVE = [0, []]
        self.DET_INTERROGATIVE = [0, []]

        self.PRON = [0, []]
        self.PRON_POSSESSIVE = [0, []]
        self.PRON_DEMONSTRATIVE = [0, []]
        self.PRON_INDEFINITE = [0, []]
        self.PRON_RELATIVE = [0, []]
        self.PRON_INTERROGATIVE = [0, []]

        self.ADV = [0, []]
        self.ADV_MODE = [0, []]
        self.ADV_TIME = [0, []]
        self.ADV_LOCAL = [0, []]
        self.ADV_DEGREE = [0, []]
        self.ADV_AFFIRMATION = [0, []]
        self.ADV_NEGATION = [0, []]
        self.ADV_INCLUSION = [0, []]
        self.ADV_EXCLUSION = [0, []]
        self.ADV_DOUBT = [0, []]
        self.ADV_DESIGNATION = [0, []]
        self.ADV_INTERROGATIVE = [0, []]
        self.ADV_CONNECTIVE = [0, []]
        self.ADV_RELATIVE = [0, []]

        self.CCONJ = [0, []]
        self.CCONJ_COPULATIVE = [0, []]
        self.CCONJ_ADVERSATIVE = [0, []]
        self.CCONJ_DISJUNCTIVE = [0, []]
        self.CCONJ_CONCLUSIVE = [0, []]
        self.CCONJ_EXPLICATIVE = [0, []]

        self.SCONJ = [0, []]
        self.SCONJ_COMPLETIVE = [0, []]
        self.SCONJ_CAUSAL = [0, []]
        self.SCONJ_FINAL = [0, []]
        self.SCONJ_TEMPORAL = [0, []]
        self.SCONJ_CONCESSIVE = [0, []]
        self.SCONJ_CONDITIONAL = [0, []]
        self.SCONJ_COMPARATIVE = [0, []]
        self.SCONJ_CONSECUTIVE = [0, []]

        self.NOUN = [0, []]
        self.NOUN_PROPER = [0, []]
        self.NOUN_COMMON = [0, []]
        self.NOUN_COLLECTIVE = [0, []]

        self.VERB = [0, []]
        self.VERB_MAIN = [0, []]
        self.VERB_COPULATIVE = [0, []]
        self.VERB_AUXILIARY = [0, []]

        self.ADJ = [0, []]
        self.ADJ_NUMERAL = [0, []]
        self.ADJ_QUALIFICATIVE = [0, []]

        self.PREP = [0, []]
        self.PREP_SIMPLE = [0, []]
        self.PREP_CONTRACTED = [0, []]

        self.INTJ = [0, []]

    def addStats(self, token, index):
       if token.tag == 'ADJ':
        self.ADJ[0] += 1
        self.ADJ[1].append(index)
        if token.sub_tag == 'ADJ_QUALIFICATIVE':
            self.ADJ_QUALIFICATIVE[0] += 1
            if index not in self.ADJ_QUALIFICATIVE[1]:
                self.ADJ_QUALIFICATIVE[1].append(index)
        elif token.sub_tag == 'ADJ_NUMERAL':
            self.ADJ_NUMERAL[0] += 1
            if index not in self.ADJ_NUMERAL[1]:
                self.ADJ_NUMERAL[1].append(index)
        else:
            pass

       elif token.tag == 'VERB':
        self.VERB[0] += 1
        self.VERB[1].append(index)
        if token.sub_tag == 'VERB_MAIN':
            self.VERB_MAIN[0] += 1
            if index not in self.VERB_MAIN[1]:
                self.VERB_MAIN[1].append(index)
        elif token.sub_tag == 'VERB_AUXILIARY':
            self.VERB_AUXILIARY[0] += 1
            if index not in self.VERB_MAIN[1]:
                self.VERB_AUXILIARY[1].append(index)
        elif token.sub_tag == 'VERB_COPULATIVE':
            self.VERB_COPULATIVE[0] += 1
            if index not in self.VERB_MAIN[1]:
                self.VERB_COPULATIVE[1].append(index)
        else:
            pass

       elif token.tag == 'PREP':
        self.PREP[0] += 1
        self.PREP[1].append(index)
        if token.sub_tag == 'PREP_SIMPLE':
            self.PREP_SIMPLE[0] += 1
            if index not in self.VERB_MAIN[1]:
                self.PREP_SIMPLE[1].append(index)
        elif token.sub_tag == 'PREP_CONTRACTED':
            self.PREP_CONTRACTED[0] += 1
            if index not in self.VERB_MAIN[1]:
                self.PREP_CONTRACTED[1].append(index)
        else:
            pass

       elif token.tag == 'INTJ':
        self.INTJ[0] += 1
        if index not in self.VERB_MAIN[1]:
            self.INTJ[1].append(index)

       elif token.tag == 'DET':
        self.DET[0] += 1
        if index not in self.VERB_MAIN[1]:
            self.DET[1].append(index)
        if token.sub_tag == 'DET_ARTICLE_DEFINITE':
            self.DET_ARTICLE_DEFINITE[0] += 1
            if index not in self.VERB_MAIN[1]:
                self.DET_ARTICLE_DEFINITE[1].append(index)
        elif token.sub_tag == 'DET_ARTICLE_INDEFINITE':
            self.DET_ARTICLE_INDEFINITE[0] += 1
            if index not in self.VERB_MAIN[1]:
                self.DET_ARTICLE_INDEFINITE[1].append(index)
        elif token.sub_tag == 'DET_POSSESSIVE':
            self.DET_POSSESSIVE[0] += 1
            if index not in self.VERB_MAIN[1]:
                self.DET_POSSESSIVE[1].append(index)
        elif token.sub_tag == 'DET_DEMONSTRATIVE':
            self.DET_DEMONSTRATIVE[0] += 1
            if index not in self.VERB_MAIN[1]:
                self.DET_DEMONSTRATIVE[1].append(index)
        elif token.sub_tag == 'DET_INDEFINITE':
            self.DET_INDEFINITE[0] += 1
            if index not in self.VERB_MAIN[1]:
                self.DET_INDEFINITE[1].append(index)
        elif token.sub_tag == 'DET_RELATIVE':
            self.DET_RELATIVE[0] += 1
            if index not in self.VERB_MAIN[1]:
                self.DET_RELATIVE[1].append(index)
        elif token.sub_tag == 'DET_INTERROGATIVE':
            self.DET_INTERROGATIVE[0] += 1
            if index not in self.VERB_MAIN[1]:
                self.DET_INTERROGATIVE[1].append(index)
        else:
            pass

       elif token.tag == 'PRON':
        self.PRON[0] += 1
        if index not in self.VERB_MAIN[1]:
            self.PRON[1].append(index)
        if token.sub_tag == 'PRON_POSSESSIVE':
            self.PRON_POSSESSIVE[0] += 1
            if index not in self.VERB_MAIN[1]:
                self.PRON_POSSESSIVE[1].append(index)
        elif token.sub_tag == 'PRON_DEMONSTRATIVE':
            self.PRON_DEMONSTRATIVE[0] += 1
            if index not in self.VERB_MAIN[1]:
                self.PRON_DEMONSTRATIVE[1].append(index)
        elif token.sub_tag == 'PRON_INDEFINITE':
            self.PRON_INDEFINITE[0] += 1
            if index not in self.VERB_MAIN[1]:
                self.PRON_INDEFINITE[1].append(index)
        elif token.sub_tag == 'PRON_RELATIVE':
            self.PRON_RELATIVE[0] += 1
            if index not in self.VERB_MAIN[1]:
                self.PRON_RELATIVE[1].append(index)
        elif token.sub_tag == 'PRON_INTERROGATIVE':
            self.PRON_INTERROGATIVE[0] += 1
            if index not in self.VERB_MAIN[1]:
                self.PRON_INTERROGATIVE[1].append(index)
        else:
            pass

       elif token.tag == 'ADV':
        self.ADV[0] += 1
        if index not in self.VERB_MAIN[1]:
            self.ADV[1].append(index)
        if token.sub_tag == 'ADV_MODE':
            self.ADV_MODE[0] += 1
            if index not in self.VERB_MAIN[1]:
                self.ADV_MODE[1].append(index)
        elif token.sub_tag == 'ADV_TIME':
            self.ADV_TIME[0] += 1
            if index not in self.VERB_MAIN[1]:
                self.ADV_TIME[1].append(index)
        elif token.sub_tag == 'ADV_LOCAL':
            self.ADV_LOCAL[0] += 1
            if index not in self.VERB_MAIN[1]:
                self.ADV_LOCAL[1].append(index)
        elif token.sub_tag == 'ADV_DEGREE':
            self.ADV_DEGREE[0] += 1
            if index not in self.VERB_MAIN[1]:
                self.ADV_DEGREE[1].append(index)
        elif token.sub_tag == 'ADV_AFFIRMATION':
            self.ADV_AFFIRMATION[0] += 1
            if index not in self.VERB_MAIN[1]:
                self.ADV_AFFIRMATION[1].append(index)
        elif token.sub_tag == 'ADV_NEGATION':
            self.ADV_NEGATION[0] += 1
            if index not in self.VERB_MAIN[1]:
                self.ADV_NEGATION[1].append(index)
        elif token.sub_tag == 'ADV_INCLUSION':
            self.ADV_INCLUSION[0] += 1
            if index not in self.VERB_MAIN[1]:
                self.ADV_INCLUSION[1].append(index)
        elif token.sub_tag == 'ADV_EXCLUSION':
            self.ADV_EXCLUSION[0] += 1
            if index not in self.VERB_MAIN[1]:
                self.ADV_EXCLUSION[1].append(index)
        elif token.sub_tag == 'ADV_DOUBT':
            self.ADV_DOUBT[0] += 1
            if index not in self.VERB_MAIN[1]:
                self.ADV_DOUBT[1].append(index)
        elif token.sub_tag == 'ADV_DESIGNATION':
            self.ADV_DESIGNATION[0] += 1
            if index not in self.VERB_MAIN[1]:
                self.ADV_DESIGNATION[1].append(index)
        elif token.sub_tag == 'ADV_INTERROGATIVE':
            self.ADV_INTERROGATIVE[0] += 1
            if index not in self.VERB_MAIN[1]:
                self.ADV_INTERROGATIVE[1].append(index)
        elif token.sub_tag == 'ADV_CONNECTIVE':
            self.ADV_CONNECTIVE[0] += 1
            if index not in self.VERB_MAIN[1]:
                self.ADV_CONNECTIVE[1].append(index)
        elif token.sub_tag == 'ADV_RELATIVE':
            self.ADV_RELATIVE[0] += 1
            if index not in self.VERB_MAIN[1]:
                self.ADV_RELATIVE[1].append(index)
        else:
            pass