import sys
sys.path.insert(0, 'utils')
import utils_algorithms
import uuid
import mcquestion
import random

WEIGHT_GRAMMAR_CASE = 1
WEIGHT_SENTENCE = 0

def prepdetpron(sent, idx_sent):

    if len(sent.stats.NR_a['type']) == len(set(sent.stats.NR_a['type'])) and len(sent.tokens) <= 15:
        i = len(sent.stats.NR_a['type'])-1
        while i >= 0:
            if sent.stats.NR_a['type'][i] == 'PRON_ATOM':
                return {'sentence_idx': idx_sent, 'token': sent.stats.NR_a['indexes'][i], 'type': 'PRON', 'type_tp': 'um pronome', 'diff': (2/4) * WEIGHT_GRAMMAR_CASE + sent.difficulty * WEIGHT_SENTENCE}
            elif sent.stats.NR_a['type'][i] == 'PRON_CLITIC':
                return {'sentence_idx': idx_sent, 'token': sent.stats.NR_a['indexes'][i], 'type': 'PRON', 'type_tp': 'um pronome', 'diff': (3/4) * WEIGHT_GRAMMAR_CASE + sent.difficulty * WEIGHT_SENTENCE}
            elif sent.stats.NR_a['type'][i] == 'DET':
                return {'sentence_idx': idx_sent, 'token': sent.stats.NR_a['indexes'][i], 'type': 'DET',  'type_tp': 'um determinante', 'diff': (1/4) * WEIGHT_GRAMMAR_CASE + sent.difficulty * WEIGHT_SENTENCE}
            elif sent.stats.NR_a['type'][i] == 'PREP':
                return {'sentence_idx': idx_sent, 'token': sent.stats.NR_a['indexes'][i], 'type': 'PREP', 'type_tp': 'uma preposição', 'diff': (4/4) * WEIGHT_GRAMMAR_CASE + sent.difficulty * WEIGHT_SENTENCE}
            else:
                pass
            i -= 1
    else:
        return {}

def produceGprepdetpron(number_questions, force_diff, my_text, prep_det_pron):

    if force_diff == 'DIFF':
        prep_det_pron.sort(key = lambda x: x['diff'], reverse = True)
    elif force_diff == 'EASY':
        prep_det_pron.sort(key = lambda x: x['diff'], reverse = False)
    elif force_diff == 'RANDOM':
        random.shuffle(prep_det_pron)

    questions = utils_algorithms.produceGroupsoOf4(number_questions, prep_det_pron, 'misc', my_text)

    mc_questions = buildMc3types(questions, my_text)

    return mc_questions


