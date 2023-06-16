from flask import Flask, render_template, request, escape
from vsearch import search4letters

'''The __name__ value (maintained by the interpreter) identifies 
the currently active module.'''
app = Flask(__name__)


def log_request(req: 'flask_request', res= 'flask_response') -> None:
    with open('vsearch.log', 'a') as log:
        print(
            req.form,
            req.remote_addr,
            req.user_agent,
            res,
            file=log,
            sep='|')


'''The @ symbol before a function's name identifies it as a decorator. 
Decorators let you change the behaviour of an existing function without 
having to change the function's code. 
A function can be decorated more than once'''
@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search4letters(phrase, letters))
    log_request(request, results)
    return render_template('results.html',
                           the_phrase=phrase,
                           the_letters=letters,
                           the_title=title,
                           the_results=results)


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='Welcome to search4letters on the web!')


@app.route('/viewlog')
def view_the_log() -> 'html':
    contents = []
    with open('vsearch.log') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
    titles = ('Form data', 'Remote addr', 'User_agent', 'Results')
    return render_template('viewlog.html',
                           the_title='View Log',
                           the_row_titles=titles,
                           the_data=contents)


'''Prepare for deployment to AWS PythonAnywhere's cloud-hosted environment'''
if __name__ == '__main__':
    app.run(debug=True)
