from flask import Flask, request, redirect, render_template, url_for
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

    email_error = ''
    password_error = ''
    
    if is_email(email) == False:
        email_error = "Please enter a valid email address."
        email = ''
        return email_error
    else:
        return "Good Username"



@app.route("/")
def index ():
    return render_template('index.html')

    
    

app.run()


# If the user's form submission is not valid, you should reject it and re-render the form with some feedback to inform the user of what they did wrong. The following things should trigger an error:
#     The user leaves any of the following fields empty: username, password, verify password. do not use the email input type
#     The user's username or password is not valid -- for example, it contains a space character or it consists of less than 3 characters or more than 20 characters (e.g., a username or password of "me" would be invalid).
#     The user's password and password-confirmation do not match.  You should, however, use type='password' 
#     The user provides an email, but it's not a valid email. Note: the email field may be left empty, but if there is content in it, then it must be validated. The criteria for a valid email address in this assignment are that it has a single @, a single ., contains no spaces, and is between 3 and 20 characters long.

# Each feedback message should be next to the field that it refers to.

# For the username and email fields, you should preserve what the user typed, so they don't have to retype it. With the password fields, you should clear them, for security reasons.

# If all the input is valid, then you should show the user a welcome page that uses the username input to display a welcome message of: "Welcome, [username]!"
# Use templates (one for the index/home page and one for the welcome page) to render the HTML for your web app.