def conjtype(sent, idx_sent):

    if sent.stats.CCONJ['qty'] ==  1:
        if sent.stats.CCONJ_COPULATIVE['qty'] == 1:
            return {'sentence_idx': idx_sent, 'token': sent.stats.CCONJ_COPULATIVE['indexes'][0], 'type': 'CCONJ_COPULATIVE', 'type_pt': 'uma conjunção coordenativa copulativa', 'diff': ((2/5) * WEIGHT_GRAMMAR_CASE) + sent.difficulty * WEIGHT_SENTENCE}
        elif sent.stats.CCONJ_ADVERSATIVE['qty'] == 1:
            return {'sentence_idx': idx_sent, 'token': sent.stats.CCONJ_ADVERSATIVE['indexes'][0], 'type': 'CCONJ_ADVERSATIVE', 'type_pt': 'uma conjunção coordenativa adversativa', 'diff': ((3/5) * WEIGHT_GRAMMAR_CASE) + sent.difficulty * WEIGHT_SENTENCE}
        elif sent.stats.CCONJ_DISJUNCTIVE['qty'] == 1:
            return {'sentence_idx': idx_sent, 'token': sent.stats.CCONJ_DISJUNCTIVE['indexes'][0], 'type': 'CCONJ_DISJUNCTIVE', 'type_pt': 'uma conjunção coordenativa disjuntiva', 'diff': 1 * WEIGHT_GRAMMAR_CASE + sent.difficulty * WEIGHT_SENTENCE}
        elif sent.stats.CCONJ_CONCLUSIVE['qty'] == 1:
            return {'sentence_idx': idx_sent, 'token': sent.stats.CCONJ_CONCLUSIVE['indexes'][0], 'type': 'CCONJ_CONCLUSIVE', 'type_pt': 'uma conjunção coordenativa conclusiva', 'diff': 1 * WEIGHT_GRAMMAR_CASE + sent.difficulty * WEIGHT_SENTENCE}
        elif sent.stats.CCONJ_EXPLICATIVE['qty'] == 1:
            return {'sentence_idx': idx_sent, 'token': sent.stats.CCONJ_EXPLICATIVE['indexes'][0], 'type': 'CCONJ_EXPLICATIVE', 'type_pt': 'uma conjunção coordenativa explicativa', 'diff': ((4/5) * WEIGHT_GRAMMAR_CASE) + sent.difficulty * WEIGHT_SENTENCE}
    elif sent.stats.SCONJ['qty'] == 1:
        if sent.stats.SCONJ_COMPLETIVE['qty'] == 1:
            return {'sentence_idx': idx_sent, 'token': sent.stats.SCONJ_COMPLETIVE['indexes'][0], 'type': 'SCONJ_COMPLETIVE', 'type_pt': 'uma conjunção subordinativa completiva', 'diff': ((2/5) * WEIGHT_GRAMMAR_CASE) + sent.difficulty * WEIGHT_SENTENCE}
        elif sent.stats.SCONJ_CAUSAL['qty'] == 1:
            return {'sentence_idx': idx_sent, 'token': sent.stats.SCONJ_CAUSAL['indexes'][0], 'type': 'SCONJ_CAUSAL', 'type_pt': 'uma conjunção subordinativa causal', 'diff': ((2/5) * WEIGHT_GRAMMAR_CASE) + sent.difficulty * WEIGHT_SENTENCE}
        elif sent.stats.SCONJ_FINAL['qty'] == 1:
            return {'sentence_idx': idx_sent, 'token': sent.stats.SCONJ_FINAL['indexes'][0], 'type': 'SCONJ_FINAL', 'type_pt': 'uma conjunção subordinativa final', 'diff': ((2/5) * WEIGHT_GRAMMAR_CASE) + sent.difficulty * WEIGHT_SENTENCE}
        elif sent.stats.SCONJ_TEMPORAL['qty'] == 1:
            return {'sentence_idx': idx_sent, 'token': sent.stats.SCONJ_TEMPORAL['indexes'][0], 'type': 'SCONJ_TEMPORAL', 'type_pt': 'uma conjunção subordinativa temporal', 'diff': ((2/5) * WEIGHT_GRAMMAR_CASE) + sent.difficulty * WEIGHT_SENTENCE}
        elif sent.stats.SCONJ_CONCESSIVE['qty'] == 1:
            return {'sentence_idx': idx_sent, 'token': sent.stats.SCONJ_CONCESSIVE['indexes'][0], 'type': 'SCONJ_CONCESSIVE', 'type_pt': 'uma conjunção subordinativa concessiva', 'diff': ((2/5) * WEIGHT_GRAMMAR_CASE) + sent.difficulty * WEIGHT_SENTENCE}
        elif sent.stats.SCONJ_CONDITIONAL['qty'] == 1:
            return {'sentence_idx': idx_sent, 'token': sent.stats.SCONJ_CONDITIONAL['indexes'][0], 'type': 'SCONJ_CONDITIONAL', 'type_pt': 'uma conjunção subordinativa condicional', 'diff': ((2/5) * WEIGHT_GRAMMAR_CASE) + sent.difficulty * WEIGHT_SENTENCE}
        elif sent.stats.SCONJ_COMPARATIVE['qty'] == 1:
            return {'sentence_idx': idx_sent, 'token': sent.stats.SCONJ_COMPARATIVE['indexes'][0], 'type': 'SCONJ_COMPARATIVE', 'type_pt': 'uma conjunção subordinativa comparativa', 'diff': ((2/5) * WEIGHT_GRAMMAR_CASE) + sent.difficulty * WEIGHT_SENTENCE}
        elif sent.stats.SCONJ_CONSECUTIVE['qty'] == 1:
            return {'sentence_idx': idx_sent, 'token': sent.stats.SCONJ_CONSECUTIVE['indexes'][0], 'type': 'SCONJ_CONSECUTIVE', 'type_pt': 'uma conjunção subordinativa consecutiva', 'diff': ((2/5) * WEIGHT_GRAMMAR_CASE) + sent.difficulty * WEIGHT_SENTENCE}
    else:
        return {}

