import sys
import argparse
import os

import mytoken
import myword
import mysentence
import mytextstats
import mysentencestats
import utils_algorithms

import stanfordnlp
from stanfordnlp.utils.resources import DEFAULT_MODEL_DIR

import concurrent.futures
import config

currentDirectory = os.getcwd()

models_dir = currentDirectory + '/gen_module/utils/models'
lang = 'pt'
cpu = 'False'

# download the models
stanfordnlp.download('pt', models_dir, confirm_if_exists=False)

# Stanford NER
from nltk.tag import StanfordNERTagger

if os.name == 'nt':
    java_path = config.JAVA_PATH
    os.environ['JAVAHOME'] = java_path

stanford_classifier = currentDirectory + '/gen_module/utils/stanford-ner/classifiers/portugueseHarem.ser.gz'
stanford_ner_path = currentDirectory + '/gen_module/utils/stanford-ner/stanford-ner.jar'
st = StanfordNERTagger(stanford_classifier, stanford_ner_path, encoding='utf-8')

def foo(all_sents_tagPtList):
    st = StanfordNERTagger(stanford_classifier, stanford_ner_path, encoding='utf-8')
    classified_text = st.tag_sents(all_sents_tagPtList)
    return classified_text

def buildStruct(content):
    textStruct = []
    #textStats = mytextstats.MyTextStats()

    # set up a pipeline
    print('Building pipeline...')
    pipeline = stanfordnlp.Pipeline(models_dir=models_dir, lang='pt', use_gpu=(not cpu))

    try:
        doc = pipeline(content)
    except:
        return -1,-1

    all_sents_tagPtList = []

    total_words = 0
    total_syllables = 0

    if len(doc.sentences) < 1:
        return -1,-1

    # save to textStruct
    for sent in doc.sentences:

        sent_tagPtList = []
        sent_depEngList = []
        
        new_sentence = mysentence.MySentence()
        sentenceStats = mysentencestats.MySentenceStats()

        for idx, token in enumerate(sent.tokens):

            sent_tagPtList.append(token.text)
            sent_depEngList.append(token.words[0].dependency_relation)

            new_token = mytoken.MyToken('NEW', token.text, token.index, token.words, sent.tokens)
            new_sentence.addToken(new_token)
            sentenceStats.addStats(sent_tagPtList, sent_depEngList, new_token, idx)
            result_syllables = calcSyllables(token.text)
            total_syllables = total_syllables + result_syllables
        
        total_words = total_words + len(sent.tokens)

        all_sents_tagPtList.append(sent_tagPtList)

        new_sentence.tagPtList = sent_tagPtList
        new_sentence.stats = sentenceStats
        new_sentence.calculateDifficulty()
        textStruct.append(new_sentence)
    
    textStruct = produceNER(all_sents_tagPtList, textStruct)
    
    stats = {'total_words': total_words, 'total_syllables': total_syllables}

    return stats, textStruct

"https://stackoverflow.com/questions/46759492/syllable-count-in-python"
def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiouy"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("e"):
        count -= 1
    if count == 0:
        count += 1
    return count

def calcSyllables(token_text):
    syllables_count = syllable_count(token_text)
 
    if syllables_count < 0: # does not happen
        return 0
    elif syllables_count == 0: # does not happen
        return 1
    elif syllables_count == 1:  # happens with symbols
        return 1
    elif syllables_count == 2:  # happens with symbols
        return 1
    elif syllables_count > 2:
        return syllables_count - 1

def produceNER(all_sents_tagPtList, textStruct):
    #classified_text = st.tag(self.tagPtList) # [('D.', 'PESSOA'), ('Afonso', 'PESSOA'), ('Henriques', 'PESSOA'), ('foi', 'O'), ('o', 'O'), ('primeiro', 'O'), ('rei', 'O'), ('de', 'O'), ('Portugal', 'LOCAL'), ('e', 'O'), ('a', 'O'), ('Maria', 'PESSOA'), ('é', 'O'), ('minha', 'O'), ('amiga', 'O'), ('.', 'O')]

    #print(all_sents_tagPtList)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(foo, all_sents_tagPtList)
        all_sents_classified_text = future.result()

    #all_sents_classified_text = st.tag_sents(all_sents_tagPtList)  # [('D.', 'PESSOA'), ('Afonso', 'PESSOA'), ('Henriques', 'PESSOA'), ('foi', 'O'), ('o', 'O'), ('primeiro', 'O'), ('rei', 'O'), ('de', 'O'), ('Portugal', 'LOCAL'), ('e', 'O'), ('a', 'O'), ('Maria', 'PESSOA'), ('é', 'O'), ('minha', 'O'), ('amiga', 'O'), ('.', 'O')]

    for sent_idx, classified_text in enumerate(all_sents_classified_text):

        entities_list = [item[1] for item in classified_text] # ['PESSOA', 'PESSOA', 'PESSOA', 'O', 'O', 'O', 'O', 'O', 'LOCAL', 'O', 'O', 'PESSOA', 'O', 'O', 'O', 'O']

        groups_entities = utils_algorithms.list_duplicates(entities_list, 0) 
        groups_entities = list(filter(lambda a: a[0] != 'O', groups_entities)) # [('PESSOA', [0, 1, 2, 11]), ('LOCAL', [8])]

        for ents in groups_entities:  # [{'entity_type': 'PERSON', 'tokens_idx': [0, 1, 2]}, {'entity_type': 'PERSON', 'tokens_idx': [11]}, {'entity_type': 'LOCAL', 'tokens_idx': [8]}]
            entity_type = ''
            if ents[0] == 'ABSTRACAO':
                entity_type = 'ABSTRACTION'
            elif ents[0] == 'ACONTECIMENTO':
                entity_type = 'EVENT'
            elif ents[0] == 'COISA':
                entity_type = 'OBJECT'
            elif ents[0] == 'LOCAL':
                entity_type = 'LOCAL'
            elif ents[0] == 'OBRA':
                entity_type = 'WORK_ART'
            elif ents[0] == 'ORGANIZACAO':
                entity_type = 'ORGANIZATION'
            elif ents[0] == 'PESSOA':
                entity_type = 'PERSON'
            elif ents[0] == 'TEMPO':
                entity_type = 'TIME'
            elif ents[0] == 'VALOR':
                entity_type = 'VALUE'
            elif ents[0] == 'OUTRO':
                entity_type = 'OTHER'
            elif ents[0] == 'ABSTRACCAO':
                entity_type = 'ABSTRACTION'
            else:
                entity_type = 'NONE'
            consecutive_ents = utils_algorithms.group_consecutives(ents[1])
            for ent in consecutive_ents:
                entity_text = getEntityText(ent, sent_idx, textStruct)
                new_entity = {'entity_type': entity_type, 'entity_text': entity_text, 'tokens_idx': ent}
                #self.entities.append(new_entity)
                textStruct[sent_idx].entities.append(new_entity)

    return textStruct

def getEntityText(ent, sent_idx, textStruct):
    return " ".join(textStruct[sent_idx].tagPtList[ ent[0]: ent[-1]+1])