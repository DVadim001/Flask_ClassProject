from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Простейшая БД для хранения вопросов и ответов
questions = [
    {'id': 1, 'title': 'Как использовать фласк', 'content': 'Я не знаю, как использовать фласк'},
    {'id': 2, 'title': 'Как использовать джанго', 'content': 'Я не знаю, как использовать джанго'},
]

answers = [
    {'id': 1, 'question_id': 1, 'answer': 'Просто скачайте фласк через пип инсталл'},
    {'id': 2, 'question_id': 2, 'answer': 'Просто скачайте джанго через пип инсталл'}
]



@app.route('/')
def hello_world():
    return render_template('index.html', questions=questions)


# страница с деталями вопроси и ответа
@app.route('/question/<int:question_id>')
def question(question_id):
    question = next((q for q in questions if q['id'] == question_id), None)
    if question:
        question_answers = [a for a in answers if a['question_id'] == question_id]
        return render_template('question.html', question=question, question_answers=question_answers)
    else:
        return "Вопрос не найден!"


# Страница для добавления нового вопроси
@app.route('/ask', methods=['GET', 'POST'])
def ask():
    if request.method == 'POST':
        # Извлечение данных из формы
        title = request.form['title']
        content = request.form['content']

        # Добавление нового вопроса
        new_content = {
            'id': len(questions) + 1,
            'title': title,
            'content': content
        }

        questions.append(new_content)
        return redirect(url_for('hello_world'))

    else:
        return render_template('ask.html')


@app.route('/search')
def search():
    query = request.args.get('query', '')
    filtered_questions = [q for q in questions if query.lower() in q['title'].lower()
                          or query.lower() in q['content'].lower()]
    return render_template('search_results.html', questions=filtered_questions)


app.run(debug=True)
