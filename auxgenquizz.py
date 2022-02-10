def checkQuestionsSelection(result_form):
    list_requests = []

    if result_form['nr_quest'] == 'nrquest_5':
        nr_quest = 5
    elif result_form['nr_quest'] == 'nrquest_10':
        nr_quest = 10
    elif result_form['nr_quest'] == 'nrquest_20':
        nr_quest = 20
    elif result_form['nr_quest'] == 'nrquest_50':
        nr_quest = 50
    elif result_form['nr_quest'] == 'nrquest_inf':
        nr_quest = 100
    else:
        nr_quest = 100

    if result_form['diff'] == 'diff_harder':
        diff = 'DIFF'
    elif result_form['diff'] == 'diff_easier':
        diff = 'EASY'
    elif result_form['diff'] == 'diff_random':
        diff = 'RANDOM'
    else:
        diff = 'RANDOM'

    grammar_requests = {
    'type': 'grammar', 
    'questions_requests': []
    }

    rc_requests = {
    'type': 'reading_comprehension', 
    'questions_requests': []
    }

    pron_requests = {
    'type': 'pronoun_reference', 
    'questions_requests': []
    }

    if 'g_sequence' in result_form:
        grammar_requests['questions_requests'].append(['g_sequence', nr_quest, diff])
    if 'g_types' in result_form:
        grammar_requests['questions_requests'].append(['g_adverbstype', nr_quest, diff])
        grammar_requests['questions_requests'].append(['g_dettype', nr_quest, diff])
        grammar_requests['questions_requests'].append(['g_prontype', nr_quest, diff])
        grammar_requests['questions_requests'].append(['g_conjtype', nr_quest, diff])
    if 'g_prepdetpron' in result_form:
        grammar_requests['questions_requests'].append(['g_prepdetpron', nr_quest, diff])
    if 'g_verbfeats' in result_form:
        grammar_requests['questions_requests'].append(['g_verbfeats', nr_quest, diff])
    if 'g_completeverb' in result_form:
        grammar_requests['questions_requests'].append(['g_completeverb', nr_quest, diff])
    if 'g_verbsmood' in result_form:
        grammar_requests['questions_requests'].append(['g_verbsmood', nr_quest, diff])
    if 'g_verbstype' in result_form:
        grammar_requests['questions_requests'].append(['g_verbstype', nr_quest, diff])
    if 'g_simplecomplex' in result_form:
        grammar_requests['questions_requests'].append(['g_simplecomplex', nr_quest, diff])

    if 'rc_facts' in result_form or 'rc_whenwhere' in result_form or 'rc_how' in result_form or 'rc_why' in result_form:
        rc_requests['questions_requests'].append(['rc_factualsyntax', nr_quest, diff])
        rc_requests['questions_requests'].append(['rc_factualdependency', nr_quest, diff])
        rc_requests['questions_requests'].append(['rc_factualsemantic', nr_quest, diff])
        rc_requests['questions_requests'].append(['relative_pronoun', nr_quest, diff])
        rc_requests['questions_requests'].append(['connectors', nr_quest, diff])

    list_rc = getRc(result_form)

    if 'pronoun_reference' in result_form:
        pron_requests['questions_requests'].append(['pronoun_reference', nr_quest, diff])

    if len(grammar_requests['questions_requests']) == 0 and len(rc_requests['questions_requests']) == 0 and len(pron_requests['questions_requests']) == 0:
        return -1, list_rc, nr_quest

    if len(grammar_requests['questions_requests']) > 0:
        list_requests.append(grammar_requests)

    if len(rc_requests['questions_requests']) > 0:
        list_requests.append(rc_requests)

    if len(pron_requests['questions_requests']) > 0:
        list_requests.append(pron_requests)
    
    return list_requests, list_rc, nr_quest


def getRc(result_form):
    list_rc = []

    if 'rc_facts' in result_form:
        list_rc.extend(('dep_facts', 'relative_pronoun_facts', 'syntax_facts'))
    if 'rc_whenwhere' in result_form:
        list_rc.extend(('sem_where', 'sem_when', 'connectors_when', 'relative_pronoun_when', 'relative_pronoun_where', 'syntax_where', 'syntax_when'))
    if 'rc_how' in result_form:
        list_rc.extend(('sem_how', 'dep_how', 'relative_pronoun_how'))
    if 'rc_why' in result_form:
        list_rc.append('connectors_why')

    return list_rc