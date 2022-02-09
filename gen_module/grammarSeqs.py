import mytext
import mcquestion
from collections import defaultdict
from itertools import combinations
import itertools
import uuid
import random 
import mcquestion
import operator

import sys
sys.path.insert(0, 'utils')
import utils_algorithms

def produceGsequence(number_questions, force_diff, my_text, sents_size):
        #sents_size = my_text.getSentsSize() # returns an array with all sentences lenght's

        all_combs2 = createGroups(sents_size) #create groups according sentence lenght

        all_combs2 = calcSimandOrders(all_combs2, force_diff, my_text) #calculates similiarity between each pair (nC2) of same group and orders them by heuristic value

        questions = []

        if all_combs2:
             while number_questions > 0:
                if not all_combs2:
                    break

                elem_and_combnr = findBestComb(all_combs2, force_diff) # best pair from all groups

                all_combs2[elem_and_combnr[1]].pop(0) # pop out first element (key)

                if not all_combs2[elem_and_combnr[1]]: # rebuild all_combs2 list
                    all_combs2 = [x for x in all_combs2 if x != []]
                    continue
                
                question = findOptions(all_combs2, elem_and_combnr[0], elem_and_combnr[1]) #find more 2 options for the first pair
                if question != -1:
                    questions.append(question)

                number_questions = number_questions - 1

        mc_questions = buildMcQuestions(questions, my_text)

        return mc_questions

def createGroups(sents_size):
    all_combs2 = []
    #create groups (number of tokens - list of index )
    for group in sorted(utils_algorithms.list_duplicates(sents_size, 1)):
        if len(group[1]) >= 4 and group[0] >= 6 and group[0] <= 13:
            comb2 = combinations(group[1], 2)
            comb2 = [list(elem) for elem in comb2]
            all_combs2.append(comb2)
        else:
            pass
    if not all_combs2:
        return []
    else:
        return all_combs2
    
def findBestComb(all_combs2, force_diff):
    top_triples = []
    res = []
    for idx, comb in enumerate(all_combs2):
        elem = comb[0]
        elem.append(idx)
        top_triples.append(elem)
    if force_diff == 'DIFF':
        res = max(top_triples, key=operator.itemgetter(2))
    elif force_diff == 'EASY':
        res = min(top_triples, key=operator.itemgetter(2))
    elif force_diff == 'RANDOM':
        res = random.choice(top_triples)
    else:
        return -1
    return [res, res[3]]


def findOptions(all_combs2, elem, comb_nr):
    chosen_elems = []
    chosen_elems.append(elem[0])
    chosen_elems.append(elem[1])

    elem0score = 0
    elem1score = 0

    for comb2 in all_combs2[comb_nr]:
        if len(chosen_elems) == 4:
            break
        if comb2[0] == elem[0] and comb2[1] not in chosen_elems:
            chosen_elems.append(comb2[1])
            elem0score = elem0score + 1
        elif comb2[0] == elem[1] and comb2[1] not in chosen_elems:
            chosen_elems.append(comb2[1])
            elem1score = elem1score + 1
        elif comb2[1] == elem[0] and comb2[0] not in chosen_elems:
            chosen_elems.append(comb2[0])
            elem0score = elem0score + 1
        elif comb2[1] == elem[1] and comb2[0] not in chosen_elems:
            chosen_elems.append(comb2[0])
            elem1score = elem1score + 1


    if len(chosen_elems) == 4:
        if elem0score >= elem1score:
            avg_weight = calcAvgWeight(elem, elem[0], chosen_elems[2], chosen_elems[3], all_combs2[comb_nr])
            return {'sents_idx': chosen_elems, 'first_pair_weight': elem[2], 'avg_weight': avg_weight}
        elif elem1score > elem0score:
            swapPositions(chosen_elems, 0, 1)
            avg_weight = calcAvgWeight(elem, elem[1], chosen_elems[2], chosen_elems[3], all_combs2[comb_nr])
            return {'sents_idx': chosen_elems, 'first_pair_weight': elem[2], 'avg_weight': avg_weight}
        else:
            pass
    else:
        return -1

