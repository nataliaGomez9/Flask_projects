from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import dictionary_stories

app = Flask(__name__)

app.config['SECRET_KEY']= "SECRET"
debug = DebugToolbarExtension(app)

@app.route('/')
def home_page():
    # story_options= [ "story_1", "story_2"]
    return render_template('home.html', stories =dictionary_stories.values() )

# @app.route('/dropdown')
# def dropdown_menu():
#     selected_options= request.form['dropdown']
#     return render_template()

@app.route('/questions')
def question_page():
    story_id = request.args["story_id"]
    story = dictionary_stories[story_id]
    prompts = story.prompts 
    return render_template('questions.html', prompts = prompts, story_id= story_id,title=story.title )

@app.route('/story')  
def show_story():
    story_id = request.args["story_id"]
    story = dictionary_stories[story_id]

    text = story.generate(request.args)

    return render_template('show_story.html', title=story.title, text = text)
