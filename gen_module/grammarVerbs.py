import uuid
import mcquestion
import clozequestion
import random
import qgsystem

import sys
sys.path.insert(0, 'utils')
import utils_algorithms

WEIGHT_GRAMMAR_CASE = 1/2
WEIGHT_SENTENCE = 1/2

def produceGverbstype(number_questions, force_diff, my_text, sents_options):

    if force_diff == 'DIFF':
        sents_options.sort(key = lambda x: x['diff'], reverse = True)
    elif force_diff == 'EASY':
        sents_options.sort(key = lambda x: x['diff'], reverse = False)
    else:
        random.shuffle(sents_options)

    size_sents_options = len(sents_options)

    questions = []

    if size_sents_options > 0:
        if number_questions <= len(sents_options):
            questions = sents_options[:number_questions]
        else:
            diff = number_questions-len(sents_options)
            questions = sents_options[:diff]

        mc_questions = buildMcVerbstype(questions, my_text)

        return mc_questions
    else:
        return []

def buildMcVerbstype(questions, my_text):
    options = [
    'um verbo copulativo e um verbo principal',
    'dois verbos principais',
    'um verbo auxiliar e um verbo principal',
    'um verbo auxiliar e um verbo copulativo'
    ]

    mc_questions = []
    for q in questions:
        current_options = options.copy()
        if q['type'] == 'cop_verb':
            del current_options[0]
        elif q['type'] == 'verb_verb':
            del current_options[1]
        elif q['type'] == 'aux_verb' or q['type'] == 'auxcop_verb':
            del current_options[2]
        elif q['type'] == 'aux_cop':
            del current_options[3]

        key_idx = q['sent_idx']
        sentence_text = '"' + my_text.textStruct[key_idx].getSentText() + '"'

        stat_text = sentence_text + "\n" + 'Identifique corretamente as subclasses dos verbos presentes na frase. ' + '\n'
        key_uuid = uuid.uuid1()
        new_mc_question = mcquestion.McQuestion(
            uuid.uuid1(),
            'g_verbstype', 
            key_uuid,
            stat_text, 
            [{'option_id': key_uuid, 'text':q['type_pt']}, {'option_id': uuid.uuid1(), 'text':current_options[0]}, {'option_id': uuid.uuid1(), 'text':current_options[1]}, {'option_id': uuid.uuid1(), 'text':current_options[2]}], 
            q['diff'],
            sentence_text,
            'Identifique corretamente as subclasses dos verbos presentes na frase.'
            )
        mc_questions.append(new_mc_question)

    return mc_questions

