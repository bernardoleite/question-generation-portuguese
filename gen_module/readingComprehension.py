import sys
sys.path.insert(0, 'utils')
import utils_algorithms
import uuid
import random
import mysentence
import copy
import factquestion
import verbs
import nlp_net
import mytoken
import itertools
from itertools import combinations 

BLOOMS_REMEMBER_LEVEL = 0.2
BLOOMS_UNDERSTAND_LEVEL = 0.4
BLOOMS_ANALYSE_LEVEL = 0.6

WEIGHT_BLOOM = 1/3
WEIGHT_TEXT = 1/3
WEIGHT_SENTENCE = 1/3

def produceSemanticQuestions(sent, my_text):

    all_questions = []
    questions_srl_tmp = []
    questions_srl_loc = []
    questions_srl_mnr = []

    labels = nlp_net.srl_list(sent.sentText)

    if labels == -1:
        return all_questions

    dup_tokens = copy.deepcopy(sent.tokens)
    diff_text = my_text.flesh_readingease

    if len(labels) >= 3:
        questions_srl_tmp = gen_srl_tmp(sent, diff_text, dup_tokens, copy.deepcopy(labels))
        questions_srl_loc = gen_srl_loc(sent, diff_text, dup_tokens, copy.deepcopy(labels))
        questions_srl_mnr = gen_srl_mnr(sent, diff_text, dup_tokens, copy.deepcopy(labels))
    
    all_questions = questions_srl_tmp + questions_srl_loc + questions_srl_mnr

    return all_questions

def gen_srl_mnr(sent, diff_text, dup_tokens, labels):
    questions = []

    #AM-MNR , A0, V,  A1
    #A1, A0, V, AM-MNR
    #A0, V, AM-MNR -> not done

    if len(labels) >= 4 and labels[0][0] == 'AM-MNR' and labels[1][0] == 'A0' and labels[2][0] == 'V' and labels[3][0] == 'A1':
        questions_srl_mnr = gen_srl_mnr_pattern1(sent, diff_text, dup_tokens, labels)
        questions.extend(questions_srl_mnr)
    if len(labels) >= 4 and labels[0][0] == 'A1' and labels[1][0] == 'A0' and labels[2][0] == 'V' and labels[3][0] == 'AM-MNR':
        questions_srl_mnr = gen_srl_mnr_pattern2(sent, diff_text, dup_tokens, labels)
        questions.extend(questions_srl_mnr)
    if len(labels) >= 4 and labels[0][0] == 'A0' and labels[1][0] == 'A1' and labels[2][0] == 'V' and labels[3][0] == 'AM-MNR':
        questions_srl_mnr = gen_srl_mnr_pattern3(sent, diff_text, dup_tokens, labels)
        questions.extend(questions_srl_mnr)
    if len(labels) >= 4 and labels[0][0] == 'A0' and labels[1][0] == 'V' and labels[2][0] == 'A1' and labels[3][0] == 'AM-MNR':
        questions_srl_mnr = gen_srl_mnr_pattern4(sent, diff_text, dup_tokens, labels)
        questions.extend(questions_srl_mnr)
    if len(labels) >= 3 and labels[0][0] == 'A0' and labels[1][0] == 'V' and labels[2][0] == 'AM-MNR':
        questions_srl_mnr = gen_srl_mnr_pattern5(sent, diff_text, dup_tokens, labels)
        questions.extend(questions_srl_mnr)

    return questions

def gen_srl_mnr_pattern1(sent, diff_text, dup_tokens, labels):
    questions = []

    new_labels = get_srl_newlabels(sent, dup_tokens, labels)

    if new_labels != -1:
            question_tokens = []
            question_tokens.extend([mytoken.MyToken('GEN','Como'), mytoken.MyToken('GEN','é'), mytoken.MyToken('GEN','que')])
            question_tokens.extend(new_labels[1][2])
            question_tokens.extend(new_labels[2][2])
            question_tokens.extend(new_labels[3][2])
            question_tokens.append(mytoken.MyToken('GEN','?'))

            question_diff = WEIGHT_BLOOM * BLOOMS_UNDERSTAND_LEVEL + WEIGHT_SENTENCE * sent.difficulty + WEIGHT_TEXT * diff_text

            new_question = factquestion.FactQuestion(uuid.uuid1(), 'sem', 'sem_how', sent.sentText, question_tokens, " ".join(new_labels[0][1]), question_diff)
            questions.append(new_question)
 
    return questions

def gen_srl_mnr_pattern2(sent, diff_text, dup_tokens, labels):
    questions = []

    new_labels = get_srl_newlabels(sent, dup_tokens, labels)

    if new_labels != -1:
            question_tokens = []
            question_tokens.extend([mytoken.MyToken('GEN','Como'), mytoken.MyToken('GEN','é'), mytoken.MyToken('GEN','que')])
            question_tokens.extend(new_labels[1][2])
            question_tokens.extend(new_labels[0][2])
            question_tokens.extend(new_labels[2][2])
            question_tokens.append(mytoken.MyToken('GEN','?'))

            question_diff = WEIGHT_BLOOM * BLOOMS_UNDERSTAND_LEVEL + WEIGHT_SENTENCE * sent.difficulty + WEIGHT_TEXT * diff_text

            new_question = factquestion.FactQuestion(uuid.uuid1(), 'sem', 'sem_how', sent.sentText, question_tokens, " ".join(new_labels[3][1]), question_diff)
            questions.append(new_question)
 
    return questions

def gen_srl_mnr_pattern3(sent, diff_text, dup_tokens, labels):
    questions = []

    new_labels = get_srl_newlabels(sent, dup_tokens, labels)

    if new_labels != -1:
            question_tokens = []
            question_tokens.extend([mytoken.MyToken('GEN','Como'), mytoken.MyToken('GEN','é'), mytoken.MyToken('GEN','que')])
            question_tokens.extend(new_labels[0][2])
            question_tokens.extend(new_labels[1][2])
            question_tokens.extend(new_labels[2][2])
            question_tokens.append(mytoken.MyToken('GEN','?'))

            question_diff = WEIGHT_BLOOM * BLOOMS_UNDERSTAND_LEVEL + WEIGHT_SENTENCE * sent.difficulty + WEIGHT_TEXT * diff_text

            new_question = factquestion.FactQuestion(uuid.uuid1(), 'sem', 'sem_how', sent.sentText, question_tokens, " ".join(new_labels[3][1]), question_diff)
            questions.append(new_question)
 
    return questions

def gen_srl_mnr_pattern4(sent, diff_text, dup_tokens, labels):
    questions = []

    new_labels = get_srl_newlabels(sent, dup_tokens, labels)

    if new_labels != -1:
            question_tokens = []
            question_tokens.extend([mytoken.MyToken('GEN','Como'), mytoken.MyToken('GEN','é'), mytoken.MyToken('GEN','que')])
            question_tokens.extend(new_labels[0][2])
            question_tokens.extend(new_labels[1][2])
            question_tokens.extend(new_labels[2][2])
            question_tokens.append(mytoken.MyToken('GEN','?'))

            question_diff = WEIGHT_BLOOM * BLOOMS_UNDERSTAND_LEVEL + WEIGHT_SENTENCE * sent.difficulty + WEIGHT_TEXT * diff_text

            new_question = factquestion.FactQuestion(uuid.uuid1(), 'sem', 'sem_how', sent.sentText, question_tokens, " ".join(new_labels[3][1]), question_diff)
            questions.append(new_question)
 
    return questions