def produceGconjtype(number_questions, force_diff, my_text, conjs_unique):

    if force_diff == 'DIFF':
        conjs_unique.sort(key = lambda x: x['diff'], reverse = True)
    elif force_diff == 'EASY':
        conjs_unique.sort(key = lambda x: x['diff'], reverse = False)
    elif force_diff == 'RANDOM':
        random.shuffle(conjs_unique)

    questions = utils_algorithms.produceGroupsoOf4(number_questions, conjs_unique, 'unique', my_text)

    mc_questions = buildWhichType(questions, my_text, 'g_conjtype')

    return mc_questions

def prontype(sent, idx_sent):
    if sent.stats.PRON['qty'] == 1:
        if sent.stats.PRON_POSSESSIVE['qty'] == 1:
            return {'sentence_idx': idx_sent, 'token': sent.stats.PRON_POSSESSIVE['indexes'][0], 'type': 'PRON_POSSESSIVE', 'type_pt': 'um pronome possessivo', 'diff': ((2/5) * WEIGHT_GRAMMAR_CASE) + sent.difficulty * WEIGHT_SENTENCE}
        elif sent.stats.PRON_DEMONSTRATIVE['qty'] == 1:
            return {'sentence_idx': idx_sent, 'token': sent.stats.PRON_DEMONSTRATIVE['indexes'][0], 'type': 'PRON_DEMONSTRATIVE', 'type_pt': 'um pronome demonstrativo', 'diff': ((3/5) * WEIGHT_GRAMMAR_CASE) + sent.difficulty * WEIGHT_SENTENCE}
        elif sent.stats.PRON_INDEFINITE['qty'] == 1:
            return {'sentence_idx': idx_sent, 'token': sent.stats.PRON_INDEFINITE['indexes'][0], 'type': 'PRON_INDEFINITE', 'type_pt': 'um pronome indefinido', 'diff': 1 * WEIGHT_GRAMMAR_CASE + sent.difficulty * WEIGHT_SENTENCE}
        elif sent.stats.PRON_RELATIVE['qty'] == 1:
            return {'sentence_idx': idx_sent, 'token': sent.stats.PRON_RELATIVE['indexes'][0], 'type': 'PRON_RELATIVE', 'type_pt': 'um pronome relativo', 'diff': 1 * WEIGHT_GRAMMAR_CASE + sent.difficulty * WEIGHT_SENTENCE}
        elif sent.stats.PRON_INTERROGATIVE['qty'] == 1:
            return {'sentence_idx': idx_sent, 'token': sent.stats.PRON_INTERROGATIVE['indexes'][0], 'type': 'PRON_INTERROGATIVE', 'type_pt': 'um pronome interrogativo', 'diff': ((4/5) * WEIGHT_GRAMMAR_CASE) + sent.difficulty * WEIGHT_SENTENCE}
        elif sent.stats.PRON_PERSONAL['qty'] == 1:
            return {'sentence_idx': idx_sent, 'token': sent.stats.PRON_PERSONAL['indexes'][0], 'type': 'PRON_PERSONAL', 'type_pt': 'um pronome pessoal', 'diff': ((1/5) * WEIGHT_GRAMMAR_CASE) + sent.difficulty * WEIGHT_SENTENCE}
        else:
            {}

