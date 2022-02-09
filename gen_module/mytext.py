# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, 'utils')
#import nltk_tools
import stanfordnlp_tools

class MyText:
  def __init__(self, file_name, text="none"):
    self.file_name = file_name

    if text == 'none':
      self.readFile(file_name)
    else:
      self.readText(text)

  content = None
  textStruct = None

  flesh_readingease = 100
  total_words = 0
  total_syllables = 0

  def readFile(self, file_name):
    f = open(file_name, "r", encoding="utf-8")
    self.content = f.read()

  def readText(self, text):
    self.content = text

  def preProcess(self):
    stats, self.textStruct = stanfordnlp_tools.buildStruct(self.content)

    if self.textStruct == -1:
      return -1

    self.total_words = stats['total_words']
    self.total_syllables = stats['total_syllables']
    self.flesh_readingease = self.calculateFleschReadingEase()
    self.produceSentStruct()
    #self.printTextPos()

  def getFileName(self):
    return self.file_name

  def getSentsSize(self):
    sents_size = []
    for sent in self.textStruct:
      sents_size.append(len(sent.tokens))
    return sents_size
  
  def produceSentStruct(self):
    for sent in self.textStruct:
      sent.produceSentStruct()
    
  def printTextPos(self):
    for i, sent in enumerate(self.textStruct):
      print("Sent nr ", i, ": ")
      for mytoken in sent.tokens:
        print("<",mytoken.getPtText(),"> ", mytoken.getTag(), mytoken.text)
      print("\n")

  def calculateFleschReadingEase(self):
    #print(self.total_words, len(self.textStruct), self.total_syllables, self.total_words)
    flesch_readingease = 248.835 - 1.015 * float(self.total_words / len(self.textStruct)) - 84.6 * float(self.total_syllables / self.total_words)
    flesch_normalized = flesch_readingease / 100
    flesch_converted  = 1 - flesch_normalized
    return flesch_converted
      

