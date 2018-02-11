# Infrastructure test page.
import os
from flask import Flask
from flask import Markup
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask import request
from flask import json

app = Flask(__name__)

# Configure MySQL connection.
db = SQLAlchemy()
db_uri = 'mysql://root:supersecure@db/information_schema'
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route("/")
def test():
    mysql_result = False
    # TODO REMOVE FOLLOWING LINE AFTER TESTING COMPLETE.
    db.session.query("1").from_statement("SELECT 1").all()
    try:
        if db.session.query("1").from_statement("SELECT 1").all():
            mysql_result = True
    except:
        pass

    if mysql_result:
        result = Markup('<span style="color: green;">PASS</span>')
    else:
        result = Markup('<span style="color: red;">FAIL</span>')

    # Return the page with the result.
    return render_template('index.html', result=result)

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

@app.route('/somewhere')
def index():
    user = {'username': 'miguel'}
    return '''
<html>
    <head>
        <title>Home Page - Microblog</title>
    </head>
    <body>
        <h1>Hello, ''' + user['username'] + '''!</h1>
    </body>
</html>'''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug = True)
