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

@app.errorhandler(404)
def pageNotFound(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run()