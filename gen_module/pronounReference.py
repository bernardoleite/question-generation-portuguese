import sys
sys.path.insert(0, 'utils')
import utils_algorithms
import uuid
import random
import copy
import mytoken
import mcquestion

NR_WRONG_CHOICES = 3

BLOOMS_REMEMBER_LEVEL = 0.2
BLOOMS_UNDERSTAND_LEVEL = 0.4
BLOOMS_ANALYSE_LEVEL = 0.6

WEIGHT_BLOOM = 1/3
WEIGHT_TEXT = 1/3
WEIGHT_SENTENCE = 1/3

def getAppositives(sent):
    retrieve_appositives = utils_algorithms.match_indexes(sent.tagPtList, [',','que'], [','])
    if len(retrieve_appositives) >= 1:
        unique_appositives = []
        for appositive in retrieve_appositives:
            appositive_exists = False
            for unique_appositive in unique_appositives:
                if appositive[0] == unique_appositive[0]:
                    appositive_exists = True
            if appositive_exists == False:
                unique_appositives.append(appositive)
            else:
                pass
        return utils_algorithms.merge_sublists(unique_appositives)
    else:
        return []

def getRefPronoun(reference):
    pronoun = 'NONE'

    if reference['feats']['Gender'] == 'Masc' and reference['feats']['Number'] == 'Sing':
        pronoun = 'Aquele' 
    elif reference['feats']['Gender'] == 'Masc' and reference['feats']['Number'] == 'Plur':
        pronoun = 'Aqueles' 
    elif reference['feats']['Gender'] == 'Fem' and reference['feats']['Number'] == 'Sing':
        pronoun = 'Aquela' 
    elif reference['feats']['Gender'] == 'Fem' and reference['feats']['Number'] == 'Plur':
        pronoun = 'Aquelas' 

    return pronoun

def producePronRefQuestions(sent, idx_sent, appositive, my_text):
    if idx_sent-1 <= len(my_text.textStruct) and idx_sent-1 >= 0:
        pre_sent = my_text.textStruct[idx_sent-1]
    if idx_sent+1 <= len(my_text.textStruct) and idx_sent+1 >= 0:
        post_sent = my_text.textStruct[idx_sent+1]

    is_pre_decl = pre_sent.checkIfDeclarative()
    is_post_decl = post_sent.checkIfDeclarative()
    reference = findAppositiveReference(sent, appositive)

    if reference != -1 and is_pre_decl == 1 and is_post_decl == 1 and len(pre_sent.tagSent) >= 3 and len(post_sent.tagSent) >= 3:
        #sent.tokens[appositive[-1]+1].tag != 'CONJ' and sent.tokens[appositive[-1]+1].tag != 'DET'
        
        pronoun_subst = getRefPronoun(reference)

        dists_pre = findDistractors(pre_sent, reference)
        dists_sent = findDistractors(sent, reference)
        dists_post = findDistractors(post_sent, reference)

        dists_case1 = getDistractorsPerCase(copy.deepcopy(dists_sent), appositive, 1)
        dists_case2 = getDistractorsPerCase(copy.deepcopy(dists_sent), appositive, 2)

        number_dists_case1 = len(dists_pre) + len(dists_case1) + len(dists_post)
        number_dists_case2 = len(dists_pre) + len(dists_case2) + len(dists_post)

        reading_passage = None

        question = None
        passage_difficulty = (pre_sent.difficulty + sent.difficulty + post_sent.difficulty)/3

        if number_dists_case1 >= NR_WRONG_CHOICES and number_dists_case1 >= number_dists_case2:
            reading_passage = genReadingPassageCase1(pre_sent, sent, post_sent, appositive, pronoun_subst)
            question = buildPronRefQuestion(reading_passage, passage_difficulty, my_text.flesh_readingease, dists_case1 + dists_pre + dists_post, reference, pronoun_subst)

        elif number_dists_case2 >= NR_WRONG_CHOICES and number_dists_case2 > number_dists_case1:
            reading_passage = genReadingPassageCase2(pre_sent, sent, post_sent, appositive, pronoun_subst)
            question = buildPronRefQuestion(reading_passage, passage_difficulty, my_text.flesh_readingease, dists_case2 + dists_pre + dists_post, reference,pronoun_subst)
        else:
            pass

        if question != None:
            return question

    else:
        return None

    return None

def buildPronRefQuestion(reading_passage, passage_difficulty, diff_text, distractors, reference, pronoun_subst):
    stat_question = "\n\n" + 'No excerto anterior, a palavra ' +  '"' + pronoun_subst + '"' + ' refere-se a:' + "\n"
    stat_text = reading_passage + stat_question

    key_uuid = uuid.uuid1()

    question_diff = WEIGHT_BLOOM * BLOOMS_ANALYSE_LEVEL + WEIGHT_SENTENCE * passage_difficulty + WEIGHT_TEXT * diff_text

    new_mc_question = mcquestion.McQuestion(
        uuid.uuid1(),
        'pronoun_reference', 
        key_uuid,
        stat_text, 
        [{'option_id': key_uuid, 'text':reference['text']}, {'option_id': uuid.uuid1(), 'text':distractors[0]['text']}, {'option_id': uuid.uuid1(), 'text':distractors[1]['text']}, {'option_id': uuid.uuid1(), 'text':distractors[2]['text']}], 
        question_diff,
        '"' + reading_passage + '"',
        stat_question
        )

    return new_mc_question