def gen_srl_mnr_pattern5(sent, diff_text, dup_tokens, labels):
    questions = []

    new_labels = get_srl_newlabels(sent, dup_tokens, labels)

    if new_labels != -1:
            question_tokens = []
            question_tokens.extend([mytoken.MyToken('GEN','Como'), mytoken.MyToken('GEN','é'), mytoken.MyToken('GEN','que')])
            question_tokens.extend(new_labels[0][2])
            question_tokens.extend(new_labels[1][2])
            question_tokens.append(mytoken.MyToken('GEN','?'))

            question_diff = WEIGHT_BLOOM * BLOOMS_UNDERSTAND_LEVEL + WEIGHT_SENTENCE * sent.difficulty + WEIGHT_TEXT * diff_text

            new_question = factquestion.FactQuestion(uuid.uuid1(), 'sem', 'sem_how', sent.sentText, question_tokens, " ".join(new_labels[2][1]), question_diff)
            questions.append(new_question)
 
    return questions

def gen_srl_loc(sent, diff_text, dup_tokens, labels):
    questions = []
    if labels[0][0] == 'A0' and labels[1][0] == 'V' and labels[2][0] == 'AM-LOC':
        questions_srl_loc = gen_srl_loc_pattern1(sent, diff_text, dup_tokens, labels)
        questions.extend(questions_srl_loc)
    if len(labels) >= 4 and labels[0][0] == 'A0' and labels[1][0] == 'V' and labels[2][0] == 'A1' and labels[3][0] == 'AM-LOC':
        questions_srl_loc = gen_srl_loc_pattern2(sent, diff_text, dup_tokens, labels)
        questions.extend(questions_srl_loc)
    if labels[0][0] == 'AM-LOC' and labels[1][0] == 'V' and labels[2][0] == 'A1':
        questions_srl_loc = gen_srl_loc_pattern3(sent, diff_text, dup_tokens, labels)
        questions.extend(questions_srl_loc)

    return questions

def gen_srl_loc_pattern1(sent, diff_text, dup_tokens, labels):
    questions = []

    new_labels = get_srl_newlabels(sent, dup_tokens, labels)

    if new_labels != -1:
            question_tokens = []
            question_tokens.extend([mytoken.MyToken('GEN','Onde'), mytoken.MyToken('GEN','é'), mytoken.MyToken('GEN','que')])
            question_tokens.extend(new_labels[0][2])
            question_tokens.extend(new_labels[1][2])
            question_tokens.append(mytoken.MyToken('GEN','?'))

            question_diff = WEIGHT_BLOOM * BLOOMS_UNDERSTAND_LEVEL + WEIGHT_SENTENCE * sent.difficulty + WEIGHT_TEXT * diff_text

            new_question = factquestion.FactQuestion(uuid.uuid1(), 'sem', 'sem_where', sent.sentText, question_tokens, " ".join(new_labels[2][1]), question_diff)
            questions.append(new_question)
 
    return questions

def gen_srl_loc_pattern2(sent, diff_text, dup_tokens, labels):
    questions = []

    new_labels = get_srl_newlabels(sent, dup_tokens, labels)

    if new_labels != -1:
            question_tokens = []
            question_tokens.extend([mytoken.MyToken('GEN','Onde'), mytoken.MyToken('GEN','é'), mytoken.MyToken('GEN','que')])
            question_tokens.extend(new_labels[0][2])
            question_tokens.extend(new_labels[1][2])
            question_tokens.extend(new_labels[2][2])
            question_tokens.append(mytoken.MyToken('GEN','?'))

            question_diff = WEIGHT_BLOOM * BLOOMS_UNDERSTAND_LEVEL + WEIGHT_SENTENCE * sent.difficulty + WEIGHT_TEXT * diff_text

            new_question = factquestion.FactQuestion(uuid.uuid1(), 'sem', 'sem_where', sent.sentText, question_tokens, " ".join(new_labels[3][1]), question_diff)
            questions.append(new_question)
 
    return questions

def gen_srl_loc_pattern3(sent, diff_text, dup_tokens, labels):
    questions = []

    new_labels = get_srl_newlabels(sent, dup_tokens, labels)

    if new_labels != -1:
            question_tokens = []
            question_tokens.extend([mytoken.MyToken('GEN','Onde'), mytoken.MyToken('GEN','é'), mytoken.MyToken('GEN','que')])
            question_tokens.extend(new_labels[1][2])
            question_tokens.extend(new_labels[2][2])
            question_tokens.append(mytoken.MyToken('GEN','?'))

            question_diff = WEIGHT_BLOOM * BLOOMS_UNDERSTAND_LEVEL + WEIGHT_SENTENCE * sent.difficulty + WEIGHT_TEXT * diff_text

            new_question = factquestion.FactQuestion(uuid.uuid1(), 'sem', 'sem_where', sent.sentText, question_tokens, " ".join(new_labels[0][1]), question_diff)
            questions.append(new_question)
 
    return questions

def gen_srl_tmp(sent, diff_text, dup_tokens, labels):
    questions = []

    if labels[0][0] == 'A0' and labels[1][0] == 'V' and labels[2][0] == 'AM-TMP':
        questions_srl_tmp = gen_srl_tmp_pattern1(sent, diff_text, dup_tokens, labels)
        questions.extend(questions_srl_tmp)
    if len(labels) >= 4 and labels[0][0] == 'A0' and labels[1][0] == 'V' and labels[2][0] == 'A1' and labels[3][0] == 'AM-TMP':
        questions_srl_tmp = gen_srl_tmp_pattern2(sent, diff_text, dup_tokens, labels)
        questions.extend(questions_srl_tmp)
    if len(labels) >= 4 and labels[0][0] == 'AM-TMP' and labels[1][0] == 'A0' and labels[2][0] == 'V' and labels[3][0] == 'A1':
        questions_srl_tmp = gen_srl_tmp_pattern3(sent, diff_text, dup_tokens, labels)
        questions.extend(questions_srl_tmp)
    if len(labels) >= 4 and labels[0][0] == 'AM-TMP' and labels[1][0] == 'A0' and labels[2][0] == 'AM-NEG' and labels[3][0] == 'V':
        questions_srl_tmp = gen_srl_tmp_pattern4(sent, diff_text, dup_tokens, labels)
        questions.extend(questions_srl_tmp)

    return questions


def gen_srl_tmp_pattern4(sent, diff_text, dup_tokens, labels):
    questions = []

    new_labels = get_srl_newlabels(sent, dup_tokens, labels)

    if new_labels != -1:
            question_tokens = []
            question_tokens.extend([mytoken.MyToken('GEN','Quando'), mytoken.MyToken('GEN','é'), mytoken.MyToken('GEN','que')])
            question_tokens.extend(new_labels[1][2])
            question_tokens.extend(new_labels[2][2])
            question_tokens.extend(new_labels[3][2])
            question_tokens.append(mytoken.MyToken('GEN','?'))

            question_diff = WEIGHT_BLOOM * BLOOMS_UNDERSTAND_LEVEL + WEIGHT_SENTENCE * sent.difficulty + WEIGHT_TEXT * diff_text

            new_question = factquestion.FactQuestion(uuid.uuid1(), 'sem', 'sem_when', sent.sentText, question_tokens, " ".join(new_labels[0][1]), question_diff)
            questions.append(new_question)
 
    return questions

def gen_srl_tmp_pattern3(sent, diff_text, dup_tokens, labels):
    questions = []

    new_labels = get_srl_newlabels(sent, dup_tokens, labels)

    if new_labels != -1:
            question_tokens = []
            question_tokens.extend([mytoken.MyToken('GEN','Quando'), mytoken.MyToken('GEN','é'), mytoken.MyToken('GEN','que')])
            question_tokens.extend(new_labels[1][2])
            question_tokens.extend(new_labels[2][2])
            question_tokens.extend(new_labels[3][2])
            question_tokens.append(mytoken.MyToken('GEN','?'))

            question_diff = WEIGHT_BLOOM * BLOOMS_UNDERSTAND_LEVEL + WEIGHT_SENTENCE * sent.difficulty + WEIGHT_TEXT * diff_text

            new_question = factquestion.FactQuestion(uuid.uuid1(), 'sem', 'sem_when', sent.sentText, question_tokens, " ".join(new_labels[0][1]), question_diff)
            questions.append(new_question)
 
    return questions

