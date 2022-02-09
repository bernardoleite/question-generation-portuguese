DET_ARTICLE_DEFINITE = ['o','a','os','as']
DET_ARTICLE_INDEFINITE = ['um','uma','uns','umas']
DET_POSSESSIVE = ['meu','teu','seu','nosso','vosso','seu',
                'minha', 'tua', 'sua','nossa', 'vossa', 'sua',
                'meus', 'teus', 'seus', 'nossos', 'vossos', 'seus',
                'minhas', 'tuas', 'suas', 'nossas', 'vossas', 'suas']
DET_DEMONSTRATIVE = ['este', 'esse', 'aquele', 'esta', 'essa', 'aquela', 'estes', 'esses', 'aqueles', 'estas', 'essas', 'aquelas']
DET_INDEFINITE = ['certo', 'outro', 'certa', 'outra', 'certos', 'outros', 'certas', 'outras']
DET_RELATIVE = ['cujo', 'cuja', 'cujos', 'cujas']
DET_INTERROGATIVE = ['qual', 'quais', 'que']


# repete qual, quais, que, quem, onde
PRON_POSSESSIVE = ['meu','teu','seu','nosso','vosso','seu',
                'minha', 'tua', 'sua','nossa', 'vossa', 'sua',
                'meus', 'teus', 'seus', 'nossos', 'vossos', 'seus',
                'minhas', 'tuas', 'suas', 'nossas', 'vossas', 'suas']
PRON_DEMONSTRATIVE = ['este', 'esse', 'aquele', 'esta', 'essa', 'aquela', 'estes', 'esses', 'aqueles', 'estas', 'essas', 'aquelas', 'o', 'a', 'os', 'as', 'isto', 'isso', 'aquilo']
PRON_INDEFINITE = ['algum', 'nenhum', 'todo', 'muito', 'pouco', 'tanto','outro','alguma', 'nenhuma', 'toda', 'muita', 'pouca', 'tanta', 'outra', 'qualquer', 'alguns', 'nenhuns', 'todos', 'muitos', 'poucos', 'tantos', 'outros', 'algumas', 'nenhumas', 'todas', 'muitas', 'poucas', 'tantas', 'outras', 'quaisquer', 'alguém', 'ninguém', 'outrem', 'tudo', 'nada', 'algo', 'cada']# algo, cada pertencem?
PRON_RELATIVE = ['qual', 'quais', 'que', 'quem'] #onde
PRON_INTERROGATIVE = ['quanto', 'qual', 'quanta', 'quantos', 'quais','quantas', 'que', 'quê', 'quem', 'porque', 'porquê', 'como', 'onde' ]


#repete 'onde' e 'como'
ADV_MODE = ['assim', 'bem', 'debalde', 'mal', 'depressa', 'devagar', 'alegremente', 'simpaticamente', 'agradavelmente', 'fortemente', 'velozmente', 'carinhosamente']
ADV_TIME = ['agora', 'ainda', 'amanhã', 'anteontem', 'antigamente', 'cedo', 'então', 'frequentemente', 'hoje', 'já', 'jamis', 'nunca', 'ontem', 'sempre', 'tarde']
ADV_LOCAL = ['abaixo', 'acima', 'acolá', 'adiante', 'aí', 'além', 'algures', 'ali', 'aquém', 'aqui', 'atrás', 'cá', 'defronte', 'dentro', 'fora', 'junto', 'lá', 'longe', 'perto']
ADV_DEGREE = ['bastante', 'demais', 'demasiadamente', 'deveras', 'extremamente', 'mais', 'menos', 'muito', 'pouco', 'quase', 'tanto', 'tão']
ADV_AFFIRMATION = ['sim', 'certamente', 'decerto', 'efetivamente', 'realmente']
ADV_NEGATION = ['não']
ADV_INCLUSION = ['até', 'inclusivamente', 'mesmo', 'também']
ADV_EXCLUSION = ['apenas', 'exceto', 'exclusivamente', 'salvo', 'senão', 'só', 'somente', 'unicamente']
ADV_DOUBT = ['provavelmente', 'possivelmente', 'talvez', 'porventura', 'acaso', 'quiçá']
ADV_DESIGNATION = ['eis']
ADV_INTERROGATIVE = ['aonde', 'donde', 'quando', 'porquê', 'porque'] #falta como e onde
ADV_CONNECTIVE = ['porém', 'contudo', 'todavia', 'primeiramente', 'seguidamente', 'consequentemente']
ADV_RELATIVE = ['onde', 'como'] #falta onde e como

