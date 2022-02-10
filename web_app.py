from flask import Flask, render_template, flash, request
import auxgenquizz

import sys
sys.path.append('gen_module/')
sys.path.append('gen_module/utils')

import qgsystem

app = Flask(__name__)
app.secret_key = "secret123"

ENV = 'dev'

if ENV == 'dev':
    app.debug = True
else:
    app.debug = False

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/quizz/<string:id>/')
def quizz(id):
    return render_template('quizz.html', id = id)

# Generate Quizz
@app.route('/gen_quizz', methods=['GET', 'POST'])
def gen_quizz():
    if request.method == 'POST':
        diff = request.form['diff']
        nr_quest = request.form['nr_quest']
        text_gen = request.form['text_gen']

        if diff == '' or nr_quest == '' or text_gen == '':
            error = 'Por favor, preencha os campos necessários.'
            return render_template('gen_quizz.html', error=error)
        
        list_requests, list_rc, nr_quest = auxgenquizz.checkQuestionsSelection(request.form)
        
        if list_requests == -1:
            error = 'Por favor, selecione uma ou mais perguntas para geração.'
            return render_template('gen_quizz.html', error=error)
    
        new_qgsystem = qgsystem.QgSystem() # init qgsystem

        res_submitText = new_qgsystem.submitText(text_gen)

        if (res_submitText) != 1:
            return render_template('gen_quizz.html', error='Não foi possível gerar perguntas. Por favor, experimente outras opções/textos.')

        res_submitRequests = new_qgsystem.submitRequests(list_requests, list_rc, nr_quest)
        if (res_submitRequests) == False:
            print("Error during text submission!")
            return render_template('gen_quizz.html', error='Não foi possível gerar perguntas. Por favor, experimente outras opções/textos.')

        if len(list_rc) > 0 and 'rc' in res_submitRequests:
            #before it was a call to filterRcQuest
            if len(res_submitRequests['rc']) == 0 and len(res_submitRequests['grammar']) == 0 and len(res_submitRequests['pronref']) == 0:
                return render_template('gen_quizz.html', error='Não foi possível gerar perguntas. Por favor, experimente outras opções/textos.')
        
        print("\n\n\n", res_submitRequests, "\n\n\n")
        flash('Foi criado um novo questionário.', 'success')
        return render_template('quizz.html', data = res_submitRequests)

    return render_template('gen_quizz.html')


if __name__ == '__main__':
    app.secret_key = "secret123"
    app.run()