def produceGprontype(number_questions, force_diff, my_text, prons_unique):
    if force_diff == 'DIFF':
        prons_unique.sort(key = lambda x: x['diff'], reverse = True)
    elif force_diff == 'EASY':
        prons_unique.sort(key = lambda x: x['diff'], reverse = False)
    elif force_diff == 'RANDOM':
        random.shuffle(prons_unique)

    questions = utils_algorithms.produceGroupsoOf4(number_questions, prons_unique, 'unique', my_text)

    mc_questions = buildWhichType(questions, my_text, 'g_prontype')

    return mc_questions

def dettype(sent, idx_sent):
    if sent.stats.DET['qty'] == 1:
        if sent.stats.DET_ARTICLE_DEFINITE['qty'] == 1:
            return {'sentence_idx': idx_sent, 'token': sent.stats.DET_ARTICLE_DEFINITE['indexes'][0], 'type': 'DET_ARTICLE_DEFINITE', 'type_pt': 'um determinante artigo definido', 'diff': 1/5 * WEIGHT_GRAMMAR_CASE + sent.difficulty * WEIGHT_SENTENCE}
        elif sent.stats.DET_ARTICLE_INDEFINITE['qty'] == 1:
            return {'sentence_idx': idx_sent, 'token': sent.stats.DET_ARTICLE_INDEFINITE['indexes'][0], 'type': 'DET_ARTICLE_INDEFINITE', 'type_pt': 'um determinante artigo indefinido', 'diff': 1/5 * WEIGHT_GRAMMAR_CASE + sent.difficulty * WEIGHT_SENTENCE}
        elif sent.stats.DET_POSSESSIVE['qty'] == 1:
            return {'sentence_idx': idx_sent, 'token': sent.stats.DET_POSSESSIVE['indexes'][0], 'type': 'DET_POSSESSIVE', 'type_pt': 'um determinante possessivo', 'diff': 2/5 * WEIGHT_GRAMMAR_CASE + sent.difficulty * WEIGHT_SENTENCE}
        elif sent.stats.DET_DEMONSTRATIVE['qty'] == 1:
            return {'sentence_idx': idx_sent, 'token': sent.stats.DET_DEMONSTRATIVE['indexes'][0], 'type': 'DET_DEMONSTRATIVE', 'type_pt': 'um determinante demonstrativo', 'diff': 3/5 * WEIGHT_GRAMMAR_CASE + sent.difficulty * WEIGHT_SENTENCE}
        elif sent.stats.DET_INDEFINITE['qty'] == 1:
            return {'sentence_idx': idx_sent, 'token': sent.stats.DET_INDEFINITE['indexes'][0], 'type': 'DET_INDEFINITE', 'type_pt': 'um determinante indefinido', 'diff': 1 * WEIGHT_GRAMMAR_CASE + sent.difficulty * WEIGHT_SENTENCE}
        elif sent.stats.DET_RELATIVE['qty'] == 1:
            return {'sentence_idx': idx_sent, 'token': sent.stats.DET_RELATIVE['indexes'][0], 'type': 'DET_RELATIVE', 'type_pt': 'um determinante relativo', 'diff': 1 * WEIGHT_GRAMMAR_CASE + sent.difficulty * WEIGHT_SENTENCE}
        elif sent.stats.DET_INTERROGATIVE['qty'] == 1:
            return {'sentence_idx': idx_sent, 'token': sent.stats.DET_INTERROGATIVE['indexes'][0], 'type': 'DET_INTERROGATIVE', 'type_pt': 'um determinante interrogativo', 'diff': 4/5 * WEIGHT_GRAMMAR_CASE + sent.difficulty * WEIGHT_SENTENCE}
        pass

def produceGdettype(number_questions, force_diff, my_text, dets_unique):
    if force_diff == 'DIFF':
        dets_unique.sort(key = lambda x: x['diff'], reverse = True)
    elif force_diff == 'EASY':
        dets_unique.sort(key = lambda x: x['diff'], reverse = False)
    elif force_diff == 'RANDOM':
        random.shuffle(dets_unique)

    questions = utils_algorithms.produceGroupsoOf4(number_questions, dets_unique, 'unique', my_text)

    mc_questions = buildWhichType(questions, my_text, 'g_dettype')

    return mc_questions