def has2Verbs(sent, idx_sent):
   
    if sent.stats.VERB['qty'] == 2 :
        if sent.stats.VERB_COPULATIVE['qty'] == 1 and sent.stats.VERB_MAIN['qty'] == 1:
            return { 'sent_idx': idx_sent, 'type': 'cop_verb', 'type_pt': 'um verbo copulativo e um verbo principal', 'diff': (2/5) * WEIGHT_GRAMMAR_CASE + sent.difficulty * WEIGHT_SENTENCE }
        if sent.stats.VERB_AUXILIARY['qty'] == 1 and sent.stats.VERB_MAIN['qty'] == 1:
            token_pos0 = sent.stats.VERB_AUXILIARY['indexes'][0]
            token_pos1 = sent.stats.VERB_MAIN['indexes'][0]
            if abs(token_pos0-token_pos1) > 1 and sent.tokens[token_pos0].words[0].lemma == 'ser':
                return { 'sent_idx': idx_sent, 'type': 'cop_verb', 'type_pt': 'um verbo copulativo e um verbo principal', 'diff': (2/5) * WEIGHT_GRAMMAR_CASE + sent.difficulty * WEIGHT_SENTENCE}
        if sent.stats.VERB_MAIN['qty'] == 2:
            return { 'sent_idx': idx_sent, 'type': 'verb_verb', 'type_pt': 'dois verbos principais', 'diff': (1/5) * WEIGHT_GRAMMAR_CASE + sent.difficulty * WEIGHT_SENTENCE}
        if sent.stats.VERB_AUXILIARY['qty'] == 1 and sent.stats.VERB_MAIN['qty'] == 1:
            token_pos = sent.stats.VERB_AUXILIARY['indexes'][0]
            if sent.tokens[token_pos].words[0].dependency_relation == 'aux':
                return { 'sent_idx': idx_sent, 'type': 'aux_verb', 'type_pt': 'um verbo auxiliar e um verbo principal', 'diff': (3/5) * WEIGHT_GRAMMAR_CASE + sent.difficulty * WEIGHT_SENTENCE}
        if sent.stats.VERB_AUXILIARY['qty'] == 2:
            token_pos0 = sent.stats.VERB_AUXILIARY['indexes'][0]
            token_pos1 = sent.stats.VERB_AUXILIARY['indexes'][1]
            if sent.tokens[token_pos0].words[0].dependency_relation == 'aux' and sent.tokens[token_pos1].words[0].dependency_relation == 'cop':
                return { 'sent_idx': idx_sent, 'type': 'aux_cop', 'type_pt': 'um verbo auxiliar e um verbo copulativo', 'diff': (4/5) * WEIGHT_GRAMMAR_CASE + sent.difficulty * WEIGHT_SENTENCE}
        if sent.stats.VERB_AUXILIARY['qty'] == 1 and sent.stats.VERB_MAIN['qty'] == 1:
            token_pos0 = sent.stats.VERB_AUXILIARY['indexes'][0]
            token_pos1 = sent.stats.VERB_MAIN['indexes'][0]
            if token_pos1-token_pos0 == 1 and sent.tokens[token_pos0].words[0].lemma == 'ser':
                return { 'sent_idx': idx_sent, 'type': 'auxcop_verb', 'type_pt': 'um verbo auxiliar e um verbo principal', 'diff': (5/5) * WEIGHT_GRAMMAR_CASE + sent.difficulty * WEIGHT_SENTENCE}
        else:
            return {}
    else:
        return {}


def produceGverbsmood(number_questions, force_diff, my_text, verbs_terms):

    mc_questions = []

    if len(verbs_terms) > 0:
        if force_diff == 'DIFF':
            verbs_terms.sort(key = lambda x: x['diff'], reverse = True)
        elif force_diff == 'EASY':
            verbs_terms.sort(key = lambda x: x['diff'], reverse = False)
        else:
            random.shuffle(verbs_terms)
        
        mc_questions = produceGroupsOf4by3(verbs_terms, number_questions, my_text)

    return mc_questions
    
def produceGroupsOf4by3(verbs_terms, number_questions, my_text):
    questions = []
    cpy_list = verbs_terms.copy()
    elems1 = []
    mc_questions = []
    
    while number_questions > 0 and len(cpy_list) >= 12:
        elems1 = []
        elems1.append(cpy_list.pop(0))

        to_remove = []

        # impedir que seja do mesmo TEMPO
        # first 3 elems 
        for idx, e in enumerate(cpy_list):
            if len(elems1) == 1 and e['mood'] == elems1[0]['mood'] and e['tense'] != elems1[0]['tense']:
                elems1.append(e)
                to_remove.append(idx)
            elif len(elems1) == 2 and e['mood'] == elems1[0]['mood'] and e['tense'] != elems1[0]['tense'] and e['tense'] != elems1[1]['tense']:
                elems1.append(e)
                to_remove.append(idx)
            if len(elems1) == 3:
                for i in sorted(to_remove, reverse=True):
                    del cpy_list[i]
                to_remove = []
                break

        cpycpy_list = []
        cpycpy_list = cpy_list.copy()
        elems1234 = [[], [], []]

        for l in elems1234:
            for e in cpycpy_list:
                if len(l) == 0 or len(l) == 1:
                    l.append(e)
                    cpycpy_list.remove(e)
                elif len(l) == 2 and l[0]['mood'] != l[1]['mood'] and (e['tense'] != l[0]['tense'] or e['tense'] != l[1]['tense']) :
                    l.append(e)
                    cpycpy_list.remove(e)
                elif len(l) == 2 and l[0]['mood'] == l[1]['mood'] and (e['mood'] != l[0]['mood'] or e['mood'] != l[1]['mood']) and (e['tense'] != l[0]['tense'] or e['tense'] != l[1]['tense']):
                    l.append(e)
                    cpycpy_list.remove(e)
                elif len(l) == 2 and l[0]['mood'] == l[1]['mood'] and e['mood'] == l[1]['mood']:
                    pass
                elif len(l) == 3:
                    break
                else:
                    pass
        
        #print(len(elems1234[0]), len(elems1234[1]), len(elems1234[2]))
        
        if len(elems1234[0]) == 3 and len(elems1234[1]) == 3 and len(elems1234[2]) == 3:
            elems1234.insert(0, elems1)
            questions.append(elems1234)
            number_questions -= 1
        else:
            pass

        mc_questions = buildMcVerbsmood(questions)

    return mc_questions