#repete 'pois'
CCONJ_COPULATIVE = ['e','nem']
CCONJ_ADVERSATIVE = ['mas', 'porém', 'todavia', 'contudo']
CCONJ_DISJUNCTIVE = ['ou', 'quer']
CCONJ_CONCLUSIVE = ['logo', 'portanto'] #falta pois
CCONJ_EXPLICATIVE = ['que', 'porquanto'] #falta pois

#repete 'que' e 'como' e 'se'
SCONJ_COMPLETIVE = [''] #falta que
SCONJ_CAUSAL = ['porque', 'pois', 'porquanto'] #falta que,como
SCONJ_FINAL = ['para'] #falta que
SCONJ_TEMPORAL = ['quando', 'enquanto', 'mal', 'apenas'] #falta que,como
SCONJ_CONCESSIVE = ['embora', 'conquanto'] #falta que
SCONJ_CONDITIONAL = [''] #falta se
SCONJ_COMPARATIVE = ['conforme', 'segundo', 'qual', 'quanto'] #falta que,como
SCONJ_CONSECUTIVE = [''] #falta que

#pilha depende do contexto?
NOUN_COLLECTIVE = ['alcateia', 'armada', 'arquipélago', 'atilho', 'banda', 'bando', 'batalhão', 'cacho', 'cáfila', 'cambada', 'cancioneiro', 'caravana', 'cardume', 'choldra', 'chorrilho', 'chusma', 'classe', 'constelação', 'corja', 'coro', 'elenco', 'enxame', 'enxoval', 'esquadra', 'esquadrilha', 'exército', 'falange', 'fato', 'frota', 'galeria', 'girândola', 'horda', 'junta', 'legião', 'magote', 'malta', 'manada', 'matilha', 'matula', 'molho', 'multidão', 'minhada', 'olival', 'pinhal', 'plantel', 'plêiade', 'pomar', 'praga', 'quadrinha', 'ramalhete', 'rebanho', 'récua', 'renque', 'réstia', 'revoada', 'roda', 'romanceiro', 'súcia', 'talha', 'vara', 'assembleia', 'equipa', 'miudagem', 'orquestra', 'povo', 'quadrilha', 'arvoredo', 'bananal', 'carvalhal', 'montado','souto', 'vinhedo', 'antologia','cordilheira', 'estrofe', 'feixe', 'pilha']

VERB_COPULATIVE = ['ser', 'estar', 'ficar', 'permanecer', 'continuar', 'andar', 'tornar', 'revelar']

#VERB_TRANSITIVE_DIRECT = ['ler', 'fazer', 'querer', 'quebrar', 'ter', 'causar', 'comprar', 'derrubar', 'começar', 'atropelar', 'perder', 'cortar', 'comer', 'ouvir', 'destruir', 'abandonar', 'abençoar', 'aborrecer', 'abraçar', 'acompanhar', 'acusar', 'admirar', 'adorar', 'alegrar', 'ameaçar', 'amolar', 'amaparar', 'auxiliar', 'castigar', 'condenar', 'conhecer', 'conservar', 'convidar', 'defender', 'eleger', 'estimar', 'humilhar', 'namorar', 'ouvir', 'prejudicar', 'prezar', 'proteger', 'respeitar', 'socorrer', 'suportar', 'visitar', 'ver', 'trazer']

