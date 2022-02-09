import mlconjug
import warnings
import sys
warnings.filterwarnings('ignore') 

# To use mlconjug with the default parameters and a pre-trained conjugation model.
default_conjugator = mlconjug.Conjugator(language='pt')

def conjugateVerb(verb, mood, tense, person, number):
    person_number = ''

    if person == '1' and number == 'Sing':
        person_number = '1s'
    elif person == '2' and number == 'Sing':
        person_number = '2s'
    elif person == '3' and number == 'Sing':
        person_number = '3s'
    elif person == '1' and number == 'Plur':
        person_number = '1p'
    elif person == '2' and number == 'Plur':
        person_number = '2p'
    elif person == '3' and number == 'Plur':
        person_number = '3p'
    else:
        return -1

    try:
        verb = default_conjugator.conjugate(verb).conjug_info[mood][tense][person_number]
        return verb
    except:
        return -1