def produceGverbfeats(number_questions, force_diff, my_text, verbs_terms):
    questions = []

    if len(verbs_terms) > 0:
        if force_diff == 'DIFF':
            verbs_terms.sort(key = lambda x: x['diff'], reverse = True)
        elif force_diff == 'EASY':
            verbs_terms.sort(key = lambda x: x['diff'], reverse = False)
        else:
            random.shuffle(verbs_terms)
        for verb in verbs_terms:
            if len(questions) == 0 or (len(questions) > 0 and verb['tense'] != questions[-1]['tense']):
                questions.append(verb)
                verbs_terms.remove(verb)
                if len(verbs_terms) == 0 or number_questions == len(questions): break
            else:
                pass
        mc_questions = buildMcVerbfeats(questions, my_text)
        return mc_questions
    else:
        return []

def produceGcompleteverb(number_questions, force_diff, my_text, verbs_terms):
    questions = []

    if len(verbs_terms) > 0:
        if force_diff == 'DIFF':
            verbs_terms.sort(key = lambda x: x['diff'], reverse = True)
        elif force_diff == 'EASY':
            verbs_terms.sort(key = lambda x: x['diff'], reverse = False)
        else:
            random.shuffle(verbs_terms)

        for verb in verbs_terms:
            if len(questions) == 0 or (len(questions) > 0 and verb['tense'] != questions[-1]['tense']):
                questions.append(verb)
                verbs_terms.remove(verb)
                if len(verbs_terms) == 0 or number_questions == len(questions): break
            else:
                pass
        cloze_questions = buildClozeCompleteVerb(questions, my_text)
        return cloze_questions
    else:
        return []


def buildClozeCompleteVerb(questions, my_text):
    cloze_questions =  []

    for q in questions:
        if len(my_text.textStruct) >= q['sent_idx']:

            my_sent = my_text.textStruct[q['sent_idx']].tagPtList.copy()
    
            if len(q['token_idx']) == 1 or len(q['token_idx']) == 2:
                new_string = '('+q['lemma']+')'
                my_sent[q['token_idx'][0]] = new_string
            if len(q['token_idx']) == 2:
                del my_sent[q['token_idx'][1]]

        stat_text = q["tense_pt"] + " do modo " + q["mood_pt"] + ":"

        new_cloze_question = clozequestion.ClozeQuestion(
            uuid.uuid1(),
            'g_verbscomplete', 
            stat_text, 
            " ".join(my_sent),
            q['token'],
            1.0 )
        cloze_questions.append(new_cloze_question)
    
    return cloze_questions