def calcAvgWeight(elem, elem_idx, elem2_idx, elem3_idx, combs):
    weights = []
    weights.append(elem[2])

    for comb in combs:
        if (elem_idx == comb[0] and elem2_idx == comb[1]) or (elem_idx == comb[1] and elem2_idx == comb[0]):
            weights.append(comb[2])
            if len(weights) == 3: break
        elif (elem_idx == comb[0] and elem3_idx == comb[1]) or (elem_idx == comb[1] and elem3_idx == comb[0]):
            weights.append(comb[2])
            if len(weights) == 3: break
        else:
            pass

    if len(weights) == 3:
        return sum(weights) / len(weights)
    else:
        return -1


def swapPositions(my_list, pos1, pos2): 
    my_list[pos1], my_list[pos2] = my_list[pos2], my_list[pos1] 
    return list


def calcSimandOrders(all_combs2, force_diff, my_text):
    new_combs2 = []

    for group_comb2 in all_combs2:
        new_group2 = []
        for comb2 in group_comb2:
            distance = calcSentsDistance(comb2, my_text)
            if distance == 1:
                pass
            else:
                comb2.append(distance)
                new_group2.append(comb2)
        if force_diff == 'DIFF':
            new_group2.sort(key = lambda x: x[2], reverse = True)
        elif force_diff == 'EASY':
            new_group2.sort(key = lambda x: x[2], reverse = False)
        else:
            random.shuffle(new_group2)
        new_combs2.append(new_group2)

    if not new_combs2:
        return []
    else:
        return new_combs2
            
def calcSentsDistance(comb2, my_text):
    tag_seq1 = my_text.textStruct[comb2[0]].getTagsSeq()
    tag_seq2 = my_text.textStruct[comb2[1]].getTagsSeq()
    
    counter = 0
    for index, tag in enumerate(tag_seq1):
        if tag == tag_seq2[index]:
            counter = counter + 1
            
    return counter/len(tag_seq1)


def buildMcQuestions(questions, my_text):

    mc_questions = []
    for q in questions:
        key_idx = q['sents_idx'][0]
        dist1_idx = q['sents_idx'][1]
        dist2_idx = q['sents_idx'][2]
        dist3_idx = q['sents_idx'][3]

        key_seq = my_text.textStruct[key_idx].getTagsPt()

        key_text = my_text.textStruct[key_idx].getSentText()
        dist1_text = my_text.textStruct[dist1_idx].getSentText()
        dist2_text = my_text.textStruct[dist2_idx].getSentText()
        dist3_text = my_text.textStruct[dist3_idx].getSentText()

        ##calc diff
        dist_pair_1 = calcSentsDistance([key_idx, dist1_idx], my_text)
        dist_pair_2 = calcSentsDistance([key_idx, dist2_idx], my_text)
        dist_pair_3 = calcSentsDistance([key_idx, dist3_idx], my_text)

        #q['avg_weight'] exists but it's not being calculated in a correct form
        avg_weight = (dist_pair_1 + dist_pair_2 + dist_pair_3) / 3

        stat_text = 'Indique a frase que contém a sequência:' + "\n" + key_seq

        key_uuid = uuid.uuid1()

        new_mc_question = mcquestion.McQuestion(
            uuid.uuid1(),
            'g_sequence', 
            key_uuid,
            stat_text, 
            [{'option_id': key_uuid, 'text':key_text}, {'option_id': uuid.uuid1(), 'text':dist1_text}, {'option_id': uuid.uuid1(), 'text':dist2_text}, {'option_id': uuid.uuid1(), 'text':dist3_text}], 
            avg_weight)
    
        mc_questions.append(new_mc_question)
        
    #NEED TO ORDER AGAIN
    mc_questions.sort(key = lambda x: x.diff, reverse = True)

    return mc_questions