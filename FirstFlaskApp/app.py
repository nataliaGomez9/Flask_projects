from flask import Flask, request, render_template
from markupsafe import escape 
from flask_debugtoolbar import DebugToolbarExtension
from random import randint, choice, sample 

app = Flask(__name__) #--> defines app

app.config['SECRET_KEY']= "TOPSECRET"
debug = DebugToolbarExtension(app)

@app.route('/')
def home_page():
    html = """ 
    <html>
      <body>
        <h1>Home Page</h1>
        <p>Welcome to my app</p>
        <a href='/hello'>Go to Hello page</a>
      </body> 
    </html>
     """
    return render_template('home.html')

@app.route('/form')
def show_form():
    return render_template('form.html')

@app.route('/form-2')
def show_form_2():
    return render_template('form_2.html')

compliments= ["beutiful", "great", "sweet", "smart", "sucessful"]
@app.route('/greet')
def get_greeting():
    username = request.args["username"]
    nice_things = choice(compliments)
    return render_template('greet.html', username=username, compliment = nice_things)

@app.route('/greet-2')
def get_greeting_2():
    username= request.args["username"]
    wants= request.args.get("yes_compliments")
    three_nice_things = sample(compliments,3)
    return render_template('greet_2.html', username= username, wants_compliments=wants, compliments=three_nice_things )

@app.route('/lucky')
def lucky_number():
    number = randint(1,10)
    return render_template('lucky.html', lucky_num = number, msg = "your so lucky")

@app.route('/spell/<word>')
def spell_word(word):
    return render_template('spell_word.html', word=word)

@app.route('/hello') 
def say_hello():
#    html = """ 
#   <html>
#     <body>
#       <h1>Hello!</h1>
#       <p>This is the hello page</p>
#      </body> 
#   </html>
#    """
#    return html  

    return render_template("hello.html")

@app.route('/search')
def search():
    term = request.args["term"]
    sort = request.args["sort"]
    # use term to find db data that matches term
    return f"<h1>Search Results For : {term}</h1> <p>Sorting by:{sort}</p>"

@app.route('/add-comment')
def add_comment_form():
    return """
    <h1>Add Comment</h1>
    <form method="POST">
        <input type= 'text' placeholder='comment' name='username'/>
        <input type= 'text' placeholder='comment' name='comment'/>
        <button>Submit</buttom>
    </form>
  """
@app.route('/add-comment',methods=["POST"]) 
def save_comment():
     return """
     <h1>SAVE YOUR COMMENT</H1>
     """
    