def buildMcVerbsmood(questions):
    key_text, dist1_text, dist2_text, dist3_text = [],[],[],[]
    avg_diff = []

    mc_questions = []

    for q in questions:
        for i, triple in enumerate(q):
            for j in triple:
                if i == 0:
                    key_text.append(j['token'])
                elif i == 1:
                    dist1_text.append(j['token'])
                elif i == 2:
                    dist2_text.append(j['token'])
                elif i == 3:
                    dist3_text.append(j['token'])
                avg_diff.append(j['diff'])
        
        stat_text = 'O conjunto constituído apenas por formas verbais que pertencem ao mesmo modo verbal é: '
        key_uuid = uuid.uuid1()
        new_mc_question = mcquestion.McQuestion(
            uuid.uuid1(),
            'g_verbsmood', 
            key_uuid,
            stat_text, 
            [{'option_id': key_uuid, 'text':' - '.join(key_text)}, 
            {'option_id': uuid.uuid1(), 'text':' - '.join(dist1_text)},
            {'option_id': uuid.uuid1(), 'text':' - '.join(dist2_text)}, 
            {'option_id': uuid.uuid1(), 'text':' - '.join(dist3_text)}],
            sum(avg_diff) / len(avg_diff) )
        mc_questions.append(new_mc_question)

        key_text, dist1_text, dist2_text, dist3_text = [],[],[],[]
    
    return mc_questions

def buildMcVerbfeats(questions, my_text):

    verbs_options = [
    {'mood': 'INDICATIVE', 'tense': 'PRESENT', 'verb_pt': 'Presente do modo indicativo'},
    {'mood': 'INDICATIVE', 'tense': 'PASTPERFECT', 'verb_pt': 'Pretérito perfeito do modo indicativo'},
    {'mood': 'INDICATIVE', 'tense': 'PASTPERFECT_C', 'verb_pt': 'Pretérito perfeito composto do modo indicativo'},
    {'mood': 'INDICATIVE', 'tense': 'IMPERFECT', 'verb_pt': 'Pretérito imperfeito do modo indicativo'},
    {'mood': 'INDICATIVE', 'tense': 'PLUSPERFECT', 'verb_pt': 'Pretério mais-que-perfeito do modo indicativo'},
    {'mood': 'INDICATIVE', 'tense': 'PLUSPERFECT_C', 'verb_pt': 'Pretério mais-que-perfeito composto do modo indicativo'},
    {'mood': 'INDICATIVE', 'tense': 'FUTURE', 'verb_pt': 'Futuro do modo indicativo'},
    {'mood': 'INDICATIVE', 'tense': 'FUTURE_C', 'verb_pt': 'Futuro composto do modo indicativo'},

    {'mood': 'CONJUNCTIVE', 'tense': 'PRESENT', 'verb_pt': 'Presente do modo conjuntivo'},
    {'mood': 'CONJUNCTIVE', 'tense': 'PASTPERFECT', 'verb_pt': 'Pretérito perfeito do modo conjuntivo'},
    {'mood': 'CONJUNCTIVE', 'tense': 'IMPERFECT', 'verb_pt': 'Pretérito imperfeito do modo conjuntivo'},
    {'mood': 'CONJUNCTIVE', 'tense': 'PLUSPERFECT', 'verb_pt': 'Pretérito mais que perfeito do modo conjuntivo'},
    {'mood': 'CONJUNCTIVE', 'tense': 'FUTURE', 'verb_pt': 'Futuro do modo conjuntivo'},
    {'mood': 'CONJUNCTIVE', 'tense': 'FUTURE_C', 'verb_pt': 'Futuro composto do modo conjuntivo'},

    {'mood': 'CONDITIONAL', 'tense': 'PRESENT', 'verb_pt': 'Presente do modo condicional'},
    {'mood': 'CONDITIONAL', 'tense': 'PAST', 'verb_pt': 'Pretérito (composto) do modo condicional'},
    ]
            
    mc_questions = []
    for q in questions:

        copy_verbs_options = verbs_options.copy()

        for idx, option in enumerate(copy_verbs_options):
            if option['mood'] == q['mood'] and option['tense'] == q['tense']:
                del copy_verbs_options[idx]

        dist1_idx = random.randrange(0, 14)
        dist1 = copy_verbs_options[dist1_idx]
        del copy_verbs_options[dist1_idx]

        dist2_idx = random.randrange(0, 13)
        dist2 = copy_verbs_options[dist2_idx]
        del copy_verbs_options[dist2_idx]

        dist3_idx = random.randrange(0, 12)
        dist3 = copy_verbs_options[dist3_idx]
        del copy_verbs_options[dist3_idx]

        key_text = q['tense_pt'] + ' do modo ' + q['mood_pt']

        sent_idx = q['sent_idx']
        sent_text = my_text.textStruct[sent_idx].getSentText()

        stat_text = sent_text + "\n" + 'A forma verbal "' + q['token'] + '" encontra-se no'
        key_uuid = uuid.uuid1()
        
        new_mc_question = mcquestion.McQuestion(
            uuid.uuid1(),
            'g_verbfeats', 
            key_uuid,
            stat_text, 
            [{'option_id': key_uuid, 'text':key_text}, 
            {'option_id': uuid.uuid1(), 'text':dist1['verb_pt']},
            {'option_id': uuid.uuid1(), 'text':dist2['verb_pt']}, 
            {'option_id': uuid.uuid1(), 'text':dist3['verb_pt']}],
            q['diff'],
            '"' + sent_text + '"',
            'A forma verbal "' + q['token'] + '" encontra-se no'
            )
        mc_questions.append(new_mc_question)
    
    return mc_questions

