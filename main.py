from flask import Flask, request, redirect, render_template
import re

app = Flask(__name__)
app.config['DEBUG'] = True

regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

def is_email(email):
    if(re.search(regex,email)):  
        return True
    else:
        return False


@app.route('/', methods = ['POST'])
def user_varification():
    email = request.form['email']
    password = request.form['password']
    verify_password = request.form['verify-password']
    username = request.form['username']

    email_error = ''
    password_error = ''
    verify_error = ''
    username_error = ''
    
    if email == '':
        pass
    else:
        if is_email(email) == False:
            email_error = "Please enter a valid email address."
    
    if username == '':
            username_error = "Please enter a password between 3 and 20 characters."
    else:
       if not len(username) > 3 or len(username) > 20:
        username_error = "Please enter a password between 3 and 20 characters."
        
    if password == '':
        password_error = "Please enter a password between 3 and 20 characters."
    else:
        if not len(password) > 3 or len(password) > 20:
            password_error = "Please enter a password between 3 and 20 characters."

    if verify_password != password:
        verify_error = "Passwords do not match."
    else:
        if verify_password == '':
            verify_error = "Passwords do not match."

    if not email_error and not password_error and not verify_error:
        return redirect ('/welcome?username=' + username)

    else:
        return render_template('index.html', email_error = email_error, password_error = password_error, verify_error = verify_error, username_error = username_error)


@app.route('/welcome', methods = ['GET'])
def welcome():
    username = request.args.get('username')
    return render_template ('welcome.html', username=username)

@app.route("/")
def index ():
    return render_template('index.html')

app.run()