#VERB_TRANSITIVE_INDIRECT = ['necessitar', 'saber', 'acreditar', 'obedecer', 'desobedecer' 'precisar', 'gostar', 'conversar', 'duvidar', 'responder', 'concordar', 'lembrar', 'simpatizar', 'antipatizar', 'ingressar', 'comparecer', 'suceder', 'consistir', 'ir', 'falar', 'telefonar', 'agradar']

def whichNOUN(word):
    if word.text.lower() in NOUN_COLLECTIVE:
        return 'NOUN_COLLECTIVE', {'class': 'nome', 'subclass': 'nome coletivo'}
    else:
        return 'NOUN_COMMON', {'class': 'nome', 'subclass': 'nome comum'}

def whichADJ(word):
    if 'NumType' in word.feats:
        if word.feats['NumType'] == 'Ord':
            return 'ADJ_NUMERAL',{'class': 'adjetivo', 'subclass': 'adjetivo numeral'}
    else:
        return 'ADJ_QUALIFICATIVE',{'class': 'adjetivo', 'subclass': 'adjetivo qualificativo'}

def whichVERB(word):
    if word.lemma != None and word.lemma.lower() in VERB_COPULATIVE:
        return 'VERB_COPULATIVE',{'class': 'verbo', 'subclass': 'verbo copulativo'}
    else:
        return 'VERB_MAIN',{'class': 'verbo', 'subclass': 'verbo principal'}

def whichAUX(word):
    return 'VERB_AUXILIARY',{'class': 'verbo', 'subclass': 'verbo auxiliar'}

def whichADV(word):
    if word.text.lower() in ADV_MODE:
        return 'ADV_MODE', {'class': 'advérbio', 'subclass': 'advérbio com valor de modo'}
    elif word.text.lower() in ADV_TIME:
        return 'ADV_TIME', {'class': 'advérbio', 'subclass': 'advérbio com valor de tempo'}
    elif word.text.lower() in ADV_LOCAL:
        return 'ADV_LOCAL', {'class': 'advérbio', 'subclass': 'advérbio com valor de lugar'}
    elif word.text.lower() in ADV_DEGREE:
        return 'ADV_DEGREE', {'class': 'advérbio', 'subclass': 'advérbio com valor de quantidade e grau'}
    elif word.text.lower() in ADV_AFFIRMATION:
        return 'ADV_AFFIRMATION', {'class': 'advérbio', 'subclass': 'advérbio com valor de afirmação'}
    elif word.text.lower() in ADV_NEGATION:
        return 'ADV_NEGATION', {'class': 'advérbio', 'subclass': 'advérbio com valor de negação'}
    elif word.text.lower() in ADV_INCLUSION:
        return 'ADV_INCLUSION', {'class': 'advérbio', 'subclass': 'advérbio com valor de inclusão'}
    elif word.text.lower() in ADV_EXCLUSION:
        return 'ADV_EXCLUSION', {'class': 'advérbio', 'subclass': 'advérbio com valor de exclusão'}
    elif word.text.lower() in ADV_DOUBT:
        return 'ADV_DOUBT', {'class': 'advérbio', 'subclass': 'advérbio com valor de dúvida'}
    elif word.text.lower() in ADV_DESIGNATION:
        return 'ADV_DESIGNATION', {'class': 'advérbio', 'subclass': 'advérbio com valor de designação'}
    elif word.text.lower() in ADV_INTERROGATIVE:
        return 'ADV_INTERROGATIVE', {'class': 'advérbio', 'subclass': 'advérbio interrogativo'}
    elif word.text.lower() in ADV_CONNECTIVE:
        return 'ADV_CONNECTIVE', {'class': 'advérbio', 'subclass': 'advérbio conetivo'}
    elif word.text.lower() in ADV_RELATIVE:
        return 'ADV_RELATIVE', {'class': 'advérbio', 'subclass': 'advérbio relativo'}
    else:
        return 'UNIDENTIFIED', {'class': 'advérbio', 'subclass': 'advérbio'}

