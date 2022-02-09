import json

class MyWord:
  def __init__(self, index, text, lemma, feats, upos, xpos, gov, dep):
    self.index = index
    self.text = text
    self.lemma = lemma
    self.feats = self.convertStrToJson(feats)
    self.upos = upos
    self.xpos = upos
    self.governor = gov
    self.dependency_relation = dep

  def getIndex(self):
      return self.index

  def getText(self):
      return self.text

  def getLemma(self):
      return self.lemma

  def getFeats(self, feats):
      return self.feats

  def getUpos(self):
      return self.upos

  def getXpos(self):
      return self.xpos

  def getDep(self):
      return self.dependency_relation
    
  def convertStrToJson(self, mystring):
      if mystring != '_':
        replace_1 = mystring.replace("|", " ")
        replace_2 = replace_1.replace("=", " ")
        replace_final = replace_2.split(" ")
        i = len(replace_final)
        new_string = ''
        comma = ''
        for index, r in enumerate(replace_final):
            if index != 0:
                comma = ', '
            if i >= 0 and ((index % 2) == 0 or index == 0):
                new_string = new_string + comma + '"{}"'.format(r) + " : " + '"{}"'.format(replace_final[index+1])
                i = i - 2
        new_string = '{'+ new_string + '}'
        return json.loads(new_string) 
      else:
          return json.loads('{}')
     