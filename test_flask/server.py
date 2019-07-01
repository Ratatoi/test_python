from flask import Flask , render_template, request
from forms import SignUpForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'batman'

@app.route('/')
def home():
    return 'Hello World!'

@app.route('/about')
def about():
    return 'The About page'

@app.route('/blog')
def blog():
    posts = [{'title': 'Tech in 2019', 'author': 'Batman'},
            {'title': 'Krypton', 'author': 'Superman'}]
    return render_template('blog.html', author='Spiderman', sunny=False, posts=posts)

@app.route('/blog/<string:blog_id>')
def blogpost(blog_id):
    return 'This is blog post number ' + blog_id

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.is_submitted():
        result = request.form
        return render_template('user.html', result=result)
    return render_template('signup.html', form=form)


if __name__ == '__main__':
    app.run()