def whichDET(word):
    if word.text.lower() in DET_ARTICLE_DEFINITE:
        return 'DET_ARTICLE_DEFINITE', {'class': 'determinante', 'subclass': 'determinante artigo definido'}
    elif word.text.lower() in DET_ARTICLE_INDEFINITE:
        return 'DET_ARTICLE_INDEFINITE', {'class': 'determinante', 'subclass': 'determinante artigo indefinido'}
    elif word.text.lower() in DET_POSSESSIVE:
        return 'DET_POSSESSIVE',{'class': 'determinante', 'subclass': 'determinante possessivo'}
    elif word.text.lower() in DET_DEMONSTRATIVE:
        return 'DET_DEMONSTRATIVE', {'class': 'determinante', 'subclass': 'determinante demonstrativo'}
    elif word.text.lower() in DET_INDEFINITE:
        return 'DET_INDEFINITE', {'class': 'determinante', 'subclass': 'determinante indefinido'}
    elif word.text.lower() in DET_RELATIVE:
        return 'DET_RELATIVE', {'class': 'determinante', 'subclass': 'determinante relativo'}
    elif word.text.lower() in DET_INTERROGATIVE:
        return 'DET_INTERROGATIVE', {'class': 'determinante', 'subclass': 'determinante interrogativo'}
    else:
        return 'UNIDENTIFIED', {'class': 'determinante', 'subclass': 'determinante'}

def whichPRON(word, last_element):
    if 'PronType' in word.feats and word.feats['PronType'] == 'Prs':
        return 'PRON_PERSONAL', {'class': 'pronome', 'subclass': 'pronome pessoal'}
    elif last_element == '?' and word.text.lower() in PRON_INTERROGATIVE:
        return 'PRON_INTERROGATIVE', {'class': 'pronome', 'subclass': 'pronome interrogativo'}
    elif word.text.lower() in PRON_POSSESSIVE:
        return 'PRON_POSSESSIVE', {'class': 'pronome', 'subclass': 'pronome possessivo'}
    elif word.text.lower() in PRON_DEMONSTRATIVE:
        return 'PRON_DEMONSTRATIVE', {'class': 'pronome', 'subclass': 'pronome demonstrativo'}
    elif word.text.lower() in PRON_INDEFINITE:
        return 'PRON_INDEFINITE', {'class': 'pronome', 'subclass': 'pronome indefinido'}
    elif word.text.lower() in PRON_RELATIVE:
        return 'PRON_RELATIVE', {'class': 'pronome', 'subclass': 'pronome relativo'}
    else:
        return 'UNIDENTIFIED', {'class': 'pronome', 'subclass': 'pronome'}

def whichPREP(word):
    return 'PREP_SIMPLE',{'class': 'preposição', 'subclass': 'preposição simples'}

def whichINTJ(word):
    return 'INTJ',{'class': 'interjeição', 'subclass': 'interjeição'}

def whichCCONJ(word):
    if word.text.lower() in CCONJ_COPULATIVE:
        return 'CCONJ_COPULATIVE', {'class': 'conjunção', 'subclass': 'conjunção coordenativa copulativa'}
    elif word.text.lower() in CCONJ_ADVERSATIVE:
        return 'CCONJ_ADVERSATIVE', {'class': 'conjunção', 'subclass': 'conjunção coordenativa adversativa'}
    elif word.text.lower() in CCONJ_DISJUNCTIVE:
        return 'CCONJ_DISJUNCTIVE', {'class': 'conjunção', 'subclass': 'conjunção coordenativa disjuntiva'}
    elif word.text.lower() in CCONJ_CONCLUSIVE:
        return 'CCONJ_CONCLUSIVE', {'class': 'conjunção', 'subclass': 'conjunção coordenativa conclusiva'}
    elif word.text.lower() in CCONJ_EXPLICATIVE:
        return 'CCONJ_EXPLICATIVE', {'class': 'conjunção', 'subclass': 'conjunção coordenativa explicativa'}
    else:
        return 'UNIDENTIFIED', {'class': 'conjunção', 'subclass': 'conjunção coordenativa'}