def gen_srl_tmp_pattern2(sent, diff_text, dup_tokens, labels):
    questions = []

    new_labels = get_srl_newlabels(sent, dup_tokens, labels)

    if new_labels != -1:
            question_tokens = []
            question_tokens.extend([mytoken.MyToken('GEN','Quando'), mytoken.MyToken('GEN','é'), mytoken.MyToken('GEN','que')])
            question_tokens.extend(new_labels[0][2])
            question_tokens.extend(new_labels[1][2])
            question_tokens.extend(new_labels[2][2])
            question_tokens.append(mytoken.MyToken('GEN','?'))

            question_diff = WEIGHT_BLOOM * BLOOMS_UNDERSTAND_LEVEL + WEIGHT_SENTENCE * sent.difficulty + WEIGHT_TEXT * diff_text

            new_question = factquestion.FactQuestion(uuid.uuid1(), 'sem', 'sem_when', sent.sentText, question_tokens, " ".join(new_labels[3][1]), question_diff)
            questions.append(new_question)
 
    return questions

def gen_srl_tmp_pattern1(sent, diff_text, dup_tokens, labels):
    questions = []

    new_labels = get_srl_newlabels(sent, dup_tokens, labels)

    if new_labels != -1:
            question_tokens = []
            question_tokens.extend([mytoken.MyToken('GEN','Quando'), mytoken.MyToken('GEN','é'), mytoken.MyToken('GEN','que')])
            question_tokens.extend(new_labels[0][2])
            question_tokens.extend(new_labels[1][2])
            question_tokens.append(mytoken.MyToken('GEN','?'))

            question_diff = WEIGHT_BLOOM * BLOOMS_UNDERSTAND_LEVEL + WEIGHT_SENTENCE * sent.difficulty + WEIGHT_TEXT * diff_text

            new_question = factquestion.FactQuestion(uuid.uuid1(), 'sem', 'sem_when', sent.sentText, question_tokens, " ".join(new_labels[2][1]), question_diff)
            questions.append(new_question)
 
    return questions

def get_srl_tokens_fromindex(dup_tokens, find_tokens):
    token_list = []
    for index in find_tokens:
        token_list.append(dup_tokens[index[1]])
    return token_list

def get_srl_newlabels(sent, dup_tokens, labels):
    for idx, label in enumerate(labels):
        find_tokens = utils_algorithms.find_matching_index(sent.tagPtList, label[1])
        if len(find_tokens) > 0:
            token_list = get_srl_tokens_fromindex(dup_tokens, find_tokens)
            labels[idx] = label + (token_list,)
        else:
            return -1
    return labels

def produceSyntaxQuestions(sent, my_text):
    if len(sent.entities) > 0:
        diff_text = my_text.flesh_readingease
        ir_ner_pos, new_subtagSent, new_tagPtList, new_tokens = produceIrNerPos(sent)
        questions_per = gen_ner_per(sent, diff_text, ir_ner_pos, new_tagPtList, new_tokens)
        questions_loc = gen_ner_loc(sent, diff_text, ir_ner_pos, new_tagPtList, new_tokens)
        questions_org = gen_ner_org(sent, diff_text, ir_ner_pos, new_tagPtList, new_tokens)
        questions_event = gen_ner_event(sent, diff_text, ir_ner_pos, new_tagPtList, new_tokens)
        questions_time = gen_ner_time(sent, diff_text, ir_ner_pos, new_tagPtList, new_tokens)
        questions_value = gen_ner_value(sent, diff_text, ir_ner_pos, new_tagPtList, new_tokens)
        questions_object = gen_ner_object(sent, diff_text, ir_ner_pos, new_tagPtList, new_tokens)

        all_questions = questions_per + questions_loc + questions_org + questions_event + questions_time + questions_value + questions_object

        return all_questions
    else: 
        return []

def producePronounQuestions(sent, my_text):
    if sent.stats.PRON_RELATIVE['qty'] > 0 or sent.stats.ADV_RELATIVE['qty'] > 0:

        dup_tokens = copy.deepcopy(sent.tokens)

        diff_text = my_text.flesh_readingease

        questions_pron_1 = gen_pron_pattern1(sent, diff_text, dup_tokens)
        questions_pron_2 = gen_pron_pattern2(sent, diff_text, dup_tokens)
        questions_pron_3 = gen_pron_pattern3(sent, diff_text, dup_tokens)
        
        all_questions = questions_pron_1 + questions_pron_2 + questions_pron_3

        return all_questions
    else:
        return []

def produceDependencyQuestions(sent, my_text):
    questions_dep_dobj = []
    questions_dep_iobj = []
    questions_dep_cop = []
    questions_dep_xcomp = []
    questions_dep_amod = []

    dup_tokens = copy.deepcopy(sent.tokens)

    diff_text = my_text.flesh_readingease

    if 'obj' in sent.tagDep:
        questions_dep_dobj = gen_dep_dobj(sent, diff_text, dup_tokens)
    if 'obj' in sent.tagDep and 'case' in sent.tagDep and 'obl' in sent.tagDep:
        questions_dep_iobj = gen_dep_iobj(sent, diff_text, dup_tokens)
    if sent.stats.VERB_COPULATIVE['qty'] >= 0 and sent.stats.ADJ['qty'] >= 0:
        questions_dep_cop = gen_dep_cop(sent, diff_text, dup_tokens)
    if 'xcomp' in sent.tagDep and 'nsubj' in sent.tagDep:
        questions_dep_xcomp = gen_dep_xcomp(sent, diff_text, dup_tokens)
    if 'amod' in sent.tagDep and 'nsubj' in sent.tagDep:
        questions_dep_amod = gen_dep_amod(sent, diff_text, dup_tokens)

    all_questions = questions_dep_dobj + questions_dep_iobj + questions_dep_cop + questions_dep_xcomp + questions_dep_amod

    return all_questions

def produceConnectorsQuestions(sent, my_text):
    questions_why = []
    questions_when = []

    dup_tokens = copy.deepcopy(sent.tokens)
    diff_text = my_text.flesh_readingease

    if 'porque' in sent.tagPtList or 'pois' in sent.tagPtList:
        questions_why = gen_con_why(sent, diff_text, dup_tokens)
    if 'quando' in sent.tagPtList:
        questions_when = gen_con_when(sent, diff_text, dup_tokens)

    all_questions = questions_why + questions_when

    return all_questions

def gen_con_why(sent, diff_text, dup_tokens):
    questions_con_why = []
    pattern_match1 = utils_algorithms.match_indexes(sent.tagSent, ['PUNCT', 'CONJ'], ['PUNCT'])

    if len(pattern_match1) > 0:
        pattern_match1 = remove_longer_matches(pattern_match1)
        for match in pattern_match1:
            questions_con_why = gen_con_pattern1(sent, diff_text, dup_tokens, 'why', match, questions_con_why)
    else:
        pass

    return questions_con_why

def gen_con_when(sent, diff_text, dup_tokens):
    questions_con_when = []
    pattern_match1 = utils_algorithms.match_indexes(sent.tagSent, ['PUNCT', 'ADV'], ['PUNCT'])

    if len(pattern_match1) > 0:
        pattern_match1 = remove_longer_matches(pattern_match1)
        for match in pattern_match1:
            questions_con_when = gen_con_pattern1(sent, diff_text, dup_tokens, 'when', match, questions_con_when)
    else:
        pass

    return questions_con_when

