import nlpnet
import os 

current_path = os.path.dirname(os.path.realpath(__file__))
tagger = nlpnet.SRLTagger(current_path+'/nlpnet/srl-pt')

def srl_dict(sentence):
    sent = tagger.tag(sentence)[0]
    if len(sent.arg_structures) > 0:
        labeldict = sent.arg_structures[0][1]
        return labeldict
    else:
        return -1
        
def srl_list(sentence):
    sent = tagger.tag(sentence)[0]
    if len(sent.arg_structures) > 0:
        labelList = list(sent.arg_structures[0][1].items())
        return labelList
    else:
        return -1

def srl_items(sentence):
    sent = tagger.tag(sentence)[0]
    items = sent.arg_structures[0][1].items()
    return items

