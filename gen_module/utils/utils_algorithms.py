from collections import defaultdict
import itertools
from itertools import combinations 

def produceGroupsoOf4(number_questions, list_unique, type_comb, my_text):
    question = []
    questions = []
    last_question_type = None
    cpy_list = list_unique.copy()

    while number_questions > 0 and len(cpy_list) > 0:
        for e in cpy_list:
            if e['type'] != last_question_type:
                elem = e
                question.append(elem)
                cpy_list.remove(e)
                break

        for list_elem in list_unique:
            if type_comb == 'misc':
                if list_elem['type'] != elem['type'] and not any(d['sentence_idx'] == list_elem['sentence_idx'] for d in question):
                    question.append(list_elem)
                    if len(question) == 4: break
            elif type_comb == 'unique':
                if not any(d['type'] == list_elem['type'] for d in question):
                    question.append(list_elem)
                    if len(question) == 4: break
            else:
                pass

        if len(question) == 4:
            last_question_type = question[0]['type']
            questions.append(question)
            number_questions -= 1

        question = []

    return questions

def list_duplicates(seq, baseline):
    tally = defaultdict(list)
    for i,item in enumerate(seq):
        tally[item].append(i)
    return ((key,locs) for key,locs in tally.items() if len(locs)>baseline)


def group_consecutives(vals, step=1):
    """Return list of consecutive lists of numbers from vals (number list)."""
    run = []
    result = [run]
    expect = None
    for v in vals:
        if (v == expect) or (expect is None):
            run.append(v)
        else:
            run = [v]
            result.append(run)
        expect = v + step
    return result

def match_indexes(probelist, head, tail):
    """ returns a list with all indexes in a list of strings that matches 
        prefix and tail 
    """
    result=list()
    step = len(head)
    last = len(probelist) - len(tail)
    if (step + len(tail) <= len(probelist)):
        for i in range(0,last):
            if (probelist[i:i+len(head)] == head):
                for j in range (i+step,last + 1):
                    if probelist[j:j+len(tail)] == tail:
                        result.append(list(range(i,j+len(tail))))
    return result

def merge_sublists(my_list):
    return list(itertools.chain.from_iterable(my_list))

def get_indexList_matchElems(a, b):
    indexes = []
    for i in range(len(a)):
        if a[i:i+len(b)] == b:
            indexes.append((i, i+len(b)))
    return indexes

def find_matching_index(list1, list2):

    inverse_index = { element: index for index, element in enumerate(list1) }

    return [(index, inverse_index[element])
        for index, element in enumerate(list2) if element in inverse_index]