def produceVerbTerms(sent, idx_sent):

    if sent.stats.VERB['qty'] > 0:
        for token_idx in sent.stats.VERB['indexes']:
            if sent.tokens[token_idx].sub_tag == 'VERB_MAIN' or sent.tokens[token_idx].sub_tag == 'VERB_COPULATIVE':
                verb_token = sent.tokens[token_idx]
                if len(verb_token.words) == 1:
                    compound_value = 0
                    verb_word = verb_token.words[0]
                    mood = {'designation': None, 'pt': None, 'weight': None}
                    tense = {'designation': None, 'pt': None, 'weight': None}
                    if 'Mood' in verb_word.feats and 'Tense' in verb_word.feats:
                        if verb_word.feats['Mood'] == 'Ind':
                            mood.update({'designation': 'INDICATIVE', 'pt': 'indicativo', 'weight': 1/3})
                        elif verb_word.feats['Mood'] == 'Sub':
                            mood.update({'designation': 'CONJUNCTIVE', 'pt': 'conjuntivo', 'weight': 2/3})
                        elif verb_word.feats['Mood'] == 'Cnd':
                            mood.update({'designation': 'CONDITIONAL', 'pt': 'condicional', 'weight': 3/3})
                        else:
                            pass
                    if 'Tense' in verb_word.feats and mood['designation'] != None:
                        if verb_word.feats['Tense'] == 'Pres':
                            tense.update({'designation': 'PRESENT', 'pt': 'Presente', 'weight': 1/4})
                        elif verb_word.feats['Tense'] == 'Past':
                            tense.update({'designation': 'PASTPERFECT', 'pt': 'Pretérito perfeito', 'weight': 2/4})
                        elif verb_word.feats['Tense'] == 'Imp':
                            tense.update({'designation': 'IMPERFECT', 'pt': 'Pretérito imperfeito', 'weight': 2/4})
                        elif verb_word.feats['Tense'] == 'Pqp':
                            tense.update({'designation': 'PLUSPERFECT', 'pt': 'Pretério mais-que-perfeito', 'weight': 4/4})
                        elif verb_word.feats['Tense'] == 'Fut':
                            tense.update({'designation': 'FUTURE', 'pt': 'Futuro', 'weight': 3/4})
                        else:
                            pass
                    if mood['designation'] != None and tense['designation'] != None:
                        #if not any(d['token'] == verb_word.text for d in verbs_terms):
                        return {'sent_idx': idx_sent, 'token': verb_word.text, 'token_idx': [token_idx], 'lemma': verb_word.lemma, 'mood': mood['designation'], 'mood_pt': mood['pt'], 'tense': tense['designation'], 'tense_pt': tense['pt'], 'diff': mood['weight']*(1/3) + tense['weight']*(1/3) + compound_value*(1/3) }
            elif sent.tokens[token_idx].sub_tag == 'VERB_AUXILIARY':
                verb_token = sent.tokens[token_idx]
                token_next = None
                if len(verb_token.words) == 1 and verb_token.words[0].lemma == 'ter' and (token_idx + 1) <= len(sent.tokens):
                    token_next = sent.tokens[token_idx+1]
                    verb_word = verb_token.words[0]
                    compound_value = 1
                if token_next != None and token_next.tag == 'VERB' and len(token_next.words) == 1 and 'VerbForm' in token_next.words[0].feats and token_next.words[0].feats['VerbForm'] == 'Part':
                    mood = {'designation': None, 'pt': None, 'weight': None}
                    tense = {'designation': None, 'pt': None, 'weight': None}
                    if 'Mood' in verb_word.feats and 'Tense' in verb_word.feats:
                        if verb_word.feats['Mood'] == 'Ind':
                            mood.update({'designation': 'INDICATIVE', 'pt': 'indicativo', 'weight': 1/3})
                        elif verb_word.feats['Mood'] == 'Sub':
                            mood.update({'designation': 'CONJUNCTIVE', 'pt': 'conjuntivo', 'weight': 2/3})
                        elif verb_word.feats['Mood'] == 'Cnd':
                            mood.update({'designation': 'CONDITIONAL', 'pt': 'condicional', 'weight': 3/3})
                        else:
                            pass
                    if 'Tense' in verb_word.feats and mood['designation'] != None:
                        if verb_word.feats['Tense'] == 'Pres' and mood['designation'] == 'INDICATIVE':
                            tense.update({'designation': 'PASTPERFECT_C', 'pt': 'Pretério perfeito composto', 'weight': 1/2})
                        elif verb_word.feats['Tense'] == 'Pres' and mood['designation'] == 'CONJUNCTIVE':
                            tense.update({'designation': 'PASTPERFECT', 'pt': 'Pretério perfeito', 'weight': 2/2})
                        elif verb_word.feats['Tense'] == 'Pres' and mood['designation'] == 'CONDITIONAL':
                            tense.update({'designation': 'PAST', 'pt': 'Pretérito', 'weight': 2/2})
                        
                        elif verb_word.feats['Tense'] == 'Imp' and mood['designation'] == 'INDICATIVE':
                            tense.update({'designation': 'PLUSPERFECT_C', 'pt': 'Pretérito mais-que-perfeito composto', 'weight': 1/2})
                        elif verb_word.feats['Tense'] == 'Imp' and mood['designation'] == 'CONJUNCTIVE':
                            tense.update({'designation': 'PLUSPERFECT', 'pt': 'Pretérito mais-que-perfeito', 'weight': 2/2})

                        elif verb_word.feats['Tense'] == 'Fut' and mood['designation'] == 'INDICATIVE':
                            tense.update({'designation': 'FUTURE_C', 'pt': 'Futuro composto', 'weight': 2/2})
                        elif verb_word.feats['Tense'] == 'Fut' and mood['designation'] == 'CONJUNCTIVE':
                            tense.update({'designation': 'FUTURE_C', 'pt': 'Futuro composto', 'weight': 2/2})
                        else:
                            pass
                    if mood['designation'] != None and tense['designation'] != None:
                        #if not any(d['token'] == verb_word.text for d in verbs_terms):
                        return {'sent_idx': idx_sent, 'token': verb_word.text + ' ' + token_next.text , 'token_idx': [token_idx, token_idx+1], 'lemma': token_next.words[0].lemma, 'mood': mood['designation'], 'mood_pt': mood['pt'], 'tense': tense['designation'], 'tense_pt': tense['pt'], 'diff': mood['weight']*(1/3) + tense['weight']*(1/3) + compound_value*(1/3) }
            else:
                return {}
    else:
        return {}

