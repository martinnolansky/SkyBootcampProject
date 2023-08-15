from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('home.html')

@app.route('/about')
def about():
   return 'The About Page'

@app.route('/blog')
def blog():
    posts = [{'title': 'Technology in 2023', 'author': 'Martin'},
     {'title': 'Technology in 2022', 'author': 'Nolan'}]
    return render_template('blog.html', author = "Martin", sunny=True, posts=posts)

@app.route('/blog/<string:blog_id>') # Specify the blog ID will be a variable in the url
def blogpost(blog_id):
    return 'This is blog post number ' + blog_id

if __name__ == '__main__':
    app.run()