def genReadingPassageCase1(pre_sent, sent, post_sent, appositive, pronoun_subst):
    reading_passage = None
    new_sent = copy.deepcopy(sent)

    if appositive[-1]+1 <= len(new_sent.tokens):
        new_sent_part1 = new_sent.tokens[0:appositive[-1]+1]
        new_sent_part2 = new_sent.tokens[appositive[-1]+1:]

        del new_sent_part1[appositive[-1]]
        del new_sent_part1[appositive[1]]
        del new_sent_part1[appositive[0]]
        new_sent_part1.append(mytoken.MyToken('GEN','.'))
        new_sent_part2.insert(0, mytoken.MyToken('GEN', pronoun_subst))

        newsent_part1_text = tokens2text(new_sent_part1)
        newsent_part2_text = tokens2text(new_sent_part2)

        reading_passage = pre_sent.sentText + "\n" + newsent_part1_text + "\n" + newsent_part2_text + "\n" + post_sent.sentText
    else:
        return None

    return reading_passage 

def genReadingPassageCase2(pre_sent, sent, post_sent, appositive, pronoun_subst):
    reading_passage = None
    new_sent = copy.deepcopy(sent)

    new_sent_part1 = new_sent.tokens[0:appositive[0]]
    new_sent_part1.extend(new_sent.tokens[appositive[-1]+1:])
    new_sent_part2 = new_sent.tokens[appositive[0]:appositive[-1]+1]

    del new_sent_part2[-1]
    del new_sent_part2[1]
    del new_sent_part2[0]
    new_sent_part2.append(mytoken.MyToken('GEN','.'))
    new_sent_part2.insert(0, mytoken.MyToken('GEN', pronoun_subst))

    newsent_part1_text = tokens2text(new_sent_part1)
    newsent_part2_text = tokens2text(new_sent_part2)

    reading_passage = pre_sent.sentText + "\n" + newsent_part1_text + "\n" + newsent_part2_text + "\n" + post_sent.sentText

    return reading_passage

def tokens2text(tokens):
    sentence = ''
    for token in tokens:
        if token.text == ',' or token.text == '.':
            sentence = sentence + token.text
        else:
            sentence = sentence + ' ' + token.text
    return sentence

def getDistractorsPerCase(dists_sent, appositive, case):

    for dist in dists_sent:
        if case == 1:
            if dist['token_idx'] <= appositive[-1]:
                pass
            else:
                dists_sent.remove(dist)
        elif case == 2:
            if dist['token_idx'] <= appositive[0] or dist['token_idx'] >= appositive[-1]:
                pass
            else:
                dists_sent.remove(dist)
    
    return dists_sent

def findDistractors(sent, reference):
    distractors = []

    for idx, token in enumerate(sent.tokens):
        if token.text not in reference['text'] and token.tag == 'NOUN':
            if 'Gender' in token.words[0].feats and 'Number' in token.words[0].feats:
                if token.words[0].feats['Gender'] == reference['feats']['Gender'] and token.words[0].feats['Number'] == reference['feats']['Number']:
                    if checkifExists(token, distractors) == True:
                        new_distractor = {'text': token.text, 'token_idx': idx}
                        distractors.append(new_distractor)

    return distractors

def checkifExists(elem, my_list):
    for e in my_list:
        if elem.text in e['text']:
            return False
    return True

def findAppositiveReference(sent, appositive):
    reference = {'text': None, 'tokens_idx': [], 'feats': None}

    for idx in appositive:
        token = sent.tokens[idx]
        if token.words[0].dependency_relation == 'acl:relcl':
            token_governor = str(token.words[0].governor)
            ref_idx, ref_feats, ref_text = findRefInfo(sent, token_governor, appositive)
            if len(ref_idx) > 0 and ref_feats != None and len(ref_text) > 0:
                reference['text'] = " ".join(ref_text)
                reference['tokens_idx'] = ref_idx
                reference['feats'] = ref_feats
                if 'Gender' in reference['feats'] and 'Number' in reference['feats']:
                    return reference
    return -1


def findRefInfo(sent, token_governor, appositive):
    ref_idx = []
    ref_feats = None
    ref_text = []

    for index, sent_token in enumerate(sent.tokens):
        if sent_token.index == token_governor and index <= appositive[0]-1 and sent_token.tag == 'NOUN':
            ref_idx.append(index)
            ref_text.append(sent_token.text)
            ref_feats = sent_token.words[0].feats
        if sent_token.index != token_governor and len(ref_idx) > 0 and index <= appositive[0]-1:
            ref_idx.append(index)
            ref_text.append(sent_token.text)
    
    return ref_idx, ref_feats, ref_text