def simplecomplex(sent, idx_sent):
    if sent.stats.VERB_MAIN['qty'] == 1 and sent.stats.VERB_COPULATIVE['qty'] ==  0:
        if sent.stats.VERB_AUXILIARY['qty'] == 0:
            return {'sentence_idx': idx_sent, 'token': 'empty', 'type': 'SIMPLE', 'diff': (1/4)}
        elif sent.stats.VERB_AUXILIARY['qty'] == 1 and (sent.stats.VERB_MAIN['indexes'][0]-sent.stats.VERB_AUXILIARY['indexes'][0]) == 1:
            return {'sentence_idx': idx_sent, 'token': 'empty', 'type': 'SIMPLE', 'diff': (2/4)}
        elif sent.stats.VERB_AUXILIARY['qty'] > 1:
            return {}
    elif sent.stats.VERB_MAIN['qty'] == 0 and sent.stats.VERB_COPULATIVE['qty'] ==  1:
        if sent.stats.VERB_AUXILIARY['qty'] == 0:
            return {'sentence_idx': idx_sent, 'token': 'empty', 'type': 'SIMPLE', 'diff': (1/4)}
        elif sent.stats.VERB_AUXILIARY['qty'] == 1 and (sent.stats.VERB_COPULATIVE['indexes'][0]-sent.stats.VERB_AUXILIARY['indexes'][0]) == 1:
            return {'sentence_idx': idx_sent, 'token': 'empty', 'type': 'SIMPLE', 'diff': (3/4)}
        elif sent.stats.VERB_AUXILIARY['qty'] > 1:
            return {}
    elif sent.stats.VERB_MAIN['qty'] > 1 or sent.stats.VERB_COPULATIVE['qty'] >  1:
        VERB_MAIN = 0
        VERB_COPULATIVE = 0
        VERB_AUXILIARY = 0
        if sent.stats.VERB_MAIN['qty'] > 0:
            VERB_MAIN = 1
        if sent.stats.VERB_COPULATIVE['qty'] > 0:
            VERB_COPULATIVE = 1
        if sent.stats.VERB_AUXILIARY['qty'] > 0:
            VERB_AUXILIARY = 1
        return {'sentence_idx': idx_sent, 'token': 'empty', 'type': 'COMPLEX', 'diff': 4/4}
    else:
        return {}

