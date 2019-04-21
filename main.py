from flask import Flask, redirect, render_template, request, session, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] =True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:launchcodelc101@localhost:8889/build-a-blog'

app.config['SQLALCHEMY_ECHO'] = True

db =SQLAlchemy(app)
app.secret_key = "k3nd3ybtje9J3saY"

class Blog(db.Model):
    post_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    content = db.Column(db.String(1000))
    
    def __init__(self, title, content):
        self.title = title
        self.content =  content


@app.route('/blog')
def blog():
    id = request.args.get('id')
    if id:
        post = Blog.query.filter_by(post_id=id).first()
        print("post: ", post)
        return render_template("blog.html", title = "Blog ", posts = [post] )
    else:
        all_posts = Blog.query.all()
        print("all post ", all_posts)
        return render_template("blog.html", title = "Build a Blog", posts=all_posts)

@app.route('/newpost', methods=['GET', 'POST'])
def newpost():
    if request.method == 'POST':
        post_title = request.form['title']
        post_content = request.form['content']

        if not post_title:
            flash("Please enter post title.", category="title_error")

        if not post_content:
            flash("Please enter contents for the post.", category="content_error")
            return render_template("newpost.html", title = post_title, content = post_content)
        

        blog = Blog(post_title, post_content)
        db.session.add(blog)
        db.session.commit()

        flash("Blog entry successful.")
        all_posts = Blog.query.all()
        return render_template("/blog.html", posts=all_posts)
    else:
        return render_template("newpost.html")  

if __name__ == '__main__':
    app.run()