def gen_con_pattern1(sent, diff_text, dup_tokens, connector, match, questions_con_why):
    if connector == 'why':
        has_connectors = ( (sent.tagPtList[match[1]] == 'porque' and 'porque' not in sent.tagPtList[0:match[0]]) or (sent.tagPtList[match[1]] == 'pois' and 'pois' not in sent.tagPtList[0:match[0]]))
        tagSent = 'CONJ'
        subtagSent = 'SCONJ_CAUSAL'
    elif connector == 'when':
        has_connectors = (sent.tagPtList[match[1]] == 'quando' and 'quando' not in sent.tagPtList[0:match[0]])
        tagSent = 'ADV'
        subtagSent = 'ADV_INTERROGATIVE'

    if len(match) >= 4 and sent.subtagSent[match[1]] == subtagSent and has_connectors:
        if 'PUNCT' in sent.tagSent[0:match[0]-1]:
            pattern_match2 = utils_algorithms.match_indexes(sent.tagSent, ['PUNCT'], ['PUNCT', tagSent])
            pattern_match2 = remove_longer_matches(pattern_match2)
            if len(pattern_match2) > 0:
                for match2 in pattern_match2:
                    if len(match2) >= 5 and match[0] == match2[-2] and 'PUNCT' not in sent.tagSent[match2[1]:match2[-2]]:
                        new_question = build_question_pattern1(diff_text, connector, sent, dup_tokens, 1, match, match2)
                        if new_question != -1: questions_con_why.append(new_question)
        else:
            new_question = build_question_pattern1(diff_text, connector, sent, dup_tokens, 2, match)
            if new_question != -1: questions_con_why.append(new_question)
    return questions_con_why

def build_question_pattern1(diff_text, connector, sent, dup_tokens, case, match, match2=[]):
    questions_tokens = []

    if connector == 'why':
        questions_tokens.extend([mytoken.MyToken('GEN','Qual'), mytoken.MyToken('GEN','o'), mytoken.MyToken('GEN','motivo'), mytoken.MyToken('GEN','pelo'), mytoken.MyToken('GEN','qual')])
    elif connector == 'when':
        questions_tokens.extend([mytoken.MyToken('GEN','Quando'), mytoken.MyToken('GEN','é'), mytoken.MyToken('GEN','que')])

    if case == 1:
        idx_chosen = get_firstIdx_match(sent, match2[1], match2[-2])
        if idx_chosen != -1: questions_tokens.extend(dup_tokens[idx_chosen:match2[-2]])
        else: return -1
    elif case == 2:
        idx_chosen = get_firstIdx_match(sent, 0, match[0])
        if idx_chosen != -1: questions_tokens.extend(dup_tokens[idx_chosen:match[0]]) 
        else: return -1
    else:
        return -1
    questions_tokens.append(mytoken.MyToken('GEN','?'))
    
    question_diff = WEIGHT_BLOOM * BLOOMS_UNDERSTAND_LEVEL + WEIGHT_SENTENCE * sent.difficulty + WEIGHT_TEXT * diff_text

    fact_subtype = 'connectors_?'
    if connector == 'why':
        fact_subtype = 'connectors_why'
    elif connector == 'when':
        fact_subtype = 'connectors_when'

    new_question = factquestion.FactQuestion(uuid.uuid1(), 'connectors', fact_subtype, sent.sentText, questions_tokens, " ".join(sent.tagPtList[match[1]:match[-1]]), question_diff)
    return new_question

def get_firstIdx_match(sent, start_idx, end_idx):
    idx_chosen = start_idx
    for idx, tag in enumerate(sent.tagSent):
        if idx >= start_idx and idx <= end_idx:
            if tag == 'VERB' or tag == 'DET': 
                idx_chosen = idx
                return idx_chosen
    return -1

def gen_con_although(sent, my_text, dup_tokens):
    questions_con_although = []
    return questions_con_although

def gen_dep_dobj(sent, diff_text, dup_tokens):
    questions_dep_dobj = []
    pattern_match1 = utils_algorithms.match_indexes(sent.tagDep, ['det','nsubj','root','det','obj'], ['punct'])

    if len(pattern_match1) > 0:
        pattern_match1 = remove_longer_matches(pattern_match1)
        for match in pattern_match1:
            questions_tokens = []
            questions_tokens.extend([mytoken.MyToken('GEN','O'), mytoken.MyToken('GEN','que'), mytoken.MyToken('GEN','é'), mytoken.MyToken('GEN','que')])
            questions_tokens.extend(dup_tokens[match[0]:match[3]])
            questions_tokens.append(mytoken.MyToken('GEN','?'))

            question_diff = WEIGHT_BLOOM * BLOOMS_UNDERSTAND_LEVEL + WEIGHT_SENTENCE * sent.difficulty + WEIGHT_TEXT * diff_text

            new_question = factquestion.FactQuestion(uuid.uuid1(), 'dep', 'dep_facts', sent.sentText, questions_tokens, " ".join(sent.tagPtList[match[3]:match[5]]), question_diff)
            questions_dep_dobj.append(new_question)

    return questions_dep_dobj

def gen_dep_iobj(sent, diff_text, dup_tokens):
    questions_dep_iobj = []
    pattern_match2 = utils_algorithms.match_indexes(sent.tagDep, ['nsubj','root','det','obj','case','obl'], ['punct'])

    if len(pattern_match2) > 0:
        pattern_match2 = remove_longer_matches(pattern_match2)
        for match in pattern_match2:
            if len(sent.tokens[match[4]].words) == 2 and sent.tokens[match[4]].words[1].dependency_relation == 'det':
                pass
                #print(sent.sentText, match, "\n")

    return questions_dep_iobj

def gen_dep_cop(sent, diff_text, dup_tokens):
    questions_dep_cop = []

    pattern_match0 = utils_algorithms.match_indexes(sent.tagDep, ['det','det','nsubj','cop','root'], ['punct'])
    pattern_match1 = utils_algorithms.match_indexes(sent.tagDep, ['det','nsubj','cop','root'], ['punct'])
    pattern_match2 = utils_algorithms.match_indexes(sent.tagDep, ['det','nsubj','cop','advmod','root'], ['punct'])
    pattern_match3 = utils_algorithms.match_indexes(sent.tagDep, ['det','nsubj','case','nmod','cop','root'], ['punct'])

    #Como caracteriza a honestidade de Hans?
    #A honestidade de Hans era célebre e a sua palavra era de oiro.

    if len(pattern_match0) > 0:
        pattern_match0 = remove_longer_matches(pattern_match0)
        for match in pattern_match0:
            if sent.tagSent[match[4]] == 'ADJ':
                questions_tokens = []
                questions_tokens.extend([mytoken.MyToken('GEN','Como'), mytoken.MyToken('GEN','caracteriza')])
                questions_tokens.extend(dup_tokens[match[0]:match[3]])
                questions_tokens.append(mytoken.MyToken('GEN','?'))

                question_diff = WEIGHT_BLOOM * BLOOMS_UNDERSTAND_LEVEL + WEIGHT_SENTENCE * sent.difficulty + WEIGHT_TEXT * diff_text

                new_question = factquestion.FactQuestion(uuid.uuid1(), 'dep', 'dep_how', sent.sentText, questions_tokens, sent.tagPtList[match[3]], question_diff)
                questions_dep_cop.append(new_question)

    if len(pattern_match1) > 0 and len(pattern_match0) == 0:
        pattern_match1 = remove_longer_matches(pattern_match1)
        for match in pattern_match1:
            if sent.tagSent[match[3]] == 'ADJ':
                questions_tokens = []
                questions_tokens.extend([mytoken.MyToken('GEN','Como'), mytoken.MyToken('GEN','caracteriza')])
                questions_tokens.extend(dup_tokens[match[0]:match[2]])
                questions_tokens.append(mytoken.MyToken('GEN','?'))

                question_diff = WEIGHT_BLOOM * BLOOMS_UNDERSTAND_LEVEL + WEIGHT_SENTENCE * sent.difficulty + WEIGHT_TEXT * diff_text

                new_question = factquestion.FactQuestion(uuid.uuid1(), 'dep', 'dep_how', sent.sentText, questions_tokens, sent.tagPtList[match[3]], question_diff)
                questions_dep_cop.append(new_question)

    if len(pattern_match2) > 0:
        pattern_match2 = remove_longer_matches(pattern_match2)
        for match in pattern_match2:
            if sent.tagSent[match[4]] == 'ADJ':
                questions_tokens = []
                questions_tokens.extend([mytoken.MyToken('GEN','Como'), mytoken.MyToken('GEN','caracteriza')])
                questions_tokens.extend(dup_tokens[match[0]:match[2]])
                questions_tokens.append(mytoken.MyToken('GEN','?'))

                question_diff = WEIGHT_BLOOM * BLOOMS_UNDERSTAND_LEVEL + WEIGHT_SENTENCE * sent.difficulty + WEIGHT_TEXT * diff_text

                new_question = factquestion.FactQuestion(uuid.uuid1(), 'dep', 'dep_how', sent.sentText, questions_tokens, " ".join(sent.tagPtList[match[3]:match[5]]), question_diff)
                questions_dep_cop.append(new_question)

    if len(pattern_match3) > 0:
        pattern_match3 = remove_longer_matches(pattern_match3)
        for match in pattern_match3:
            if sent.tagSent[match[5]] == 'ADJ':
                questions_tokens = []
                questions_tokens.extend([mytoken.MyToken('GEN','Como'), mytoken.MyToken('GEN','caracteriza')])
                questions_tokens.extend(dup_tokens[match[0]:match[4]])
                questions_tokens.append(mytoken.MyToken('GEN','?'))

                question_diff = WEIGHT_BLOOM * BLOOMS_UNDERSTAND_LEVEL + WEIGHT_SENTENCE * sent.difficulty + WEIGHT_TEXT * diff_text

                new_question = factquestion.FactQuestion(uuid.uuid1(), 'dep', 'dep_how', sent.sentText, questions_tokens, sent.tagPtList[match[5]], question_diff)
                questions_dep_cop.append(new_question)
    
    return questions_dep_cop

    #Modificador do adjetivo
    #Ela anda muito cansada.
    #Ela salta mais alto

    #Modificador do nome
    #Ele é um homem bonito