def whichSCONJ(word):
    if word.text.lower() in SCONJ_COMPLETIVE:
        return 'SCONJ_COMPLETIVE', {'class': 'conjunção', 'subclass': 'conjunção subordinativa completiva'}
    elif word.text.lower() in SCONJ_CAUSAL:
        return 'SCONJ_CAUSAL', {'class': 'conjunção', 'subclass': 'conjunção subordinativa causal'}
    elif word.text.lower() in SCONJ_FINAL:
        return 'SCONJ_FINAL', {'class': 'conjunção', 'subclass': 'conjunção subordinativa final'}
    elif word.text.lower() in SCONJ_TEMPORAL:
        return 'SCONJ_TEMPORAL', {'class': 'conjunção', 'subclass': 'conjunção subordinativa temporal'}
    elif word.text.lower() in SCONJ_CONCESSIVE:
        return 'SCONJ_CONCESSIVE', {'class': 'conjunção', 'subclass': 'conjunção subordinativa concessiva'}
    elif word.text.lower() in SCONJ_CONDITIONAL:
        return 'SCONJ_CONDITIONAL', {'class': 'conjunção', 'subclass': 'conjunção subordinativa condicional'}
    elif word.text.lower() in SCONJ_COMPARATIVE:
        return 'SCONJ_COMPARATIVE', {'class': 'conjunção', 'subclass': 'conjunção subordinativa comparativa'}
    elif word.text.lower() in SCONJ_CONSECUTIVE:
        return 'SCONJ_CONSECUTIVE',  {'class': 'conjunção', 'subclass': 'conjunção subordinativa consecutiva'}
    else:
        return 'UNIDENTIFIED',{'class': 'conjunção', 'subclass': 'conjunção subordinativa'}

def whichPUNCT(word):
    if word.text == '.':
        return 'PUNCT_FINAL', {'class': 'ponto', 'subclass': 'ponto final'}
    elif word.text == '?':
        return 'PUNCT_QUESTION', {'class': 'ponto', 'subclass': 'ponto de interrogação'}
    elif word.text == '!':
        return 'PUNCT_EXCLAMATIVE', {'class': 'ponto', 'subclass': 'ponto de exclamação'}
    elif word.text == ',':
        return 'PUNCT_COMMA', {'class': 'vírgula', 'subclass': 'vírgula'}
    elif word.text == '—' or word.text == '-' or word.text == '--' or word.text ==  '–':
        return 'PUNCT_DASH', {'class': 'travessão', 'subclass': 'travessão'}
    elif word.text == ':':
        return 'PUNCT_TWOPOINTS', {'class': 'dois pontos', 'subclass': 'dois pontos'}
    elif word.text == ';':
        return 'PUNCT_SEMICOLON', {'class': 'ponto e vírgula', 'subclass': 'ponto e vírgula'}
    elif word.text == '"' or word.text == '“' or word.text == '”':
        return 'PUNCT_QUOTATION', {'class': 'aspas', 'subclass': 'aspas'}
    elif word.text == '(' or word.text == ')':
        return 'PUNCT_PARENTHESES', {'class': 'aspas', 'subclass': 'aspas'}
    else:
        return 'UNIDENTIFIED', {'class': 'ponto', 'subclass': 'ponto'}

def whichSYM(word):
    return 'SYM',{'class': 'símbolo', 'subclass': 'símbolo'}

#does not have
def whichQNT(word):
    return 'QNT', {'class': 'quantificador', 'subclass': 'quantificador'}