def adverbtype(sent, idx_sent):
    if sent.stats.ADV['qty'] == 1:
        if sent.stats.ADV_MODE['qty'] == 1:
            return {'sentence_idx': idx_sent, 'token': sent.stats.ADV_MODE['indexes'][0], 'type': 'ADV_MODE', 'type_pt': 'um advérbio com valor de modo', 'diff': (3/7) * WEIGHT_GRAMMAR_CASE + sent.difficulty * WEIGHT_SENTENCE}
        elif sent.stats.ADV_TIME['qty'] == 1:
            return {'sentence_idx': idx_sent, 'token': sent.stats.ADV_TIME['indexes'][0], 'type': 'ADV_TIME', 'type_pt': 'um advérbio com valor de tempo', 'diff': (2/7) * WEIGHT_GRAMMAR_CASE + sent.difficulty * WEIGHT_SENTENCE}
        elif sent.stats.ADV_LOCAL['qty'] == 1:
            return {'sentence_idx': idx_sent, 'token': sent.stats.ADV_LOCAL['indexes'][0], 'type': 'ADV_LOCAL', 'type_pt': 'um advérbio com valor de lugar', 'diff': (2/7) * WEIGHT_GRAMMAR_CASE + sent.difficulty * WEIGHT_SENTENCE}
        elif sent.stats.ADV_DEGREE['qty'] == 1:
            return {'sentence_idx': idx_sent, 'token': sent.stats.ADV_DEGREE['indexes'][0], 'type': 'ADV_DEGREE', 'type_pt': 'um advérbio com valor de quantidade e grau', 'diff': (4/7) * WEIGHT_GRAMMAR_CASE + sent.difficulty * WEIGHT_SENTENCE}
        elif sent.stats.ADV_AFFIRMATION['qty'] == 1:
            return {'sentence_idx': idx_sent, 'token': sent.stats.ADV_AFFIRMATION['indexes'][0], 'type': 'ADV_AFFIRMATION', 'type_pt': 'um advérbio com valor de afirmação', 'diff': (1/7) * WEIGHT_GRAMMAR_CASE + sent.difficulty * WEIGHT_SENTENCE}
        elif sent.stats.ADV_NEGATION['qty'] == 1:
            return {'sentence_idx': idx_sent, 'token': sent.stats.ADV_NEGATION['indexes'][0], 'type': 'ADV_NEGATION', 'type_pt': 'um advérbio com valor de negação', 'diff': (1/7) * WEIGHT_GRAMMAR_CASE + sent.difficulty * WEIGHT_SENTENCE}
        elif sent.stats.ADV_INCLUSION['qty'] == 1:
            return {'sentence_idx': idx_sent, 'token': sent.stats.ADV_INCLUSION['indexes'][0], 'type': 'ADV_INCLUSION', 'type_pt': 'um advérbio com valor de inclusão', 'diff': (5/7) * WEIGHT_GRAMMAR_CASE + sent.difficulty * WEIGHT_SENTENCE}
        elif sent.stats.ADV_EXCLUSION['qty'] == 1:
            return {'sentence_idx': idx_sent, 'token': sent.stats.ADV_EXCLUSION['indexes'][0], 'type': 'ADV_EXCLUSION', 'type_pt': 'um advérbio com valor de exclusão', 'diff': (5/7) * WEIGHT_GRAMMAR_CASE + sent.difficulty * WEIGHT_SENTENCE}
        elif sent.stats.ADV_DOUBT['qty'] == 1:
            return {'sentence_idx': idx_sent, 'token': sent.stats.ADV_DOUBT['indexes'][0], 'type': 'ADV_DOUBT', 'type_pt': 'um advérbio com valor de dúvida', 'diff': (4/7) * WEIGHT_GRAMMAR_CASE + sent.difficulty * WEIGHT_SENTENCE}
        elif sent.stats.ADV_DESIGNATION['qty'] == 1:
            return {'sentence_idx': idx_sent, 'token': sent.stats.ADV_DESIGNATION['indexes'][0], 'type': 'ADV_DESIGNATION', 'type_pt': 'um advérbio com valor de designação', 'diff': (6/7) * WEIGHT_GRAMMAR_CASE + sent.difficulty * WEIGHT_SENTENCE}
        elif sent.stats.ADV_INTERROGATIVE['qty'] == 1:
            return {'sentence_idx': idx_sent, 'token': sent.stats.ADV_INTERROGATIVE['indexes'][0], 'type': 'ADV_INTERROGATIVE', 'type_pt': 'um advérbio interrogativo', 'diff': (1/7) * WEIGHT_GRAMMAR_CASE + sent.difficulty * WEIGHT_SENTENCE}
        elif sent.stats.ADV_CONNECTIVE['qty'] == 1:
            return {'sentence_idx': idx_sent, 'token': sent.stats.ADV_CONNECTIVE['indexes'][0], 'type': 'ADV_CONNECTIVE', 'type_pt': 'um advérbio conetivo', 'diff': 1 * WEIGHT_GRAMMAR_CASE + sent.difficulty * WEIGHT_SENTENCE}
        elif sent.stats.ADV_RELATIVE['qty'] == 1:
            return {'sentence_idx': idx_sent, 'token': sent.stats.ADV_RELATIVE['indexes'][0], 'type': 'ADV_RELATIVE', 'type_pt': 'um advérbio relativo', 'diff': 1 * WEIGHT_GRAMMAR_CASE + sent.difficulty * WEIGHT_SENTENCE}
    else:
        {}

