import sys
sys.path.append('gen_module/')
sys.path.append('gen_module/utils')
import qgsystem
import auxgenquizz

# All Reading Comprehension question types
READING_COMP_TYPES = ['dep_facts', 'relative_pronoun_facts', 'syntax_facts', 'sem_where', 'sem_when', 'connectors_when', 'relative_pronoun_when', 'relative_pronoun_where', 'syntax_where', 'syntax_when', 'sem_how', 'dep_how', 'relative_pronoun_how', 'connectors_why']

# Example text
text_example = """
A vida de Hans mais uma vez tinha virado. Já não eram as longas navegações até aos confins dos continentes, o avançar aventuroso ao longo das costas luxuriantes e de costas desérticas, de povo em povo, de baía em baía. Agora verificava a ordem dos armazéns, o bom estado dos navios, a competência das equipagens, controlava as cargas e descargas, discutia negócios e contratos. As suas viagens iam-se tornando rápidas e espaçadas.
E Hans compreendeu que, como todas as vidas, a sua vida não seria a sua própria vida, a que nele estava impaciente e latente, mas um misto de encontro e desencontro, de desejo cumprido e desejo fracassado, embora, em rigor tudo fosse possível. E compreendeu que as suas grandes vitórias seriam as que não tinha desejado e que, por isso, nem sequer seriam vitórias.
Escreveu ao Pai. Disse-lhe que não era mais um navegador entre as ondas e o vento. Que era um homem estabelecido, em terra firme e que queria voltar a Vig. Foi a Mãe que respondeu à sua carta dizendo que o pai não o receberia.
        	Associado ao inglês, Hans começou a construir uma fortuna pessoal que nunca tinha projetado. Era um homem de negócios hábil porque se apercebia da natureza das coisas e da natureza das pessoas e negociava sem paixão. A fortuna não era nem a sua ambição, nem a sua aventura nem o seu jogo e nela nada de si próprio envolvia. Enriquecia porque a sua perceção e os seus cálculos estavam certos.
Algum tempo depois casou com a filha de um general liberal que desembarcara no Mindelo e cuja espada, mais tarde, transitando de herança em herança, se conservou na família.
Escolheu Ana porque tinha a cara redonda e rosada e cheirava a maçã como a primeira mulher criada e como a casa onde ele nascera, e porque o seu loiro de minhota lhe lembrava as tranças das mulheres de Vig.Pouco antes do seu casamento Hoyle morrera e Hans fundara a sua própria firma cuja prosperidade crescia. Era agora um homem rico e também respeitado e escutado. A sua honestidade era célebre e a sua palavra era de oiro.
Parecia estar já inteiramente integrado na cidade onde, quase ainda criança, vagueara estrangeiro e perdido. Conhecia um por um os notáveis do burgo: ele próprio agora era um dos notáveis do burgo. Amava o rio, o granito das casas e calçadas, as enormes tílias inchadas de brisas, as cameleiras de folhas polidas que floriram desde novembro até maio.
E foi no tempo das últimas camélias (vermelhas, pesadas e largas) que nasceu o seu primeiro filho.
"""

# Number of questions (per question type).
# Note: The system will attempt to generate up to the number of questions requested. It may not always be possible, depending on the text.
NR_QUESTIONS_PER_TYPE = 10

# ->DESIRED<- difficulty degree. You can request different difficulty degrees per question type.
# Note: The system will try to maximize, minimize or randomize the difficulty. It does not mean that it is possible in all cases, depending on the text.
DIFFICULTY_DEGREE = 'DIFF' # Possible options: 'DIFF', 'EASY' or 'RANDOM'

# List of possible requests
list_requests = [
    {'type': 'grammar', 'questions_requests': 
        [['g_sequence', NR_QUESTIONS_PER_TYPE, DIFFICULTY_DEGREE], 
        ['g_adverbstype', NR_QUESTIONS_PER_TYPE, DIFFICULTY_DEGREE], 
        ['g_dettype', NR_QUESTIONS_PER_TYPE, DIFFICULTY_DEGREE], 
        ['g_prontype', NR_QUESTIONS_PER_TYPE, DIFFICULTY_DEGREE], 
        ['g_conjtype', NR_QUESTIONS_PER_TYPE, DIFFICULTY_DEGREE], 
        ['g_prepdetpron', NR_QUESTIONS_PER_TYPE, DIFFICULTY_DEGREE], 
        ['g_verbfeats', NR_QUESTIONS_PER_TYPE, DIFFICULTY_DEGREE], 
        ['g_completeverb', NR_QUESTIONS_PER_TYPE, DIFFICULTY_DEGREE], 
        ['g_verbsmood', NR_QUESTIONS_PER_TYPE, DIFFICULTY_DEGREE], 
        ['g_verbstype', NR_QUESTIONS_PER_TYPE, DIFFICULTY_DEGREE], 
        ['g_simplecomplex', NR_QUESTIONS_PER_TYPE, DIFFICULTY_DEGREE]]
    }, 
    {'type': 'reading_comprehension', 'questions_requests': 
        [['rc_factualsyntax', NR_QUESTIONS_PER_TYPE, DIFFICULTY_DEGREE],
        ['rc_factualdependency', NR_QUESTIONS_PER_TYPE, DIFFICULTY_DEGREE],
        ['rc_factualsemantic', NR_QUESTIONS_PER_TYPE, DIFFICULTY_DEGREE],
        ['relative_pronoun', NR_QUESTIONS_PER_TYPE, DIFFICULTY_DEGREE],
        ['connectors', NR_QUESTIONS_PER_TYPE, DIFFICULTY_DEGREE]]
        }, 
    {'type': 'pronoun_reference', 'questions_requests': [
        ['pronoun_reference', NR_QUESTIONS_PER_TYPE, DIFFICULTY_DEGREE]]}
    ]

# check for errors in list_requests
if list_requests == -1:
    print('Por favor, selecione uma ou mais perguntas para geração.')
    sys.exit()

new_qgsystem = qgsystem.QgSystem() # init qgsystem
res_submitText = new_qgsystem.submitText(text_example) # submit text

# check for errors in text submission
if (res_submitText) != 1:
    print('Não foi possível gerar perguntas. Por favor, experimente outras opções/textos.')
    sys.exit()

# submit request
result = new_qgsystem.submitRequests(list_requests, READING_COMP_TYPES, NR_QUESTIONS_PER_TYPE)

# check for errors after request submission
if result == False:
    print('Não foi possível gerar perguntas. Por favor, experimente outras opções/textos.')
    sys.exit()

if 'rc' in result:
    if len(result['rc']) == 0 and len(result['grammar']) == 0 and len(result['pronref']) == 0:
        print('Não foi possível gerar perguntas. Por favor, experimente outras opções/textos.')
        sys.exit()

# Reading Comprehension
# Each RC question will have the following types and subtypes:
    #type: syntax , subtypes: syntax_facts, syntax_where, syntax_when
    #type: dep, subtypes: dep_facts, dep_how
    #type: sem, subtypes: sem_where, sem_when, sem_how
    #type: relative_pronoun, subtypes: relative_pronoun_facts, relative_pronoun_when, relative_pronoun_where, relative_pronoun_how
    #type: connectors, subtypes: connectors_when, connectors_why
for  q in result['rc']:
    print(q.getQuestion())
    print(q.fact_type)

# Reading Grammar
for  q in result['grammar']:
    print(q.getQuestion())

# Pronoun Reference
for  q in result['pronref']:
    print(q.getQuestion())

print('Sucesso! Foi criado um novo questionário! Ver pasta -- results.')