def produceGsimplecomplex(number_questions, force_diff, my_text, simple_complex):
    if force_diff == 'DIFF':
        simple_complex.sort(key = lambda x: x['diff'], reverse = True)
    elif force_diff == 'EASY':
        simple_complex.sort(key = lambda x: x['diff'], reverse = False)
    else:
        random.shuffle(simple_complex)

    questions = utils_algorithms.produceGroupsoOf4(number_questions, simple_complex, 'misc', my_text)

    mc_questions = buildMcSimpleComplex(questions, my_text)

    return mc_questions


def buildMcSimpleComplex(questions, my_text):

    mc_questions = []

    for q in questions:
        key_idx = q[0]['sentence_idx']
        dist1_idx = q[1]['sentence_idx']
        dist2_idx = q[2]['sentence_idx']
        dist3_idx = q[3]['sentence_idx']

        key_text = my_text.textStruct[key_idx].getSentText()
        dist1_text = my_text.textStruct[dist1_idx].getSentText()
        dist2_text = my_text.textStruct[dist2_idx].getSentText()
        dist3_text = my_text.textStruct[dist3_idx].getSentText()

        simpleOrComplex = ''
        if q[0]['type'] == 'SIMPLE':
            simpleOrComplex = 'simples'
        elif q[0]['type'] == 'COMPLEX':
            simpleOrComplex = 'complexa'
        elif q[0]['type'] == 'RANDOM':
            simpleOrComplex = '??????????????'

        stat_text = 'Assinale a única frase ' + simpleOrComplex + ' das quatro apresentadas.' + "\n"

        key_uuid = uuid.uuid1()
        new_mc_question = mcquestion.McQuestion(
            uuid.uuid1(),
            'g_simplecomplex', 
            key_uuid,
            stat_text, 
            [{'option_id': key_uuid, 'text':key_text}, 
            {'option_id': uuid.uuid1(), 'text':dist1_text},
            {'option_id': uuid.uuid1(), 'text':dist2_text}, 
            {'option_id': uuid.uuid1(), 'text':dist3_text}],
            q[0]['diff'])
        mc_questions.append(new_mc_question)

    return mc_questions



