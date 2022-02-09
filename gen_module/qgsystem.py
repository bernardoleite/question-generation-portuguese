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
import os
import copy
sys.path.insert(0, 'utils')
import utils_algorithms

import verbs

import readingComprehension
import pronounReference
import grammarSeqs
import grammarVerbs
import grammarTypes

from pathlib import Path
from difflib import SequenceMatcher

TYPE_QUESTION = 0
NUMBER_QUESTIONS = 1
DIFF_QUESTION = 2

NR_TYPE = 0
POSITION = 1

class QgSystem:
    def __init__(self):
        print("QgSystem has started!")

    my_text = 'NONE'
    list_requests = 'NONE'

    def submitRequests(self, new_requests, list_rc, nr_quest):
        self.list_requests = new_requests

        grammar_questions = []
        rc_questions = []
        pronref_questions = []

        for group_requests in self.list_requests:
            if group_requests['type'] == 'grammar':
                grammar_questions = self.produceGrammar(group_requests, copy.deepcopy(self.my_text))
                #self.writeQuestionsFile(group_requests['type'], grammar_questions)
            elif group_requests['type'] == 'reading_comprehension':
                rc_questions = self.produceReadingC(group_requests, copy.deepcopy(self.my_text), list_rc, nr_quest)
                #self.writeQuestionsFile(group_requests['type'], rc_questions)
            elif group_requests['type'] == 'pronoun_reference':
                pronref_questions = self.producePronounReference(group_requests, copy.deepcopy(self.my_text))
                #self.writeQuestionsFile(group_requests['type'], pronref_questions)
            else:
                pass

        if len(grammar_questions) > 0 or len(rc_questions) > 0 or len(pronref_questions) > 0:
            return {'grammar': grammar_questions, 'rc': rc_questions, 'pronref':pronref_questions}
        else:
            return False

    def writeQuestionsFile(self, type_questions, questions):
        if not os.path.exists('gen_module/results'):
            os.makedirs('gen_module/results')
            os.makedirs('gen_module/results/reading_comprehension')
            os.makedirs('gen_module/results/grammar')
            os.makedirs('gen_module/results/pronoun_reference')

        if type_questions == 'reading_comprehension':
            file_syntax = open("gen_module/results/reading_comprehension/syntax.txt", "w", encoding='utf8')
            file_sem = open("gen_module/results/reading_comprehension/semantic.txt", "w", encoding='utf8')
            file_dep = open("gen_module/results/reading_comprehension/dependency.txt", "w", encoding='utf8')
            file_relative_pronoun = open("gen_module/results/reading_comprehension/relative_pron.txt", "w", encoding='utf8')
            file_con = open("gen_module/results/reading_comprehension/connectors.txt", "w", encoding='utf8') 
            for q in questions:
                if q.fact_type == 'syntax':
                    file_syntax.write(q.getQuestion())
                elif q.fact_type == 'sem':
                    file_sem.write(q.getQuestion())
                elif q.fact_type == 'dep':
                    file_dep.write(q.getQuestion())
                elif q.fact_type == 'relative_pronoun':
                    file_relative_pronoun.write(q.getQuestion())
                elif q.fact_type == 'connectors':
                    file_con.write(q.getQuestion())
                else:
                    pass
            file_syntax.close()
            file_sem.close()
            file_dep.close()
            file_relative_pronoun.close()
            file_con.close()

        elif type_questions == 'grammar':
            file = open("gen_module/results/grammar/grammar.txt", "w", encoding='utf8') 
            for q in questions:
                file.write(q.getQuestion())
            file.close()

        elif type_questions == 'pronoun_reference':
            file = open("gen_module/results/pronoun_reference/pronoun_reference.txt", "w", encoding='utf8') 
            for q in questions:
                file.write(q.getQuestion())
            file.close()

    def submitFile(self, file_name):
        self.my_text = mytext.MyText(file_name)
        self.my_text.preProcess()
        return 1

    def submitText(self, text):
        self.my_text = mytext.MyText('none', text)
        result = self.my_text.preProcess()

        if result == -1:
            return -1
        else:
            return 1
    
    def create_structs(self, my_text):
        sents_size = []
        prep_det_pron = []
        conjs_unique = []
        prons_unique = []
        adverbs_unique = []
        dets_unique = []
        sents_options = []
        verbs_terms = []
        simple_complex = []
        verbs_terms_filtered = []

        for idx_sent, sent in enumerate(my_text.textStruct):
            is_declarative = sent.checkIfDeclarative() # check if sentence contains '--', '?', '!', '...'

            #g_sequence
            if is_declarative == 1 and len(sent.tagSent) >= 3 and sent.stats.PUNCT_COMMA['qty'] == 0: # it is declarative and len >= 3, probably questionable
                sents_size.append(len(sent.tokens))
            else:
                sents_size.append(-1)

            #g_prepdetpron
            elem_prepdetpron = grammarTypes.prepdetpron(sent, idx_sent)
            if is_declarative == 1 and len(sent.tagSent) >= 3 and bool(elem_prepdetpron) == True:
                prep_det_pron.append(elem_prepdetpron)

            #g_conjtype
            conj_unique = grammarTypes.conjtype(sent, idx_sent)
            if is_declarative == 1 and len(sent.tagSent) >= 3 and bool(conj_unique) == True:
                conjs_unique.append(conj_unique)

            #g_prontype
            pron_type = grammarTypes.prontype(sent, idx_sent)
            if is_declarative == 1 and len(sent.tagSent) >= 3 and bool(pron_type) == True:
                prons_unique.append(pron_type)

            #g_adverbtype
            adverb_unique = grammarTypes.adverbtype(sent, idx_sent)
            if is_declarative == 1 and len(sent.tagSent) >= 3 and bool(adverb_unique) == True:
                adverbs_unique.append(adverb_unique)

            #g_adverbtype
            det_unique = grammarTypes.dettype(sent, idx_sent)
            if is_declarative == 1 and len(sent.tagSent) >= 3 and bool(det_unique) == True:
                dets_unique.append(det_unique)

            sent_options = grammarVerbs.has2Verbs(sent, idx_sent)
            if is_declarative == 1 and len(sent.tagSent) >= 3 and bool(sent_options) == True:
                sents_options.append(sent_options)

            verb_term = grammarVerbs.produceVerbTerms(sent, idx_sent)
            if bool(verb_term) == True:
                verbs_terms.append(verb_term)

            isSimple = grammarVerbs.simplecomplex(sent, idx_sent)
            if is_declarative == 1 and len(sent.tagSent) >= 3 and bool(isSimple) == True:
                simple_complex.append(isSimple)

            verb_term_filtered = grammarVerbs.produceVerbTerms(sent, idx_sent)
            if is_declarative == 1 and len(sent.tagSent) >= 3 and bool(verb_term_filtered) == True:
                verbs_terms_filtered.append(verb_term_filtered)

        return {
        'sents_size': sents_size, 
        'prep_det_pron': prep_det_pron, 
        'conjs_unique': conjs_unique, 
        'prons_unique': prons_unique, 
        'adverbs_unique': adverbs_unique,
        'dets_unique': dets_unique,
        'sents_options': sents_options,
        'verbs_terms': verbs_terms,
        'verbs_terms_filtered': verbs_terms_filtered,
        'simple_complex': simple_complex
        }

    def produceGrammar(self, group_requests, my_text):
        questions = []
        grammar_requests = group_requests['questions_requests']

        my_structs = self.create_structs(my_text)

        for request in grammar_requests:
            if request[TYPE_QUESTION] == 'g_sequence':
                mc_Gsequence = grammarSeqs.produceGsequence(request[NUMBER_QUESTIONS], request[DIFF_QUESTION], self.my_text, my_structs['sents_size'])
                if len(mc_Gsequence) > 0: questions.append(mc_Gsequence)

            elif request[TYPE_QUESTION] == 'g_prepdetpron':
                mc_Gprepdetpron = grammarTypes.produceGprepdetpron(request[NUMBER_QUESTIONS], request[DIFF_QUESTION], self.my_text, my_structs['prep_det_pron'])
                if len(mc_Gprepdetpron) > 0: questions.append(mc_Gprepdetpron)

            elif request[TYPE_QUESTION] == 'g_verbstype':
                mc_Gverbstype = grammarVerbs.produceGverbstype(request[NUMBER_QUESTIONS], request[DIFF_QUESTION], self.my_text, my_structs['sents_options'])
                if len(mc_Gverbstype) > 0: questions.append(mc_Gverbstype)
                
            elif request[TYPE_QUESTION] == 'g_adverbstype':
                mc_Gadverbstype = grammarTypes.produceGadverbstype(request[NUMBER_QUESTIONS], request[DIFF_QUESTION], self.my_text, my_structs['adverbs_unique'])
                if len(mc_Gadverbstype) > 0: questions.append(mc_Gadverbstype)

            elif request[TYPE_QUESTION] == 'g_dettype':
                mc_Gdettype = grammarTypes.produceGdettype(request[NUMBER_QUESTIONS], request[DIFF_QUESTION], self.my_text, my_structs['dets_unique'])
                if len(mc_Gdettype) > 0: questions.append(mc_Gdettype)

            elif request[TYPE_QUESTION] == 'g_prontype':
                mc_Gprontype = grammarTypes.produceGprontype(request[NUMBER_QUESTIONS], request[DIFF_QUESTION], self.my_text, my_structs['prons_unique'])
                if len(mc_Gprontype) > 0: questions.append(mc_Gprontype)

            elif request[TYPE_QUESTION] == 'g_conjtype':
                mc_Gconjtype = grammarTypes.produceGconjtype(request[NUMBER_QUESTIONS], request[DIFF_QUESTION], self.my_text, my_structs['conjs_unique'])
                if len(mc_Gconjtype) > 0: questions.append(mc_Gconjtype)

            elif request[TYPE_QUESTION] == 'g_verbsmood':
                mc_Gverbsmood = grammarVerbs.produceGverbsmood(request[NUMBER_QUESTIONS], request[DIFF_QUESTION], self.my_text, my_structs['verbs_terms'])
                if len(mc_Gverbsmood) > 0: questions.append(mc_Gverbsmood)

            elif request[TYPE_QUESTION] == 'g_completeverb':
                mc_Gcompleteverb = grammarVerbs.produceGcompleteverb(request[NUMBER_QUESTIONS], request[DIFF_QUESTION], self.my_text, my_structs['verbs_terms_filtered'])
                if len(mc_Gcompleteverb) > 0: questions.append(mc_Gcompleteverb)

            elif request[TYPE_QUESTION] == 'g_verbfeats':
                mc_Gverbsfeats = grammarVerbs.produceGverbfeats(request[NUMBER_QUESTIONS], request[DIFF_QUESTION], self.my_text, my_structs['verbs_terms'])
                if len(mc_Gverbsfeats) > 0: questions.append(mc_Gverbsfeats)

            elif request[TYPE_QUESTION] == 'g_simplecomplex':
                mc_Gsimplecomplex = grammarVerbs.produceGsimplecomplex(request[NUMBER_QUESTIONS], request[DIFF_QUESTION], self.my_text, my_structs['simple_complex'])
                if len(mc_Gsimplecomplex) > 0: questions.append(mc_Gsimplecomplex)
            else:
                pass

        #self.writeQuestionsFile("grammar", utils_algorithms.merge_sublists(questions))
        return utils_algorithms.merge_sublists(questions)

    def orderByDifficulty(self, all_questions, diff_request):
        if diff_request == 'DIFF':
            all_questions.sort(key = lambda x: x.diff, reverse = True)
        elif diff_request == 'EASY':
            all_questions.sort(key = lambda x: x.diff, reverse = False)
        else:
            pass
        return all_questions


    def produceReadingC(self, group_requests, my_text, list_rc, nr_quest):
        questions = []

        questions_syntax = []
        questions_semantic = []
        questions_pronoun = []
        questions_dependency = []
        questions_connectors = []

        readingc_requests = group_requests['questions_requests']
        diff_request = readingc_requests[0][2]

        for idx_sent, sent in enumerate(my_text.textStruct):

            is_declarative = sent.checkIfDeclarative() # check if sentence does not contain '--', '?', '!', '...'
            
            if is_declarative == 1 and len(sent.tagSent) >= 3: # it is declarative and len >= 3, probably questionable
                my_sent = sent # copy.deepcopy(sent)
                questions_syntax = readingComprehension.produceSyntaxQuestions(my_sent, my_text)
                questions_dependency = readingComprehension.produceDependencyQuestions(my_sent, my_text)
                questions_pronoun = readingComprehension.producePronounQuestions(my_sent, my_text)
                questions_connectors = readingComprehension.produceConnectorsQuestions(my_sent, my_text)
                questions_semantic = readingComprehension.produceSemanticQuestions(my_sent, my_text)

            else: # not questionable, need to clear to not repeat
                questions_syntax.clear()
                questions_semantic.clear()
                questions_dependency.clear()
                questions_pronoun.clear()
                questions_connectors.clear()

            questions.append(questions_syntax)
            questions.append(questions_semantic)
            questions.append(questions_pronoun)
            questions.append(questions_dependency)
            questions.append(questions_connectors)

        questions = utils_algorithms.merge_sublists(questions)

        #post_processing
        questions = self.post_processing(questions)

        #filter questions
        questions = self.filterRcQuest(questions, list_rc, nr_quest)

        #order by difficulty
        questions = self.orderByDifficulty(questions, diff_request)

        return questions

    #originally at app.py
    def filterRcQuest(self, rc_questions, list_rc, nr_quest):
        new_rc_questions = []

        rc_facts_types = ['dep_facts', 'relative_pronoun_facts', 'syntax_facts']
        rc_whenwhere_types = ['sem_where', 'sem_when', 'connectors_when', 'relative_pronoun_when', 'relative_pronoun_where', 'syntax_where', 'syntax_when']
        rc_how_types = ['sem_how', 'dep_how', 'relative_pronoun_how']
        rc_why_types = ['connectors_why']

        rc_facts = []
        rc_whenwhere = []
        rc_how = []
        rc_why = []

        for question in rc_questions:
            if question.state == "APPROVED":
                if question.fact_subtype in list_rc and question.fact_subtype in rc_facts_types  and len(rc_facts) < nr_quest:
                    rc_facts.append(question)
                elif question.fact_subtype in list_rc and question.fact_subtype in rc_whenwhere_types and len(rc_whenwhere) < nr_quest:
                    rc_whenwhere.append(question)
                elif question.fact_subtype in list_rc and question.fact_subtype in rc_how_types and len(rc_how) < nr_quest:
                    rc_how.append(question)
                elif question.fact_subtype in list_rc and question.fact_subtype in rc_why_types and len(rc_why) < nr_quest:
                    rc_why.append(question)
                else:
                    pass

        new_rc_questions = rc_facts + rc_whenwhere + rc_how + rc_why

        return new_rc_questions

    def producePronounReference(self, group_requests, my_text):
        questions = []
        question_pron_ref = None

        pronoun_requests = group_requests['questions_requests']
        diff_request = pronoun_requests[0][2]

        for idx_sent, sent in enumerate(my_text.textStruct):

            is_declarative = sent.checkIfDeclarative()

            if is_declarative == 1 and len(sent.tagSent) >= 3:
                appositives = pronounReference.getAppositives(sent)

                if len(appositives) > 0 and idx_sent > 0 and idx_sent < len(my_text.textStruct)-1: # if sentence has appositive and it is in the middle of text
                    question_pron_ref = pronounReference.producePronRefQuestions(sent, idx_sent, appositives, my_text)

            if question_pron_ref != None:
                questions.append(question_pron_ref)
            
            question_pron_ref = None
        
        questions = self.orderByDifficulty(questions, diff_request)

        return questions

    def post_processing(self, questions):

        for q in questions:
            nr_tokens = 0

            # IF PRE-LAST ONE IS CONJ remove it
            if q.tokens_question[-2].tag == 'CONJ':
                del q.tokens_question[-2]

            produce_seq_text = []
            for idx, token in enumerate(q.tokens_question):
                
                # ADD TO SEQ IN ORDER TO REMOVE PARTS AT THE END
                produce_seq_text.append(token.text)

                #SUM NR TOKEN IF NOT GEN
                if token.token_type != 'GEN':
                    nr_tokens = nr_tokens + 1

                #PRONOUNS
                if token.tag == 'PRON' and (token.sub_tag == 'PRON_PERSONAL' or token.sub_tag == 'PRON_DEMONSTRATIVE'):
                    q.state = 'REJECTED'
                elif token.tag == 'PRON' and (token.text == 'me' or token.text == 'mim' or token.text == 'comigo' or token.text == 'te' or token.text == 'ti' or token.text == 'contigo' or token.text == 'si' or token.text == 'consigo' or token.text == 'nos' or token.text == 'vos'):
                    q.state = 'REJECTED'
                else:
                    pass

                #PUNCTS OR SYMBOLS
                if token.text == '(' or token.text == ')' or token.text == '"' or token.text == ';' or token.text == '«' or token.text == '»':
                    q.state = 'REJECTED'

                #MAÍSCULAS e MÍNISCULAS
                if q.state == 'APPROVED' and token.token_type != 'GEN' and token.tag != 'NOUN':
                    q.tokens_question[idx].text = token.text.lower()

                #Clitic
                if q.state == 'APPROVED' and token.tag == 'VERB' and len(token.words) == 2:
                    if token.words[1].upos == 'PRON' and token.words[1].text == 'lo':
                        new_verb = 'o' + ' ' + token.words[0].lemma
                        q.tokens_question[idx].text = new_verb
                    elif token.words[1].upos == 'PRON' and token.words[1].text == 'la':
                        new_verb = 'a' + ' ' + token.words[0].lemma
                        q.tokens_question[idx].text = new_verb 
                    elif token.words[1].upos == 'PRON':
                        new_verb = token.words[1].text + ' ' + token.words[0].text
                        q.tokens_question[idx].text = new_verb
                    else:
                        pass

                #VERBS IN PLURAL AFTER GEN TOKEN
                if q.state == 'APPROVED' and (q.fact_type == 'syntax' or q.fact_type == 'relative_pronoun') and token.tag == 'VERB' and len(token.words) == 1 and q.tokens_question[idx-1].token_type == 'GEN':
                    verb_tobe = False
                    if 'Person' in list(token.words[0].feats.keys()) and 'Number' in list(token.words[0].feats.keys()):
                        if token.words[0].lemma == 'ser' or token.words[0].lemma == 'haver': verb_tobe = True
                        if token.words[0].feats['Number'] == 'Plur' and verb_tobe == False:
                            new_verb = verbs.conjugateVerb(token.words[0].lemma, 'Indicativo', 'Indicativo pretÃ©rito perfeito simples', token.words[0].feats['Person'], 'Sing')
                            if new_verb != -1:
                                q.tokens_question[idx].text = new_verb
                            else:
                                pass
                    verb_tobe = False
                #'Mood' in list(token.words[0].feats.keys()) and 'Tense' in list(token.words[0].feats.keys())
                # do i need this?

            #REMOVE , TO ?
            pattern_match_unwanted = utils_algorithms.match_indexes(produce_seq_text, [','], ['?'])
            if len(pattern_match_unwanted) > 0:
                list_to_remove = max(pattern_match_unwanted, key=len)
                del q.tokens_question[list_to_remove[0]:list_to_remove[-1]]
                nr_tokens = nr_tokens - len(list_to_remove)

            # AGAIN BECAUSE IT CAN HAPPEN GIVEN THE LAST STEP
            if q.tokens_question[-2].tag == 'CONJ':
                del q.tokens_question[-2]
                nr_tokens = nr_tokens - 1

            #SIZE
            if nr_tokens < 2 or nr_tokens > 20:
                q.state = 'REJECTED'

            q.updateQuestion()

        return questions