def gen_dep_xcomp(sent, diff_text, dup_tokens):
    questions_dep_xcomp = []

    pattern_match0 = utils_algorithms.match_indexes(sent.tagDep, ['det','det','nsubj'], ['root','xcomp'])
    pattern_match1 = utils_algorithms.match_indexes(sent.tagDep, ['det','nsubj'], ['root','xcomp'])
    pattern_match2 = utils_algorithms.match_indexes(sent.tagDep, ['det','nsubj'], ['root','advmod','xcomp'])

    if len(pattern_match0) > 0:
        pattern_match0 = remove_longer_matches(pattern_match0)
        for match in pattern_match0:
            if 'punct' not in sent.tagDep[match[0]:match[-1]] and sent.tagSent[match[-2]] == 'VERB' and sent.tagSent[match[-1]] == 'ADJ':
                questions_tokens = []
                questions_tokens.extend([mytoken.MyToken('GEN','Como'), mytoken.MyToken('GEN','é'), mytoken.MyToken('GEN','que')])
                questions_tokens.append(dup_tokens[match[-2]])
                questions_tokens.extend(dup_tokens[match[0]:match[3]])
                questions_tokens.append(mytoken.MyToken('GEN','?'))

                question_diff = WEIGHT_BLOOM * BLOOMS_UNDERSTAND_LEVEL + WEIGHT_SENTENCE * sent.difficulty + WEIGHT_TEXT * diff_text

                new_question = factquestion.FactQuestion(uuid.uuid1(), 'dep', 'dep_how', sent.sentText, questions_tokens, sent.tagPtList[match[-1]], question_diff)
                questions_dep_xcomp.append(new_question)

    if len(pattern_match1) > 0 and len(pattern_match0) == 0:
        pattern_match1 = remove_longer_matches(pattern_match1)
        for match in pattern_match1:
            if 'punct' not in sent.tagDep[match[0]:match[-1]] and sent.tagSent[match[-2]] == 'VERB' and sent.tagSent[match[-1]] == 'ADJ':
                questions_tokens = []
                questions_tokens.extend([mytoken.MyToken('GEN','Como'), mytoken.MyToken('GEN','é'), mytoken.MyToken('GEN','que')])
                questions_tokens.append(dup_tokens[match[-2]])
                questions_tokens.extend(dup_tokens[match[0]:match[2]])
                questions_tokens.append(mytoken.MyToken('GEN','?'))

                question_diff = WEIGHT_BLOOM * BLOOMS_UNDERSTAND_LEVEL + WEIGHT_SENTENCE * sent.difficulty + WEIGHT_TEXT * diff_text

                new_question = factquestion.FactQuestion(uuid.uuid1(), 'dep', 'dep_how', sent.sentText, questions_tokens, sent.tagPtList[match[-1]], question_diff)
                questions_dep_xcomp.append(new_question)

    if len(pattern_match2) > 0:
        pattern_match2 = remove_longer_matches(pattern_match2)
        for match in pattern_match2:
            if 'punct' not in sent.tagDep[match[0]:match[-2]] and sent.tagSent[match[-3]] == 'VERB' and sent.tagSent[match[-2]] == 'ADV' and sent.tagSent[match[-1]] == 'ADJ':
                questions_tokens = []
                questions_tokens.extend([mytoken.MyToken('GEN','Como'), mytoken.MyToken('GEN','é'), mytoken.MyToken('GEN','que')])
                questions_tokens.append(dup_tokens[match[-3]])
                questions_tokens.extend(dup_tokens[match[0]:match[2]])
                questions_tokens.append(mytoken.MyToken('GEN','?'))

                question_diff = WEIGHT_BLOOM * BLOOMS_UNDERSTAND_LEVEL + WEIGHT_SENTENCE * sent.difficulty + WEIGHT_TEXT * diff_text

                new_question = factquestion.FactQuestion(uuid.uuid1(), 'dep', 'dep_how', sent.sentText, questions_tokens, " ".join(sent.tagPtList[match[-2]:match[-1]+1]), question_diff)
                questions_dep_xcomp.append(new_question)

    return questions_dep_xcomp

def gen_dep_amod(sent, diff_text, dup_tokens):
    questions_dep_amod = []

    pattern_match1 = utils_algorithms.match_indexes(sent.tagDep, ['nsubj'], ['root','amod'])

    if len(pattern_match1) > 0:
        pattern_match1 = remove_longer_matches(pattern_match1)
        for match in pattern_match1:
            if 'punct' not in sent.tagDep[match[0]:match[-1]] and sent.tagSent[match[-2]] == 'NOUN':
                pass
                #print(sent.sentText, match, "\n")

    return questions_dep_amod

def whichTerm(sent, noun):
    for ent in sent.entities:
        if noun in ent['entity_text'] and ent['entity_type'] == 'PERSON':
            return [mytoken.MyToken('GEN','Quem')]
        elif noun in ent['entity_text'] and ent['entity_type'] == 'LOCAL':
            return [mytoken.MyToken('GEN','Onde'), mytoken.MyToken('GEN','é'), mytoken.MyToken('GEN','que')]
        elif noun in ent['entity_text'] and ent['entity_type'] == 'EVENT':
            return [mytoken.MyToken('GEN','Que'), mytoken.MyToken('GEN','acontecimento')]
        elif noun in ent['entity_text'] and ent['entity_type'] == 'TIME':
            return [mytoken.MyToken('GEN','Quando'), mytoken.MyToken('GEN','é'), mytoken.MyToken('GEN','que')]
    return [mytoken.MyToken('GEN','O'), mytoken.MyToken('GEN','que'), mytoken.MyToken('GEN','é'), mytoken.MyToken('GEN','que')]


def whichSubType(questions_tokens):
    if questions_tokens[0].text == 'Quando':
        return 'relative_pronoun_when'
    elif questions_tokens[0].text == 'Onde':
        return 'relative_pronoun_where'
    else:
        return 'relative_pronoun_facts'
    return 'relative_pronoun_facts'

