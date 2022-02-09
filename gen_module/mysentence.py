import listsubtags
import myword
import mytoken
import mysentencestats

import os
import sys

sys.path.insert(0, 'utils')
import utils_algorithms

from nltk.tokenize import word_tokenize

class MySentence:
    def __init__(self):
        self.tokens = [] # done in 1st loop
        self.tagPtList = [] # done in 1st loop
        self.entities = [] # done in 1st loop
        self.stats = mysentencestats.MySentenceStats() # done in 1st loop

        self.tagSent = [] # done in ----> produceSentStruct
        self.subtagSent = [] # done in ----> produceSentStruct
        self.tagDep = [] # done in ----> produceSentStruct
        self.tagPt = '' # done in ----> produceSentStruct
        self.sentText = '' # done in ----> produceSentStruct

        self.difficulty = 0

        #Frequency of words with more than 3 syllables
        #MAIN VERBS
        # AUX VERBS - 0
        #nr of adverbs - 0.17
        # nr of coord - 0.18
        #NUMERALS - 0.31
        #self.DIFFERENT_DEPENDENCIES = {'qty': 0, 'indexes': []} - 0.60
        #self.DIFFERENT_TOKENS = {'qty': 0, 'indexes': []} - 0.61
        #nr of words - extension - 0.67 

    def performSimplification(self):
        return 1

    def checkIfDeclarative(self):
        if self.stats.PUNCT_FINAL['qty'] == 1 and self.stats.PUNCT_COMMA['qty'] >= 0 and self.stats.PUNCT_PARENTHESES['qty'] >= 0 and self.stats.PUNCT_QUESTION['qty'] == 0 and self.stats.PUNCT_EXCLAMATIVE['qty'] == 0 and self.stats.PUNCT_DASH['qty'] == 0 and self.stats.PUNCT_TWOPOINTS['qty'] == 0 and self.stats.PUNCT_SEMICOLON['qty'] == 0 and self.stats.PUNCT_QUOTATION['qty'] == 0:
            return 1
        else:
            return -1
    
    def calculateDifficulty(self):
        NR_WORDS = len(self.tokens)

        if NR_WORDS >= 25: # sentence is too long
            norm_NRWORDS_25 = 1
        else:
            norm_NRWORDS_25 = NR_WORDS / 25

        WEIGHT_NRWORDS = norm_NRWORDS_25 * ((0.67/6)*2.364)
        WEIGHT_DIFFERENT_TOKENS = ( self.stats.DIFFERENT_TOKENS['qty'] / NR_WORDS ) * ((0.61/6)*2.364)
        WEIGHT_DIFFERENT_DEPENDENCIES = ( self.stats.DIFFERENT_DEPENDENCIES['qty'] / 37 ) * ((0.60/6)*2.364)
        WEIGHT_NUMERALS = ( self.stats.NUM['qty'] / NR_WORDS ) * ((0.31/6)*2.364)
        WEIGHT_CONJS = ( self.stats.CONJ['qty'] / NR_WORDS )  * ((0.18/6)*2.364)
        WEIGHT_ADVS = ( self.stats.ADV['qty'] / NR_WORDS )  * ((0.17/6)*2.364)

        self.difficulty = WEIGHT_NRWORDS + WEIGHT_DIFFERENT_TOKENS + WEIGHT_DIFFERENT_DEPENDENCIES + WEIGHT_NUMERALS + WEIGHT_CONJS + WEIGHT_ADVS

    def addToken(self, token):
        self.tokens.append(token)

    def addAlltokens(self, allTokens):
        self.tokens = allTokens

    def getTokensLen(self):
        return len(self.tokens)

    def getTagsSeq(self):
        return self.tagSent

    def getTagsPt(self):
        return self.tagPt

    def getSentText(self):
        return self.sentText

    def produceSentStruct(self):
        for token in self.tokens:
            self.tagSent.append(token.tag) #English PoS list
            self.subtagSent.append(token.sub_tag) #English Subtag Pos list
            self.tagDep.append(token.dep) #English Dep list
            
            if self.tagPt == '':
                self.tagPt = str(token.pt_text['class']) #Portuguese PoS Text
            elif self.tagPt != '' and str(token.pt_text['class']) != "ponto" :
                self.tagPt = self.tagPt + '-' + str(token.pt_text['class']) #Portuguese PoS Text

            if token.text == ',' or token.text == '.' or token.text == "%":
                self.sentText = self.sentText + token.text
            else:
                self.sentText = self.sentText + ' ' + token.text # Portuguese Original Sentence
            #self.tagPtList.append(token.text) # Portuguese Original Token List # done in 1st loop
            #self.stats.addStats(token, index)
        self.sentText = self.sentText.lstrip(' ')