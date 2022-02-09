import listsubtags
import json
import ast 
import myword

class MyToken:
  def __init__(self, token_type, text, index="none", words="none", tokens_orig="none"):
    self.token_type = token_type
    self.text = text
    self.index = index
    if token_type != 'GEN':
      self.words = self.convertToWords(words)
      self.tokens_orig = tokens_orig
      self.defineTags()

  tag = ''
  sub_tag = ''
  dep = ''
  pt_text = {'class': None, 'subclass': None}

  def getIndex(self):
      return self.index

  def getText(self):
      return self.text

  def getWords(self):
      return self.words

  def getTag(self):
    return self.tag

  def getPtText(self):
      return self.pt_text

  def convertToWords(self, words):
    my_words=[]
    for word in words:
      my_words.append(myword.MyWord(word.index, word.text, word.lemma, word.feats, word.upos, word.xpos, word.governor, word.dependency_relation))
    return my_words

  def defineTags(self):
    if len(self.words) == 1:
      self.assignTags_1word(self.words[0])
      self.dep = self.words[0].dependency_relation
    elif len(self.words) > 1:
      self.assignTags_words(self.words[0])
      self.dep = self.words[0].dependency_relation
    else:
      return -1

  def assignTags_words(self, word):
    if word.upos == 'ADP':
      self.tag = 'PREP'
      self.sub_tag = 'PREP_CONTRACTED'
      self.pt_text = {'class': 'preposição', 'subclass': 'preposição contraída'}
    else:
      self.assignTags_1word(self.words[0])

  def assignTags_1word(self, word):
    last_element = self.tokens_orig[-1].words[0].text
    if word.upos == 'ADJ':
      self.tag = 'ADJ'
      self.sub_tag, self.pt_text = listsubtags.whichADJ(word)
    elif word.upos == 'ADV':
      self.tag = 'ADV'
      self.sub_tag, self.pt_text = listsubtags.whichADV(word)
    elif word.upos == 'INTJ':
      self.tag = 'INTJ'
      self.sub_tag, self.pt_text = listsubtags.whichINTJ(word)
    elif word.upos == 'NOUN':
      self.tag = 'NOUN'
      self.sub_tag, self.pt_text = listsubtags.whichNOUN(word)
    elif word.upos == 'PROPN':
      self.tag = 'NOUN'
      self.sub_tag = 'NOUN_PROPER'
      self.pt_text = {'class': 'nome', 'subclass': 'nome próprio'}
    elif word.upos == 'VERB':
      self.tag = 'VERB'
      self.sub_tag, self.pt_text= listsubtags.whichVERB(word)
    elif word.upos == 'AUX':
      self.tag = 'VERB'
      self.sub_tag, self.pt_text = listsubtags.whichAUX(word)
    elif word.upos == 'ADP':
      self.tag = 'PREP'
      self.sub_tag, self.pt_text = listsubtags.whichPREP(word)
    elif word.upos == 'CCONJ':
      self.tag = 'CONJ'
      self.sub_tag, self.pt_text= listsubtags.whichCCONJ(word)
    elif word.upos == 'SCONJ':
      self.tag = 'CONJ'
      self.sub_tag, self.pt_text = listsubtags.whichSCONJ(word)
    elif word.upos == 'NUM':
      self.tag = 'NUM'
      self.sub_tag = 'NUM'
      self.pt_text = {'class': 'número', 'subclass': 'número'}
    elif word.upos == 'PART':
      self.tag = 'PART'
      self.sub_tag = 'PART'
    elif word.upos == 'PRON':
      self.tag = 'PRON'
      self.sub_tag, self.pt_text = listsubtags.whichPRON(word, last_element)
    elif word.upos == 'DET':
      self.tag = 'DET'
      self.sub_tag, self.pt_text = listsubtags.whichDET(word)
    elif word.upos == 'PUNCT':
      self.tag = 'PUNCT'
      self.sub_tag, self.pt_text = listsubtags.whichPUNCT(word)
    elif word.upos == 'SYM':
      self.tag = 'SYM'
      self.sub_tag, self.pt_text = listsubtags.whichSYM(word)
    elif word.upos == 'X':
      self.tag = 'X'
      self.sub_tag = 'X'
    else:
      return -1