#E as apóstrofes que o velho dirige ao seu contendor
#O episódio é o do passarito que vem pousar na linha de pesca , e ao qual o velho fala carinhosamente por achá-lo jovem e inerme . {'qty': 2, 'indexes': [6, 16]}
def gen_pron_pattern1(sent, diff_text, dup_tokens):

    questions_pron = []
    pattern_match1 = utils_algorithms.match_indexes(sent.tagSent, ['NOUN','PRON'], ['PUNCT'])

    if len(pattern_match1) > 0:
        pattern_match1 = remove_longer_matches(pattern_match1)
        for match in pattern_match1:
            if sent.subtagSent[match[1]] == 'PRON_RELATIVE' and sent.tagPtList[match[1]] == 'que': 
                if sent.tokens[match[1]].words[0].dependency_relation == 'nsubj' or sent.tokens[match[1]].words[0].dependency_relation == 'obj': ## last added to match new case
                    for token in sent.tokens[match[1]:]:
                            if token.words[0].dependency_relation == 'acl:relcl' and str(token.words[0].governor) == sent.tokens[match[0]].index:
                                
                                begin_term = whichTerm(sent, sent.tagPtList[match[0]])

                                questions_tokens = []
                                questions_tokens.extend(begin_term)
                                questions_tokens.extend(dup_tokens[match[2]:match[-1]])
                                questions_tokens.append(mytoken.MyToken('GEN','?'))

                                question_diff = WEIGHT_BLOOM * BLOOMS_REMEMBER_LEVEL + WEIGHT_SENTENCE * sent.difficulty + WEIGHT_TEXT * diff_text

                                fact_subtype = whichSubType(questions_tokens)

                                new_question = factquestion.FactQuestion(uuid.uuid1(), 'relative_pronoun', fact_subtype, sent.sentText, questions_tokens, sent.tagPtList[match[0]], question_diff)
                                questions_pron.append(new_question)

                                if sent.subtagSent[match[2]] == 'VERB_COPULATIVE' or sent.subtagSent[match[2]] == 'VERB_AUXILIARY':
                                    before_noun_idx = match[0]-1
                                    if before_noun_idx >= 0 and sent.tagDep[before_noun_idx] == 'det':

                                        questions_tokens = []
                                        questions_tokens.append(mytoken.MyToken('GEN','Como'))
                                        questions_tokens.append(dup_tokens[match[2]])
                                        questions_tokens.extend(dup_tokens[before_noun_idx:match[1]])
                                        questions_tokens.append(mytoken.MyToken('GEN','?'))

                                        question_diff = WEIGHT_BLOOM * BLOOMS_UNDERSTAND_LEVEL + WEIGHT_SENTENCE * sent.difficulty + WEIGHT_TEXT * diff_text

                                        new_question = factquestion.FactQuestion(uuid.uuid1(), 'relative_pronoun', 'relative_pronoun_how', sent.sentText, questions_tokens, " ".join(sent.tagPtList[match[2]:match[-1]]), question_diff)
                                        questions_pron.append(new_question)
                                    
    return questions_pron

def gen_pron_pattern2(sent, diff_text, dup_tokens):
    questions_pron = []
    pattern_match2 = utils_algorithms.match_indexes(sent.tagSent, ['NOUN','ADV'], ['PUNCT'])

    if len(pattern_match2) > 0:
        pattern_match2 = remove_longer_matches(pattern_match2)
        for match in pattern_match2:
            if sent.subtagSent[match[1]] == 'ADV_RELATIVE' and sent.tagPtList[match[1]] == 'onde':
                if sent.tokens[match[1]].words[0].dependency_relation == 'advmod':
                    for token in sent.tokens[match[1]:]:
                            if token.words[0].dependency_relation == 'acl:relcl' and str(token.words[0].governor) == sent.tokens[match[0]].index:

                                questions_tokens = []
                                questions_tokens.extend([mytoken.MyToken('GEN','Onde'), mytoken.MyToken('GEN','é'), mytoken.MyToken('GEN','que')])
                                questions_tokens.extend(dup_tokens[match[2]:match[-1]])
                                questions_tokens.append(mytoken.MyToken('GEN','?'))

                                question_diff = WEIGHT_BLOOM * BLOOMS_REMEMBER_LEVEL + WEIGHT_SENTENCE * sent.difficulty + WEIGHT_TEXT * diff_text

                                new_question = factquestion.FactQuestion(uuid.uuid1(), 'relative_pronoun', 'relative_pronoun_where', sent.sentText, questions_tokens, sent.tagPtList[match[0]], question_diff)
                                questions_pron.append(new_question)
    
    return questions_pron

def gen_pron_pattern3(sent, diff_text, dup_tokens):
    questions_pron = []
    pattern_match3 = utils_algorithms.match_indexes(sent.tagSent, ['NOUN','PUNCT','ADV'], ['PUNCT'])

    if len(pattern_match3) > 0:
        pattern_match3 = remove_longer_matches(pattern_match3)
        for match in pattern_match3:
            if sent.subtagSent[match[2]] == 'ADV_RELATIVE' and sent.tagPtList[match[2]] == 'onde':
                if sent.tokens[match[2]].words[0].dependency_relation == 'advmod':
                    for token in sent.tokens[match[2]:]:
                            if token.words[0].dependency_relation == 'acl:relcl' and str(token.words[0].governor) == sent.tokens[match[0]].index:

                                questions_tokens = []
                                questions_tokens.extend([mytoken.MyToken('GEN','Onde'), mytoken.MyToken('GEN','é'), mytoken.MyToken('GEN','que')])
                                questions_tokens.extend(dup_tokens[match[3]:match[-1]])
                                questions_tokens.append(mytoken.MyToken('GEN','?'))

                                question_diff = WEIGHT_BLOOM * BLOOMS_REMEMBER_LEVEL + WEIGHT_SENTENCE * sent.difficulty + WEIGHT_TEXT * diff_text

                                new_question = factquestion.FactQuestion(uuid.uuid1(), 'relative_pronoun', 'relative_pronoun_where', sent.sentText, questions_tokens, sent.tagPtList[match[0]], question_diff)
                                questions_pron.append(new_question)
    return questions_pron

def produceIrNerPos(sent): # produce intermediate representation between Ner and PoS
    ir_ner_pos = sent.tagSent.copy()
    new_subtagSent = sent.subtagSent.copy()
    new_tagPtList = sent.tagPtList.copy()
    new_tokens = sent.tokens.copy()

    sent.entities.sort(key = lambda x: x['tokens_idx'][0], reverse = True)

    for my_ent in sent.entities:
        ent = my_ent['tokens_idx']
        if len(ent) > 1:
            ir_ner_pos[ent[0]:ent[-1]+1] = [''.join(ir_ner_pos[ent[0]:ent[-1]+1])]
            new_subtagSent[ent[0]:ent[-1]+1] = ['|'.join(new_subtagSent[ent[0]:ent[-1]+1])]
            new_tagPtList[ent[0]:ent[-1]+1] = [' '.join(new_tagPtList[ent[0]:ent[-1]+1])]
            del new_tokens[ent[1]:ent[-1]+1] 
        ir_ner_pos[ent[0]] = my_ent['entity_type']

    return ir_ner_pos, new_subtagSent, new_tagPtList, new_tokens

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

def getInicialConj(sent):
    if sent.tagSent[0] == 'CONJ':
        if len(sent.tagSent) > 1 and sent.tagPtList[1] == ',':
            return [0, 1]
        else:
            return [0]
    else:
        return []

def simplifySent(sent):
    appositives_indexes = getAppositives(sent) # careful, function has changed
    initial_conj_indexes = getInicialConj(sent)
    tokens_indexes_todelete = list(dict.fromkeys(appositives_indexes + initial_conj_indexes)) # remove duplicates from list

    if len(tokens_indexes_todelete) > 0:
        new_sentence = mysentence.MySentence()
        new_sentence.addAlltokens(sent.tokens.copy())

        for index in sorted(tokens_indexes_todelete, reverse=True):
            del new_sentence.tokens[index]

        new_sentence.produceSentStruct()
        new_sentence.entities = sent.entities
        return new_sentence
    else:
        return sent

