import logging

from flask import Flask #, render_template, request


app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello COMS4156!'

# @app.route('/form')
# def form():
#     return render_template('form.html')

# @app.route('/submitted', methods=['POST'])
# def submitted_form():
#     name = request.form['name']
#     email = request.form['email']
#     site = request.form['site_url']
#     comments = request.form['comments']

#     return render_template(
# 	    'submitted_form.html',
# 	    name=name,
# 	    email=email,
# 	    site=site,
# 	    comments=comments)


@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500