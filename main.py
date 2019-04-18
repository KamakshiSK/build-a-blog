from flask import Flask, redirect, render_template, request, session, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] =True
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://build-a-blog:lauchcodelc101@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True

db =SQLAlchemy(app)
app.secret_key = "k3nje9J3saY"

class Blog(db.Model):
    post_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    content = db.Column(db.String(1000))
    
    def __init__(self, title, content):
        title = title
        content =  content

@app.route('/blog', methods=['GET', 'POST'])
def index():
    pass

@app.route('/newpost', methods=['GET', 'POST'])
def newpost():
    pass

if __name__ == '__main__':
    app.run()