def remove_longer_matches(patter_match): # issubset does not consider order, maybe change by KMP algorithm?, SEE https://stackoverflow.com/questions/425604/best-way-to-determine-if-a-sequence-is-in-another-sequence-in-python
    for comb in combinations(patter_match, 2): # remove duplicates
        if set(comb[0]).issubset(comb[1]) and comb[0][0] == comb[1][0]:
            if comb[1] in patter_match: patter_match.remove(comb[1])
        elif set(comb[1]).issubset(comb[0]) and comb[0][0] == comb[1][0]:
            if comb[0] in patter_match: patter_match.remove(comb[0])
        else:
            pass
    return patter_match

def gen_ner_per(original_sent, diff_text, ir_ner_pos, new_tagPtList, new_tokens):

    questions_per = []

    pattern_match1 = utils_algorithms.match_indexes(ir_ner_pos, ['PERSON','VERB'], ['PUNCT']) #active
    pattern_match2 = utils_algorithms.match_indexes(ir_ner_pos, ['PERSON','CONJ','DET','PERSON','VERB'], ['PUNCT']) # two people
    pattern_match3 = utils_algorithms.match_indexes(ir_ner_pos, ['PERSON','CONJ','PERSON','VERB'], ['PUNCT']) # two people

    #pattern_match4 = utils_algorithms.match_indexes(ir_ner_pos, ['VERB','VERB','PREP','PERSON'], ['PUNCT']) # passive (only 1 with canterville)

    if len(pattern_match1) > 0:
        pattern_match1 = remove_longer_matches(pattern_match1)
        for match in pattern_match1:
            questions_per = handle_pattern1(questions_per, match, [mytoken.MyToken('GEN','Quem')], original_sent, ir_ner_pos, diff_text, new_tagPtList, new_tokens, 1, new_tagPtList[match[0]])
    if len(pattern_match2) > 0:
        pattern_match2 = remove_longer_matches(pattern_match2)
        for match in pattern_match2:
            questions_per = handle_pattern1(questions_per, match, [mytoken.MyToken('GEN','Que'), mytoken.MyToken('GEN','pessoas')], original_sent, ir_ner_pos, diff_text, new_tagPtList, new_tokens, 4, " ".join(new_tagPtList[match[0]:match[4]]))
    if len(pattern_match3) > 0:
        pattern_match3 = remove_longer_matches(pattern_match3)
        for match in pattern_match3:
            questions_per = handle_pattern1(questions_per, match, [mytoken.MyToken('GEN','Que'), mytoken.MyToken('GEN','pessoas')], original_sent, ir_ner_pos, diff_text, new_tagPtList, new_tokens, 3, " ".join(new_tagPtList[match[0]:match[3]]))

    return questions_per

#pattern_match1 = re.findall("<LOC><VERB>.*?<PUNCT>", expression)
#pattern_match1 = re.findall("<DET><PER><VERB>.*?<ADP><LOC><PUNCT>", expression) # Per and Loc

def gen_ner_loc(original_sent, diff_text, ir_ner_pos, new_tagPtList, new_tokens):

    questions_loc = []

    pattern_match1 = utils_algorithms.match_indexes(ir_ner_pos, ['LOCAL','VERB'], ['PUNCT']) #active
    pattern_match2 = utils_algorithms.match_indexes(ir_ner_pos, ['PERSON','VERB'], ['PREP','LOCAL'])

    if len(pattern_match1) > 0:
        pattern_match1 = remove_longer_matches(pattern_match1)
        for match in pattern_match1:
            questions_loc = handle_pattern1(questions_loc, match, [mytoken.MyToken('GEN','Onde'), mytoken.MyToken('GEN','é'), mytoken.MyToken('GEN','que')], original_sent, ir_ner_pos, diff_text, new_tagPtList, new_tokens, 1, new_tagPtList[match[0]])
    if len(pattern_match2) > 0:
        pattern_match2 = remove_longer_matches(pattern_match2)
        for match in pattern_match2:
            if 'PUNCT' not in ir_ner_pos[match[0]:match[-1]]:

                questions_tokens = []
                questions_tokens.extend([mytoken.MyToken('GEN','Onde'), mytoken.MyToken('GEN','é'), mytoken.MyToken('GEN','que')])
                questions_tokens.extend(new_tokens[match[0]:match[-2]])
                questions_tokens.append(mytoken.MyToken('GEN','?'))

                question_diff = WEIGHT_BLOOM * BLOOMS_REMEMBER_LEVEL + WEIGHT_SENTENCE * original_sent.difficulty + WEIGHT_TEXT * diff_text
            
                new_question = factquestion.FactQuestion(uuid.uuid1(), 'syntax', 'syntax_where', original_sent.sentText, questions_tokens, new_tagPtList[match[-1]], question_diff)
                questions_loc.append(new_question)
    
    return questions_loc

def gen_ner_org(original_sent, diff_text, ir_ner_pos, new_tagPtList, new_tokens):

    questions_org = []

    pattern_match1 = utils_algorithms.match_indexes(ir_ner_pos, ['ORGANIZATION','VERB'], ['PUNCT']) #active
    #new_tagPtList = treatVerbs(new_tagPtList, new_tokens)

    if len(pattern_match1) > 0:
        pattern_match1 = remove_longer_matches(pattern_match1)
        for match in pattern_match1:
            questions_org = handle_pattern1(questions_org, match, [mytoken.MyToken('GEN','Que'), mytoken.MyToken('GEN','organização')], original_sent, ir_ner_pos, diff_text, new_tagPtList, new_tokens, 1, new_tagPtList[match[0]])
    
    return questions_org

def gen_ner_event(original_sent, diff_text, ir_ner_pos, new_tagPtList, new_tokens):

    questions_event = []

    pattern_match1 = utils_algorithms.match_indexes(ir_ner_pos, ['EVENT', 'VERB'], ['PUNCT']) #active

    if len(pattern_match1) > 0:
        pattern_match1 = remove_longer_matches(pattern_match1)
        for match in pattern_match1:
            questions_event = handle_pattern1(questions_event, match, [mytoken.MyToken('GEN','Que'), mytoken.MyToken('GEN','acontecimento')], original_sent, ir_ner_pos, diff_text, new_tagPtList, new_tokens, 1, new_tagPtList[match[0]])
    
    return questions_event

def gen_ner_time(original_sent, diff_text, ir_ner_pos, new_tagPtList, new_tokens):

    questions_time = []

    pattern_match1 = utils_algorithms.match_indexes(ir_ner_pos, ['TIME', 'VERB'], ['PUNCT']) #active

    if len(pattern_match1) > 0:
        pattern_match1 = remove_longer_matches(pattern_match1)
        for match in pattern_match1:
            if 'PUNCT' not in ir_ner_pos[match[0]:match[-2]]:

                questions_tokens = []
                questions_tokens.extend([mytoken.MyToken('GEN','Quando'), mytoken.MyToken('GEN','é'), mytoken.MyToken('GEN','que')])
                questions_tokens.extend(new_tokens[match[1]:match[-1]])
                questions_tokens.append(mytoken.MyToken('GEN','?'))

                question_diff = WEIGHT_BLOOM * BLOOMS_REMEMBER_LEVEL + WEIGHT_SENTENCE * original_sent.difficulty + WEIGHT_TEXT * diff_text

                new_question = factquestion.FactQuestion(uuid.uuid1(), 'syntax', 'syntax_when', original_sent.sentText, questions_tokens, new_tagPtList[match[0]], question_diff)
                questions_time.append(new_question)
    return questions_time

