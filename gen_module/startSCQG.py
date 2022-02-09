import sys
import os
import qgsystem
import time

from pathlib import Path

template_requests = [
    {
    'type': 'grammar', 
    'questions_requests': [
        ['g_sequence', 20, 'DIFF'],
        ['g_verbstype', 20, 'DIFF'],
        ['g_adverbstype', 20, 'DIFF'],
        ['g_prepdetpron', 20, 'DIFF'],
        ['g_dettype', 20, 'DIFF'],
        ['g_prontype', 20, 'DIFF'],
        ['g_conjtype', 20, 'DIFF'],
        ['g_verbsmood', 20, 'DIFF'],
        ['g_completeverb', 20, 'DIFF'],
        ['g_verbfeats', 20, 'DIFF'],
        ['g_simplecomplex', 20, 'DIFF'],
        ['r_factualsyntax', 20, 'DIFF']]
    },
    {
    'type': 'reading_comprehension', 
    'questions_requests': [
        ['rc_factualsyntax', 10, 'DIFF'],
        ['rc_factualsemantic', 10, 'DIFF'],
        ['rc_factualdependency', 10, 'DIFF']]
    }
]

def clean_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def check_exists(file_name):
    my_file = Path("texts/"+file_name)
    if my_file.is_file():
        return True
    else:
        return False

def check_questions(info_gen, type_question, difficulty, new_qgsystem):
    if info_gen == False:
        clean_console()
        print('\n [Informação] Não existem perguntas geradas para o ficheiro de texto submetido. Por favor, tente com outro ficheiro.')
        sub_generate(type_question, new_qgsystem)
    else:
        clean_console()
        print('\n [Informação] Sucesso! As perguntas geradas encontram-se na pasta "results" deste diretório.')
        main_menu(new_qgsystem)

def submit_requests(type_question, difficulty, new_qgsystem):
    list_requests = []

    if difficulty == "1":
        diff_request = 'DIFF'
    elif difficulty == "2":
        diff_request = 'EASY'
    else:
        diff_request = 'RANDOM'

    if type_question == "1":
        grammar_requests = {
        'type': 'grammar', 
        'questions_requests': [
            ['g_sequence', 100, diff_request],
            ['g_verbstype', 5, diff_request],
            ['g_adverbstype', 5, diff_request],
            ['g_prepdetpron', 5, diff_request],
            ['g_dettype', 5, diff_request],
            ['g_prontype', 5, diff_request],
            ['g_conjtype', 5, diff_request],
            ['g_verbsmood', 5, diff_request],
            ['g_completeverb', 5, diff_request],
            ['g_verbfeats', 5, diff_request],
            ['g_simplecomplex', 5, diff_request],
            ['r_factualsyntax', 5, diff_request]]
        }
        list_requests.append(grammar_requests)

    elif type_question == "2":
        rc_requests = {
        'type': 'reading_comprehension', 
        'questions_requests': [
            ['rc_factualsyntax', 10, diff_request],
            ['rc_factualsemantic', 10, diff_request],
            ['rc_factualdependency', 10, diff_request]]}
        list_requests.append(rc_requests)

    elif type_question == "3":
        pron_requests = {
        'type': 'pronoun_reference', 
        'questions_requests': [
            ['pronoun_reference', 10, diff_request]]}
        list_requests.append(pron_requests)

    else:
        pass

    info_gen = new_qgsystem.submitRequests(list_requests)

    check_questions(info_gen, type_question, difficulty, new_qgsystem)

def sub_chooseDif(type_question, new_qgsystem):
    ans=True
    while ans:
        print("""
        1. Difícil
        2. Fácil
        3. Aleatória
        4. Retroceder
        """)
        ans=input("Qual a dificuldade pretendida para as perguntas que irão ser geradas? ")
        if ans=="1" or ans =="2" or ans=="3":
            print("\n [Informação] O sistema irá agora tentar gerar as perguntas pretendidas, com base no ficheiro submetido. Aguarde, por favor.")
            time.sleep(3)
            submit_requests(type_question, ans, new_qgsystem)
        elif ans=="4":
            clean_console()
            sub_generate(type_question, new_qgsystem)
        else:
            clean_console()
            print("\n [!Erro] A sua escolha não é válida. Tente novamente.")

def sub_generate(type_question, new_qgsystem):
    ans=True
    while ans:
        print("""
        1. Submeter ficheiro de texto
        2. Retroceder
        3. Sair/Terminar
        """)
        ans=input("O que gostaria de fazer? ")
        if ans=="1":
            clean_console()
            print("\n Indique o nome do ficheiro de texto a partir do qual se irá gerar as perguntas.\n")
            print('Nota 1: O ficheiro de texto deverá ser criado e guardado na pasta "texts" deste diretório.')
            print('Nota 2: Alguns exemplos já se econtram disponíveis na pasta "texts" tais como "velhoeomar.txt", "gatomalhado.txt" e "canterville.txt".')
            file_name = input("\n Escreva aqui (exemplo: gatomalhado.txt): ")
            if check_exists(file_name) == True: 
                print("\n [Informação] O ficheiro vai agora ser processado. Aguarde, por favor.")
                time.sleep(3)
                new_qgsystem.submitFile("texts/"+file_name)
                clean_console()
                print("\n [Informação] Ficheiro de texto submetido com sucesso!")
                sub_chooseDif(type_question, new_qgsystem)
            else: 
                clean_console()
                print("\n [!Erro] O ficheiro não existe. Verifique o nome do ficheiro.")
        elif ans=="2":
            clean_console()
            main_menu(new_qgsystem)
        elif ans=="3":
            print("\n Até logo!") 
            ans = None
            sys.exit()
        else:
            clean_console()
            print("\n [!Erro] A sua escolha não é válida. Tente novamente.")

def main_menu(new_qgsystem):
    print("\n Bem-vindo ao melhor gerador de perguntas para a Língua Portuguesa!")
    ans=True
    while ans:
        print("""
        1. Gerar perguntas de gramática
        2. Gerar perguntas factuais para a compreensão de leitura
        3. Gerar perguntas de referenciação de pronomes
        4. Saber mais
        5. Conhecer os autores
        6. Sair/Terminar
        """)
        ans=input("O que gostaria de fazer? ")
        if ans=="1":
            clean_console()
            sub_generate(ans, new_qgsystem)
        elif ans=="2":
            clean_console()
            sub_generate(ans, new_qgsystem)
        elif ans=="3":
            clean_console()
            sub_generate(ans, new_qgsystem)
        elif ans=="4":
            clean_console()
            print("\n [Informação] Esta ferramenta foi desenvolvida no âmbito de uma Dissertação de Mestrado pela Faculdade de Engenharia da Universidade do Porto - MIEIC")
        elif ans=="5":
            clean_console()
            print("\n Bernardo Leite. Henrique Lopes Cardoso. Luís Paulo Reis.")
        elif ans=="6":
            print("\n Até logo!") 
            ans = None
            sys.exit()
        else:
            clean_console()
            print("\n [!Erro] A sua escolha não é válida. Tente novamente.")


def gui_request(list_requests, text):

    new_qgsystem = qgsystem.QgSystem() # init qgsystem

    info1 = new_qgsystem.submitFile('no_name', text)
    print(info1)

    info2 = new_qgsystem.submitRequests(list_requests)
    print(info2)
    
def main():

    new_qgsystem = qgsystem.QgSystem() # init qgsystem

    clean_console()
    main_menu(new_qgsystem) # init menu
    
    #text = sys.argv[1]
    #file_name = "texts/" + text