def produceGadverbstype(number_questions, force_diff, my_text, adverbs_unique):

    if force_diff == 'DIFF':
        adverbs_unique.sort(key = lambda x: x['diff'], reverse = True)
    elif force_diff == 'EASY':
        adverbs_unique.sort(key = lambda x: x['diff'], reverse = False)
    elif force_diff == 'RANDOM':
        random.shuffle(adverbs_unique)

    questions = utils_algorithms.produceGroupsoOf4(number_questions, adverbs_unique, 'unique', my_text)

    mc_questions = buildWhichType(questions, my_text, 'g_adverbstype')

    return mc_questions


def buildWhichType(questions, my_text, type_question):
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

        stat_text = 'Assinale a única frase que contém ' + q[0]['type_pt'] + '.'

        #changed!
        question_diff = q[0]['diff'] * 0.6 + ((q[1]['diff'] + q[2]['diff'] + q[3]['diff']) / 3) * 0.4

        key_uuid = uuid.uuid1()
        new_mc_question = mcquestion.McQuestion(
            uuid.uuid1(),
            type_question, 
            key_uuid,
            stat_text, 
            [{'option_id': key_uuid, 'text':key_text}, 
            {'option_id': uuid.uuid1(), 'text':dist1_text},
            {'option_id': uuid.uuid1(), 'text':dist2_text}, 
            {'option_id': uuid.uuid1(), 'text':dist3_text}],
            question_diff)
        mc_questions.append(new_mc_question)

    #NEED TO ORDER AGAIN
    mc_questions.sort(key = lambda x: x.diff, reverse = True)

    return mc_questions

def buildMc3types(questions, my_text):

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

        stat_text = 'Assinale a frase em que a letra "a" é ' + q[0]['type_tp'] + '.' + "\n"

        #changed!
        question_diff = q[0]['diff'] * 0.6 + ((q[1]['diff'] + q[2]['diff'] + q[3]['diff']) / 3) * 0.4

        key_uuid = uuid.uuid1()
        new_mc_question = mcquestion.McQuestion(
            uuid.uuid1(),
            'g_prepdetpron', 
            key_uuid,
            stat_text, 
            [{'option_id': key_uuid, 'text':key_text}, 
            {'option_id': uuid.uuid1(), 'text':dist1_text},
            {'option_id': uuid.uuid1(), 'text':dist2_text}, 
            {'option_id': uuid.uuid1(), 'text':dist3_text}],
            question_diff)
        mc_questions.append(new_mc_question)

    #NEED TO ORDER AGAIN
    mc_questions.sort(key = lambda x: x.diff, reverse = True)

    return mc_questions