def gen_ner_value(original_sent, diff_text, ir_ner_pos, new_tagPtList, new_tokens):

    questions_value = []

    pattern_match1 = utils_algorithms.match_indexes(ir_ner_pos, ['VALUE','PREP'], ['PUNCT'])
    pattern_match2 = utils_algorithms.match_indexes(ir_ner_pos, ['VALUE','NOUN'], ['PUNCT'])

    unitsToCheck = ['unidade', 'unidades', 'dezena', 'dezenas', 'centena', 'centenas', 'milhar', 'mil', 'milhares', 'milhão', 'milhões']
    value_token = 'valor'

    if len(pattern_match1) > 0:
        pattern_match1 = remove_longer_matches(pattern_match1)
        for match in pattern_match1:
            if '%' in new_tagPtList[match[0]]:
                value_token = 'percentagem'
            if any(unit in new_tagPtList[match[0]] for unit in unitsToCheck):
                value_token = 'número'
            questions_value = handle_pattern1(questions_value, match,  [mytoken.MyToken('GEN','Que'), mytoken.MyToken('GEN', value_token)], original_sent, ir_ner_pos, diff_text, new_tagPtList, new_tokens, 1, new_tagPtList[match[0]])

    if len(pattern_match2) > 0:
        pattern_match2 = remove_longer_matches(pattern_match2)
        for match in pattern_match2:
            if '%' in new_tagPtList[match[0]]:
                value_token = 'percentagem'
            if any(unit in new_tagPtList[match[0]] for unit in unitsToCheck):
                value_token = 'número'
            questions_value = handle_pattern1(questions_value, match,  [mytoken.MyToken('GEN','Que'), mytoken.MyToken('GEN', value_token), mytoken.MyToken('GEN','de')], original_sent, ir_ner_pos, diff_text, new_tagPtList, new_tokens, 1, new_tagPtList[match[0]])
    

    return questions_value

def gen_ner_object(original_sent, diff_text, ir_ner_pos, new_tagPtList, new_tokens):

    questions_object = []

    pattern_match1 = utils_algorithms.match_indexes(ir_ner_pos, ['OBJECT', 'VERB'], ['PUNCT']) #active

    if len(pattern_match1) > 0:
        pattern_match1 = remove_longer_matches(pattern_match1)
        for match in pattern_match1:
            questions_object = handle_pattern1(questions_object, match,  [mytoken.MyToken('GEN','Que'), mytoken.MyToken('GEN','objeto')], original_sent, ir_ner_pos, diff_text, new_tagPtList, new_tokens, 1, new_tagPtList[match[0]])
    
    return questions_object

def handle_pattern1(questions_ner, match, begin_term, original_sent, ir_ner_pos, diff_text, new_tagPtList, new_tokens, offset, answer):
    #new_tagPtList = treatVerbs(new_tagPtList, new_tokens)

    if new_tagPtList[match[-2]] != 'e' and new_tagPtList[match[-2]] != 'que' and len(match) > 3:
        range_sent = {'start': match[offset], 'end': match[-1]}
        #print("--------------------------------------> ", new_tagPtList[offset:match[-1]])
        questions_ner = gen_ner_first(begin_term, original_sent, ir_ner_pos, diff_text, range_sent, new_tagPtList, new_tokens, match, questions_ner, answer)
    
    elif new_tagPtList[match[-2]] == 'e' and len(match) > 3:
        range_sent = {'start': match[offset], 'end': match[-2]}
        questions_ner = gen_ner_first(begin_term, original_sent, ir_ner_pos, diff_text, range_sent, new_tagPtList, new_tokens, match, questions_ner, answer)

        questions_ner = gen_ner_third(begin_term, original_sent, ir_ner_pos, diff_text, new_tagPtList, new_tokens, match, questions_ner, answer)

    elif ir_ner_pos[match[-2]] == 'VERB' and len(match) == 3:
        questions_ner = gen_ner_second(begin_term, original_sent, ir_ner_pos, diff_text, new_tagPtList, new_tokens, match, questions_ner, answer)

        begin_term.append(new_tokens[match[offset]])
        questions_ner = gen_ner_third(begin_term, original_sent, ir_ner_pos, diff_text, new_tagPtList, new_tokens, match, questions_ner, answer)

    elif new_tagPtList[match[-2]] == 'que' and len(match) > 3:
        range_sent = {'start': match[offset], 'end': match[-2]}
        questions_ner = gen_ner_first(begin_term, original_sent, ir_ner_pos, diff_text, range_sent, new_tagPtList, new_tokens, match, questions_ner, answer)

        begin_term.extend(new_tokens[match[offset]:match[-1]])
        questions_ner = gen_ner_third(begin_term, original_sent, ir_ner_pos, diff_text, new_tagPtList, new_tokens, match, questions_ner, answer)
    else:
        pass

    return questions_ner

def gen_ner_first(begin_question, original_sent, ir_ner_pos, diff_text, range_sent, new_tagPtList, new_tokens, match, questions_ner, answer):

    questions_tokens = []
    questions_tokens.extend(begin_question)
    questions_tokens.extend(new_tokens[range_sent['start']:range_sent['end']])
    questions_tokens.append(mytoken.MyToken('GEN','?'))

    question_diff = WEIGHT_BLOOM * BLOOMS_REMEMBER_LEVEL + WEIGHT_SENTENCE * original_sent.difficulty + WEIGHT_TEXT * diff_text

    fact_subtype = 'syntax_facts'
    if questions_tokens[0].text == 'Onde':
        fact_subtype = 'syntax_where'

    new_question = factquestion.FactQuestion(uuid.uuid1(), 'syntax', fact_subtype, original_sent.sentText, questions_tokens, answer, question_diff)
    questions_ner.append(new_question)

    return questions_ner

def gen_ner_third(begin_question, original_sent, ir_ner_pos, diff_text, new_tagPtList, new_tokens, match, questions_ner, answer):

    pattern_match1b = utils_algorithms.match_indexes(ir_ner_pos, ['PUNCT'], ['PUNCT'])
    pattern_match1b = remove_longer_matches(pattern_match1b)
    for match1b in pattern_match1b:
        if match1b[0] == match[-1]:
            for match1c in pattern_match1b:
                if match1b[-1] == match1c[0]:

                    questions_tokens = []
                    questions_tokens.extend(begin_question)
                    questions_tokens.extend(new_tokens[match1c[1]:match1c[-1]])
                    questions_tokens.append(mytoken.MyToken('GEN','?'))

                    question_diff = WEIGHT_BLOOM * BLOOMS_REMEMBER_LEVEL + WEIGHT_SENTENCE * original_sent.difficulty + WEIGHT_TEXT * diff_text

                    fact_subtype = 'syntax_facts'
                    if questions_tokens[0].text == 'Onde':
                        fact_subtype = 'syntax_where'

                    new_question = factquestion.FactQuestion(uuid.uuid1(), 'syntax', fact_subtype, original_sent.sentText, questions_tokens, answer, question_diff)
                    questions_ner.append(new_question)
    
    return questions_ner

def gen_ner_second(begin_question, original_sent, ir_ner_pos, diff_text, new_tagPtList, new_tokens, match, questions_ner, answer):

    pattern_match1d = utils_algorithms.match_indexes(ir_ner_pos, ['VERB','PUNCT'], ['PUNCT'])
    pattern_match1d = remove_longer_matches(pattern_match1d)
    for match1d in pattern_match1d:
        if match1d[1] == match[-1]:

            questions_tokens = []
            questions_tokens.extend(begin_question)
            questions_tokens.append(new_tokens[match1d[0]])
            questions_tokens.extend(new_tokens[match1d[2]:match1d[-1]])
            questions_tokens.append(mytoken.MyToken('GEN','?'))

            question_diff = WEIGHT_BLOOM * BLOOMS_REMEMBER_LEVEL + WEIGHT_SENTENCE * original_sent.difficulty + WEIGHT_TEXT * diff_text

            fact_subtype = 'syntax_facts'
            if questions_tokens[0].text == 'Onde':
                fact_subtype = 'syntax_where'
                
            new_question = factquestion.FactQuestion(uuid.uuid1(), 'syntax', fact_subtype, original_sent.sentText, questions_tokens, answer, question_diff)
            questions_ner.append(new_question)

    return questions_ner