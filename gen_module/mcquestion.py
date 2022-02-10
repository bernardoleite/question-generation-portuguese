import random

class McQuestion:
  def __init__(self, mc_uuid, question_type, key_uuid, stat_text, mc_options, diff, gui_sent="none", gui_quest="none"):
    self.mc_uuid = mc_uuid
    self.type = "mc_choice"
    self.mc_type = question_type
    self.key_uuid = key_uuid
    self.stat_text = stat_text
    self.mc_options = mc_options
    self.gui_sent = gui_sent
    self.gui_quest = gui_quest
    self.diff = diff

  def myfunc(self):
    print("This is a question.")

  def getMcUuid(self):
    return self.mc_uuid

  def getMcType(self):
    return self.mc_type

  def getKeyUuid(self):
    return self.key_uuid

  def getStatText(self):
    return self.stat_text

  def getMcOptions(self):
    return self.mc_options

  def getMcDiff(self):
    return self.diff

  def printMc(self):
    print(self.stat_text)
    for mc_option in self.mc_options:
      print(mc_option['text'])

  def getQuestion(self):
    question_string = "\n Questão: " + "\n" + self.stat_text
    for mc_option in self.mc_options:
      question_string = question_string + "\n" + mc_option["text"]
    question_string = question_string + "\n"
    question_string = question_string + "\n" + "Dificuldade: " + str(self.diff) + "\n" + "Tipo de questão: " + str(self.mc_type) + "\n"
    return question_string
